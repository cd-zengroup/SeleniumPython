import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.implicitly_wait(25)

MyWait = WebDriverWait(driver, 60)

driver.get("http://169.254.1.1")

time.sleep(3)

FirstPageConfigureButton = driver.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[3]/div[2]/a").click()

time.sleep(7)

ScrollDown = driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

DProceed = driver.find_element_by_id("btnIPConfigNext").click()

time.sleep(3)

EMail = driver.find_element_by_id("txt_c_email").send_keys("hemang4it2@gmail.com")
Password = driver.find_element_by_id("txt_c_password").send_keys("P@$$w0rd")
MProceed = driver.find_element_by_id("btnOpModenext").click()

time.sleep(17)

Site = driver.find_element_by_id("dropdwnSiteName")
drp = Select(Site)
drp.select_by_visible_text('SeleniumPython')

time.sleep(7)

RProceed = driver.find_element_by_id("btnCloudSiteSetupNext").click()

time.sleep(3)

OProceed = driver.find_element_by_id("btnMasterAPnext").click()

time.sleep(3)

WLAN = driver.find_element_by_id("txt_c_wlan").send_keys("t470")
SSID = driver.find_element_by_id("txt_c_ssid").send_keys("t470")
Passkey = driver.find_element_by_id("txt_c_wlankey").send_keys("12345678")
CProceed = driver.find_element_by_id("btnCloudSSIDnext").click()

time.sleep(5)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

CSProceed = driver.find_element_by_id("btnFinishconfigure").click()

print("AP On-Boarded Successfully")