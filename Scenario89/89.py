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

#ProtocolSelection = driver.find_element_by_id("ddlProtocol")
#drp = Select(ProtocolSelection)

#time.sleep(2)

#drp.select_by_visible_text('PPPoE')

#time.sleep(1)

Vlan = driver.find_element_by_id("chkVLAN").click()
VlanText = driver.find_element_by_id("txtVLAN").send_keys("20")
#PUsername = driver.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[8]/div[1]/div/fieldset/div[17]/input").send_keys("test")
#PPassword = driver.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[8]/div[1]/div/fieldset/div[18]/input").send_keys("test")
FetchIP = driver.find_element_by_id("fetchIPAddress").click()

time.sleep(45)

ProtocolSelection = driver.find_element_by_id("ddlProtocol")
drp = Select(ProtocolSelection)

time.sleep(2)

drp.select_by_visible_text('Static')

time.sleep(1)

IP = driver.find_element_by_id("txtIPAddr").clear()
driver.find_element_by_id("txtIPAddr").send_keys("10.20.20.20")

time.sleep(1)

proceed = driver.find_element_by_id("btnIPConfigNext")
driver.execute_script("arguments[0].click();", proceed)

time.sleep(5)

Email = driver.find_element_by_name("c_email").send_keys("admin@qntm.loc")
Password = driver.find_element_by_id("txt_c_password").send_keys("admin@1234")
OnPremIPAddress = driver.find_element_by_id("txt_c_URL").clear()
driver.find_element_by_id("txt_c_URL").send_keys("10.20.0.216")

time.sleep(1)

MProceed = driver.find_element_by_id("btnOpModenext").click()

time.sleep(7)

SiteSelection = driver.find_element_by_id("dropdwnSiteName")
drp = Select(SiteSelection)

time.sleep(2)

drp.select_by_visible_text('SeleniumPython')

time.sleep(1)

GroupSelection = driver.find_element_by_id("ddl_cc_site_ap_group")
drp = Select(GroupSelection)

time.sleep(2)

drp.select_by_visible_text('NewGroup')

time.sleep(1)

RProceed = driver.find_element_by_id("btnCloudSiteSetupNext").click()

time.sleep(3)

RModeSelection = driver.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[15]/div[1]/div/label[2]").click()

time.sleep(1)

OProceed = driver.find_element_by_id("btnMasterAPnext").click()

time.sleep(1)

Wlan = driver.find_element_by_id("txt_c_wlan").send_keys("scenario89")
Sssid = driver.find_element_by_id("txt_c_ssid").send_keys("scenario89")
Key = driver.find_element_by_id("txt_c_wlankey").send_keys("12345678")
ipaddress = driver.find_element_by_id("txtCloudLSIP").send_keys("192.168.1.1")
Subnet = driver.find_element_by_id("txtCloudLSMask").send_keys("255.255.255.0")

time.sleep(1)

CSummary = driver.find_element_by_id("btnCloudSSIDnext").click()

time.sleep(5)

FProceed = driver.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[18]/div[2]/div/span[2]")
driver.execute_script("arguments[0].click();", FProceed)

print("AP On-Boarded Successfully")