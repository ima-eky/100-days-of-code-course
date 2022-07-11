import requests
from bs4 import BeautifulSoup
import  smtplib
import lxml
my_email = "YOUR EMAIL"
password = "YOUR PASSWORD"

# using requests library to get amazon website html for particular product

URL= "URL OF PRODUCT YOU WANT TO TRACK"
reponse=requests.get(url=URL,headers={
    "Accept-Language":"en-US,en;q=0.5",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"})
product_details=reponse.text
# using beautiful soup to scrape product details(price,title and so on)
soup=BeautifulSoup(product_details,features="lxml")
product_price=soup.find(name="td",class_="a-span12").getText().split("$")[1]
product_title=soup.find(name="span",id="productTitle").getText().strip()
BUY_PRICE=20
if float(product_price) <= BUY_PRICE:
    message=f"{product_title} is now {product_price}"

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="RECIPIENT EMAIL/YOUR EMAIL",msg=f"Subject:Amazon Price Alert\n\n"
                                                                                      f"{message}\n{URL}")
