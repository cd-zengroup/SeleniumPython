from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")

options = Options()
options.add_argument("--remote-debugging-port=9222")  # Use an arbitrary port number
options.add_experimental_option("detach", True)  # Keep the browser window open after exiting the script

driver = webdriver.Chrome(service=serv_obj, options=options)


driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# ID & Name locators
# driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")


# linktext & partial linktext

#driver.find_element(By.LINK_TEXT, "Register").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()

#driver.close()
#driver.quit()




