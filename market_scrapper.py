import selenium
import pandas as pd

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(5)

driver.get(url='https://lostark.game.onstove.com/Market')

search_box = driver.find_element_by_id('txtItemName')

search_box.send_keys('머리')
search_box.send_keys(Keys.RETURN)


name = driver.find_element_by_css_selector("#tbodyItemList > tr:nth-child(1) > td:nth-child(1) > div > span.name")
print(name.text)
price = driver.find_element_by_css_selector('#tbodyItemList > tr:nth-child(1) > td:nth-child(2) > div > em')
print(price.text)