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

driver.get("http://rudder.dev.qntmnet.com/login")

# LoginPage of Rudder

Username = driver.find_element_by_id("email").send_keys("hemang@zengroup.co.in")
NextButton = driver.find_element_by_id("user_check").click()
Password = driver.find_element_by_name("password").send_keys("P@$$w0rd")
LoginButton = driver.find_element_by_id("passwrd_step").click()

# Site Selection

SiteButton = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/aside[1]/section[1]/ul[1]/li[2]/a[1]").click()
SiteSelect = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/section[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[2]/a[1]").click()

# Creating Hotspot Profile

time.sleep(3)
Profiles = driver.find_element_by_css_selector("body > div:nth-child(2) > aside:nth-child(2) > section:nth-child(1) > ul:nth-child(2) > li:nth-child(8) > a:nth-child(1) > span:nth-child(2)").click()
Hotspot = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/aside[1]/section[1]/ul[1]/li[8]/ul[1]/li[1]/a[1]/span[1]").click()
HAddButton = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]").click()
Name = driver.find_element_by_id("Name").send_keys("HotSpot")
PortalURL = driver.find_element_by_name("LogonURL").send_keys("https://wsmp.zencc.net/subscriber/index")
PortalSecret = driver.find_element_by_name("PortalSecret").send_keys("developer")
CPortalSecret = driver.find_element_by_name("CPortalSecret").send_keys("developer")
HSubmit = driver.find_element_by_id("btnSubmitD")
driver.execute_script("arguments[0].click();", HSubmit)

# Authentication

time.sleep(3)
ASelect = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/aside[1]/section[1]/ul[1]/li[8]/ul[1]/li[2]/a[1]/span[1]")
driver.execute_script("arguments[0].click();", ASelect)
AAdd = driver.find_element_by_css_selector(".btn.btn-success.btn-sm.hedicon").click()
AName = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/section[1]/form[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys("Auth")
AuthenticationMethod = driver.find_element_by_id("AuthenticationMethod")
drp = Select(AuthenticationMethod)
drp.select_by_visible_text('AAA')
ServerIP = driver.find_element_by_id("Address").send_keys("36.255.3.166")
SServerIP = driver.find_element_by_id("S_Address").send_keys("36.255.3.166")
APort = driver.find_element_by_id("AuthPort").send_keys("1812")
SharedSecret = driver.find_element_by_name("SharedSecret").send_keys("BrE@d8Q#BBhot5p0t")
CSharedSecret = driver.find_element_by_name("CSharedSecret").send_keys("BrE@d8Q#BBhot5p0t")
ASIP = driver.find_element_by_id("AcctAddress").send_keys("36.255.3.166")
SASIP = driver.find_element_by_id("AcctS_Address").send_keys("36.255.3.166")
AccPort = driver.find_element_by_id("AcctPort").send_keys("1813")
ASharedSecret = driver.find_element_by_name("AcctSharedSecret").send_keys("BrE@d8Q#BBhot5p0t")
CASharedSecret = driver.find_element_by_name("AcctCSharedSecret").send_keys("BrE@d8Q#BBhot5p0t")
ASubmit = driver.find_element_by_id("btnAuth")
driver.execute_script("arguments[0].click();", ASubmit)

# Wireless

time.sleep(3)
WClick = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/aside[1]/section[1]/ul[1]/li[4]/a[1]/span[1]").click()
WLAN = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/aside[1]/section[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]/span[1]").click()
WADD = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]").click()
WlanName = driver.find_element_by_id("DisplayWLANname").send_keys("Auth470")
SSID = driver.find_element_by_id("SSID").click()
AccessType = driver.find_element_by_id("Network_Type")
drp = Select(AccessType)
drp.select_by_visible_text('Hotspot (WISPr)')
AuthenticationProfile = driver.find_element_by_id("RadiusProfileID")
drp = Select(AuthenticationProfile)
drp.select_by_visible_text('Auth')
HotspotProfile = driver.find_element_by_id("HotspotProfileID")
drp = Select(HotspotProfile)
drp.select_by_visible_text('HotSpot')
Key = driver.find_element_by_name("EncryptionKey").send_keys("12345678")
VLAN = driver.find_element_by_id("VLAN_ID").send_keys("1")
NASID = driver.find_element_by_id("NAS_ID")
drp = Select(NASID)
drp.select_by_visible_text('AP_MAC')
APGroup = driver.find_element_by_id("1APGroup")
driver.execute_script("arguments[0].click();", APGroup)
WSubmit = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/section[1]/form[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[60]/div[1]/input[1]")
driver.execute_script("arguments[0].click();", WSubmit)

# End of Hotspot Profile