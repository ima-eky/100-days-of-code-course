import json
from telnetlib import EC

from bs4 import  BeautifulSoup
import requests
import lxml
# using beautiful/requests to scrape all listings from the Zillow web address
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

CHROME_DRIVER_PATH="C:/Development/chromedriver_win32/chromedriver.exe"
GOOGLE_FORM="https://docs.google.com/forms/d/e/1FAIpQLSctp5Tn-rd6Rg9YvSZuXGibLLNzAAuZQmd-uI1DMXTtxlw97Q/viewform?usp=sf_link"
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate"
}
response=requests.get('https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D',headers=headers)
website_html=response.text
soup=BeautifulSoup(website_html,features="html.parser")

# creates a list of links of listing scraped
data = json.loads(soup.select_one("script[data-zrr-shared-data-key]").contents[0].strip("!<>-"))

website_links = [result["detailUrl"] for result in data["cat1"]["searchResults"]["listResults"]]
# Amending house_links to have all proper URLS
website_links = [link.replace(link, "https://www.zillow.com" + link) if not link.startswith("http") else link
                 for link in website_links]


# Getting the prices of the listings
cost=[]
second_data=data["cat1"]["searchResults"]["listResults"]
for item in second_data:
    try:
        price=item["price"]
    except KeyError:
        price=item['units'][0]['price']
    finally:
        cost.append(price)

cost = [price.split("+")[0].split("/")[0].split("$")[1].replace(",", "") for price in cost]

# Getting the Addresses
addresses = []
for item in second_data:
    address = item['address']
    addresses.append(address)

# Filling up the Form
for n in range(len(addresses)):
    try:
        driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
        driver.get(GOOGLE_FORM)

        form_address = driver.find_element(By.XPATH,
                                           '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        form_address.send_keys(addresses[n])
        form_address.send_keys(Keys.ENTER)

        form_price = driver.find_element(By.XPATH,
                                         '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        form_price.send_keys(cost[n])
        form_price.send_keys(Keys.ENTER)

        form_link = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        form_link.send_keys(website_links[n])

        # Cliking the Button
        # submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')))
        button.click()
    except:
        pass
