from selenium import webdriver

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://mail.zengroup.co.in/")

driver.maximize_window()

driver.find_element_by_name("User").send_keys("chaitanya@zengroup.co.in")
driver.find_element_by_id("Password").send_keys("Zen@Hell1234")
driver.find_element_by_name("Logon").click()
driver.find