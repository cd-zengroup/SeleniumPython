from selenium import webdriver

import time

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

serv_object = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome("service=serv_object")

driver.maximize_window()

driver.get("https://rudder.dev.qntmnet.com/login")

#driver.find_element(By.XPATh, "/html/body/div/div/div/div/div[2]/div/div/div/div/form/div[1]/div[1]/input").send_keys("hemang@zengroup.co.in")

#driver.find_element(By.ID, "user_check").click()

#time.sleep(1)

#driver.find_element(By.NAME, "password").send_keys("P@$$w0rd")

#driver.find_element(By.ID, "passwrd_step").click()

#print("Login Test Passed")
