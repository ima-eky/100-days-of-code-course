from bs4 import  BeautifulSoup
import requests

response=requests.get("https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors")
print(response.text)