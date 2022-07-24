from  selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path=Service("C:/Development/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=chrome_driver_path)
url="http://orteil.dashnet.org/experiments/cookie/"
driver.get(url)

upgrade_purchase=driver.find_elements(By.CSS_SELECTOR,"#store b")
price_of_upgrade=[name.text.strip().split("-")[-1].replace(",","") for name in upgrade_purchase][:8]
price_as_int= [int(number) for number in price_of_upgrade]

#Get upgrade item ids.
items = driver.find_elements(By.CSS_SELECTOR,"#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes

button_click = driver.find_element(By.ID, "cookie")

while True:
    #Get cookie to click on
    button_click.click()
    cookie_upgrades = {}
    if time.time() > timeout:
        for n in range(len(price_as_int)):
            cookie_upgrades[price_as_int[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element(By.ID,"money").text.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID,to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

        # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID,"cps").text
        print(cookie_per_s)
        break

