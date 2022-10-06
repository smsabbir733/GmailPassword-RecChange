"""
We are using selenium documentation to buield this softwere
https://selenium-python.readthedocs.io/
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument('disable-infobars')
chrome_options.add_argument('--disable-logging')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--disable-web-security')

driver = webdriver.Chrome("chromedriver.exe", options=chrome_options)

driver.get("http://gmail.com")
# print(input("Stop :"))

elem = driver.find_element(By.ID, "identifierId")

elem.send_keys("sabbirtestinghrome@gmail.com")

next_button = driver.find_element(By.ID, "identifierNext")
next_button.click()

# TODO : use "SelectorsHub" find X path video : https://youtu.be/srExpm-d9dU ,
#  https://youtube.com/playlist?list=PLmRg3gEG2XIackdOpGvb_jEX1ywaplUmh
