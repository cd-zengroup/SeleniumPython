import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

MyWait = WebDriverWait(driver, 60)

driver.get("http://169.254.1.1")

time.sleep(3)

FirstPageConfigureButton = driver.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[3]/div[2]/a/span[2]").click()

time.sleep(7)

Interface = driver.find_element_by_id("ddlWANPort")
drp = Select(Interface)

time.sleep(2)

drp.select_by_visible_text('eth1')

time.sleep(1)

proceed = driver.find_element_by_id("btnIPConfigNext")
driver.execute_script("arguments[0].click();", proceed)
