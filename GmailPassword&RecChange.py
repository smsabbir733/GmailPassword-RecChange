from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")
driver.get("http://gmail.com")
assert "Python" in driver.title
elem = driver.find_element(By.id="identifierId", "q")
elem.clear()
elem.send_keys("sabbir")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
