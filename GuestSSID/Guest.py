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

# Guest Selection & creation of Splash Portal

GuestSelect = driver.find_element_by_xpath("//li[@id='LISiteUserPanel']//a[@href='#']").click()
SplashPortalSelect = driver.find_element_by_xpath("//span[normalize-space()='Splash Portal']").click()
AddButton = driver.find_element_by_css_selector(".btn.btn-success.btn-sm.hedicon").click()
NameField = driver.find_element_by_id("Name").send_keys("test")
DescriptionField = driver.find_element_by_id("description").send_keys("ForTestPurpose")
WebPortalLogoEnable = driver.find_element_by_css_selector("#divms > div:nth-child(1) > div.col-lg-4.col-sm-3.col-xs-10 > div > span").click()
WebPortalTitle = driver.find_element_by_id("PortalTitle").send_keys("Login")
SSubmit = driver.find_element_by_id("btnGuestProfile")
driver.execute_script("arguments[0].click();", SSubmit)

# Guest Profile

GuestClick = driver.find_element_by_xpath("//li[@id='LISiteUserPanel']//a[@href='#']").click()
GuestProfileSelect = driver.find_element_by_css_selector("body > div:nth-child(2) > aside:nth-child(2) > section:nth-child(1) > ul:nth-child(2) > li:nth-child(9) > ul:nth-child(2) > li:nth-child(3) > a:nth-child(1) > span:nth-child(2)")
driver.execute_script("arguments[0].click();", GuestProfileSelect)

time.sleep(4)
GAddButton = driver.find_element_by_css_selector("body > div.wrapper > div > section > div:nth-child(1) > div.panel-heading.panelhed > div > div:nth-child(2) > a").click()
ProfileName = driver.find_element_by_xpath("/html/body/div[2]/div/section/form/div/div/div/div/fieldset/div[1]/div/input").send_keys("GuestProfile")
UseTime = driver.find_element_by_id("PassValidFor").send_keys("10")
DaySelect = driver.find_element_by_id("PassValidUnit")
drp = Select(DaySelect)
drp.select_by_visible_text('Days')
ExpiryGuestPass = driver.find_element_by_id("PassExpiryDays").send_keys("10")
GSubmit = driver.find_element_by_id("btnGuestProfile")
driver.execute_script("arguments[0].click();", GSubmit)

# Guest Pass

time.sleep(5)
#GPClick = driver.find_element_by_xpath("//li[@id='LISiteUserPanel']//a[@href='#']")
#driver.execute_script("arguments[0].click();", GPClick)
GuestPassSelect = driver.find_element_by_css_selector("#LISiteGuestPass > a > span").click()
GenerateButton = driver.find_element_by_xpath("/html/body/div[2]/div/section/div/div[1]/div/div/div[3]/a").click()
PassType = driver.find_element_by_xpath("/html/body/div[2]/div/section/form/div/div/div/div/fieldset/div[1]/div/label[2]/input").click()
NumberofPasses = driver.find_element_by_name("PassesNo").send_keys("8")
GuestPolicyProfile = driver.find_element_by_id("gpPlanProfile")
drp = Select(GuestPolicyProfile)
drp.select_by_visible_text('GuestProfile')
GPSubmit = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/section[1]/form[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[9]/div[1]/input[1]")
driver.execute_script("arguments[0].click();", GPSubmit)

# WLAN Creation

Wireless = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/aside[1]/section[1]/ul[1]/li[4]/a[1]/span[1]").click()
WLAN = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/aside[1]/section[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]/i[1]").click()
WADD = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]").click()
WlanName = driver.find_element_by_id("DisplayWLANname").send_keys("guest470")
SSID = driver.find_element_by_id("SSID").send_keys("guest470")
AccessType = driver.find_element_by_id("Network_Type")
drp = Select(AccessType)
drp.select_by_visible_text('GuestAccess')
SplashPortalProfile = driver.find_element_by_id("GuestPanelID")
drp = Select(SplashPortalProfile)
drp.select_by_visible_text('test')
GuestPolicy = driver.find_element_by_id("GuestPolicyID")
drp = Select(GuestPolicy)
drp.select_by_visible_text('GuestProfile')
NASOption = driver.find_element_by_id("NASOption")
drp = Select(NASOption)
drp.select_by_visible_text('Default')
Key = driver.find_element_by_name("EncryptionKey").send_keys("12345678")
VLAN = driver.find_element_by_id("VLAN_ID").send_keys("1")
APGroup = driver.find_element_by_id("1APGroup").click()
WSubmit = driver.find_element_by_xpath("/html/body/div[2]/div/section/form/div[1]/div/div/div/fieldset/div[60]/div/input")
driver.execute_script("arguments[0].click();", WSubmit)

# End of Guest Profile