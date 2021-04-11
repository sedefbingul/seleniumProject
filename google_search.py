from time import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# or specify the path: driver = webdriver.Chrome('/path/to/chromedriver')
sleep(5)

driver.get("https://google.com")

search_text_box = driver.find_element_by_name("q")
search_text_box.clear()
search_text_box.send_keys("python selenium integration")
search_text_box.send_keys(Keys.RETURN)
