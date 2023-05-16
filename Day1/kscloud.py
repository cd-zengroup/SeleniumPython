from selenium import webdriver
import time


driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get("https://rudder.dev.qntmnet.com/login")


driver.find_element_by_name("email").send_keys("ks.zengroup@gmail.com")
driver.find_element_by_id("user_check").click()

time.sleep(1)
driver.find_element_by_id("password").send_keys("P@$$w0rd")
driver.find_element_by_id("passwrd_step").click()
driver.find_element_by_class_name("skin-blue sidebar-mini  pace-done").click()