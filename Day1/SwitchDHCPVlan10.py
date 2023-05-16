from selenium import webdriver

# Webdriver imported successfully from selenium

import time


driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get("http://10.20.0.51")

driver.find_element_by_css_selector(".wizard__button").click()

time.sleep(5)

driver.find_element_by_css_selector("form.u-pos--rel:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)").send_keys(0)



# driver.find_element_by_class_name("form.u-pos--rel:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)").send_keys("10")
driver.find_element_by_id("vlantag").click()
driver.find_element_by_css_selector("div.wizard__buttons--item:nth-child(2) > p:nth-child(1)").click()