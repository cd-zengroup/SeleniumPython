# Selenium 3

from selenium import webdriver

# Web Driver import from selenium

import time

# Wait time for execution

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

# Path of the chrome driver called as executable path

driver.maximize_window()

# Chrome window maximize

driver.get("https://rudder.dev.qntmnet.com/login")

# From get method any url can be executed

driver.find_element_by_name("email").send_keys("hemang@zengroup.co.in")

# From html, name and id both can be derived for webdriver

driver.find_element_by_id("user_check").click()

time.sleep(1)

# Wait time add for password field otherwise error might come

driver.find_element_by_id("password").send_keys("P@$$w0rd")

driver.find_element_by_id("passwrd_step").click()

print("Login Test Passed")

# End of login page


