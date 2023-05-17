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

ConnectivityMode = driver.find_element_by_id("ddlConnectivity")
drp = Select(ConnectivityMode)

time.sleep(2)

drp.select_by_visible_text('USB')

time.sleep(1)

UProceed = driver.find_element_by_id("btnIPConfigNext").click()

time.sleep(15)

Email = driver.find_element_by_name("c_email").send_keys("hemang4it2@gmail.com")
Password = driver.find_element_by_id("txt_c_password").send_keys("P@$$w0rd")

time.sleep(1)

MProceed = driver.find_element_by_id("btnOpModenext").click()

time.sleep(5)

SiteSelection = driver.find_element_by_id("dropdwnSiteName")
drp = Select(SiteSelection)

time.sleep(2)

drp.select_by_visible_text('SeleniumPython')

time.sleep(1)

RProceed = driver.find_element_by_id("btnCloudSiteSetupNext").click()

time.sleep(3)

OProceed = driver.find_element_by_id("btnMasterAPnext").click()

time.sleep(1)

Wlan = driver.find_element_by_id("txt_c_wlan").send_keys("scenario8")
Sssid = driver.find_element_by_id("txt_c_ssid").send_keys("scenario8")
Key = driver.find_element_by_id("txt_c_wlankey").send_keys("12345678")
ipaddress = driver.find_element_by_id("txtCloudLSIP").send_keys("192.168.1.1")
Subnet = driver.find_element_by_id("txtCloudLSMask").send_keys("255.255.255.0")

time.sleep(1)

CSummary = driver.find_element_by_id("btnCloudSSIDnext").click()

time.sleep(5)

FProceed = driver.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[18]/div[2]/div/span[2]")
driver.execute_script("arguments[0].click();", FProceed)

print("AP On-Boarded Successfully")