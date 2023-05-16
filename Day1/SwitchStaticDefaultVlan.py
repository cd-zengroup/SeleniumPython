from selenium import webdriver

# Webdriver imported successfully from selenium

import time


driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get("http://10.20.0.51")

driver.find_element_by_css_selector(".wizard__button").click()

time.sleep(5)

driver.find_element_by_css_selector("div.col:nth-child(3) > div:nth-child(2) > div:nth-child(1)").click()
driver.find_element_by_css_selector("div.wizard__buttons--item:nth-child(2) > p:nth-child(1)").click()

time.sleep(10)

driver.find_element_by_class_name("quantumInput").send_keys("hemang4it2@gmail.com")
driver.find_element_by_css_selector("div.field:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)").send_keys("P@$$w0rd")
driver.find_element_by_css_selector("div.wizard__buttons--item:nth-child(2) > p:nth-child(1)").click()

time.sleep(7)

driver.find_element_by_css_selector("div.upgrade__buttons:nth-child(3)").click()

time.sleep(1)

driver.find_element_by_css_selector("div.field:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").click()
driver.find_element_by_css_selector("li.ivu-select-item:nth-child(1)").click()
driver.find_element_by_css_selector("div.field:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").click()
driver.find_element_by_css_selector(".ivu-select-visible > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1)").click()
driver.find_element_by_css_selector("div.wizard__buttons--item:nth-child(2) > p:nth-child(1)").click()

time.sleep(1)

driver.find_element_by_css_selector(".wizard__button > span:nth-child(1)").click()

print("Device On-Boarded Successfully")
