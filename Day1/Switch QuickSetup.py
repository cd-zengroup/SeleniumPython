from selenium import webdriver

# Webdriver imported successfully from selenium

import time


driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get("http://10.20.0.51")

driver.find_element_by_class_name("wizard__button").click()

time.sleep(5)

driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div[3]/div[2]/div").click()
driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div[4]/div[2]/p").click()

time.sleep(10)

driver.find_element_by_name("input").send_keys("hemang4it2@gmail.com")
driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/form/div[2]/div[1]/div/input").send_keys("P@$$w0rd")
time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div[5]/div[2]/p").click()
driver.find_element_by_xpath("//div[@class='upgrade__buttons' or 'upgrade--skip wizard__buttons--item']").click()
driver.find_element_by_css_selector("div[name='site'] div[class='ivu-select-selection']").click()
driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/form/div[1]/div[1]/div/div[1]/div[2]/ul[2]/li[1]").click()
driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/form/div[2]/div[1]/div/div[1]/div[2]/ul[2]/li").click()
driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div[3]/div[2]/p").click()
driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div[5]").click()