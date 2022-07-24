# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# PROMISED_UP="150"
# PROMISED_DOWN="10"
# CHROME_DRIVER_PATH="C:/Development/chromedriver_win32/chromedriver.exe"
# TWITTER_EMAIL="YOUR EMAIL"
# TWITTER_PASSWORD="YOUR PASSWORD"
# URL="https://www.speedtest.net/result/13403946607"
#
#
# class InternetSpeedTwitterBot:
#     def __init__(self, driver_path):
#         self.driver = webdriver.Chrome(service=Service(driver_path))
#         self.up = 0
#         self.down = 0
#
#     def get_internet_speed(self):
#         self.driver.get(URL)
#
#     def tweet_at_provider(self):
#         pass
#
#
# bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
# bot.get_internet_speed()
# bot.tweet_at_provider()