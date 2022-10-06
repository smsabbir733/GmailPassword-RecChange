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

driver = webdriver.Chrome("chromedriver.exe", options = chrome_options)

driver.get("http://gmail.com")
# print(input("Stop :"))

elem = driver.find_element(By.ID, "identifierId")

elem.send_keys("smsabbir6001@gmail.com")

next_button = driver.find_element(By.ID, "identifierNext")
next_button.click()