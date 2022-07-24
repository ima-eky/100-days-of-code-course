from  selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path=Service("C:/Development/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=chrome_driver_path)
url="http://secure-retreat-92358.herokuapp.com/"
driver.get(url)
first_name=driver.find_element(By.NAME,"fName")
last_name=driver.find_element(By.NAME,"lName")
email=search=driver.find_element(By.NAME,"email")
first_name.send_keys("Ima-Abasi")
last_name.send_keys("Ekanem")
email.send_keys("mymail@yahoo.com")
email.send_keys(Keys.ENTER)
first_name.send_keys(Keys.ENTER)
last_name.send_keys(Keys.ENTER)
sign_up_button=driver.find_element(By.CLASS_NAME,"btn btn-lg btn-primary btn-block")
sign_up_button.click()
driver.quit()
