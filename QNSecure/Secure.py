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

# QIM Selection

GridButton = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/header[1]/nav[1]/div[2]/ul[1]/li[3]/a[1]/i[1]").click()
QIM = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/header[1]/nav[1]/div[2]/ul[1]/li[3]/ul[1]/li[2]/span[1]/a[1]/img[1]").click()

# Group Creation

Group = driver.find_element_by_css_selector("body > div:nth-child(2) > aside:nth-child(2) > section:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1) > span:nth-child(2)").click()
GAdd = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/div[2]/button[1]/i[1]").click()
GName = driver.find_element_by_name("name").send_keys("Chaitanya")
GRemarks = driver.find_element_by_name("remarks").send_keys("For Selenium")
GSubmit = driver.find_element_by_id("btnSubmitD")
driver.execute_script("arguments[0].click();", GSubmit)

# User Creation

User = driver.find_element_by_css_selector("body > div:nth-child(2) > aside:nth-child(2) > section:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > ul:nth-child(2) > li:nth-child(3) > a:nth-child(1) > span:nth-child(2)").click()
UAdd = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/section[1]/form[1]/div[1]/div[1]/div[1]/div[2]/a[2]").click()
FName = driver.find_element_by_id("first_name").send_keys("Chaitanya")
LName = driver.find_element_by_id("last_name").send_keys("Dixit")
EMail = driver.find_element_by_id("email").send_keys("chaitanya@gmail.com")
PNo = driver.find_element_by_id("contact").send_keys("7845120356")
UGroup = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/section[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/fieldset[1]/div[7]/div[1]/div[1]/button[1]/span[1]")
drp = Select(UGroup)
drp.select_by_visible_text('Chaitanya')
UStatus = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/section[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/fieldset[1]/div[10]/div[1]/div[1]/span[1]").click()
UUsername = driver.find_element_by_id("username").send_keys("admin")
UPassword = driver.find_element_by_id("password").send_keys("admin")
EnableSecure = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/section[1]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/div[1]/fieldset[1]/div[1]/div[1]/div[1]/span[1]").click()
PlusIcon = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/section[1]/div[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]/i[1]").click()
LAdd = driver.find_element_by_id("addLinkDevice").click()
DName = driver.find_element_by_id("DeviceName").send_keys("CD PC")
MAddress = driver.find_element_by_id("MACAddress").send_keys("E4A8DFA3155C")
OS = driver.find_element_by_id("OS")
drp = Select(OS)
drp.select_by_visible_text('Windows')
Securenable = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/fieldset[1]/div[11]/div[1]/div[1]/span[1]").click()
Save = driver.find_element_by_id("add").click()
Savechanges = driver.find_element_by_id("btnQAMUsers").click()

# SSID Creation

RudderPage = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/header[1]/a[1]/span[2]/img[1]").click()
Sites = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/aside[1]/section[1]/ul[1]/li[2]/a[1]/span[1]").click()
SiteSelect = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/section[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[2]/a[1]").click()
Wireless = driver.find_element_by_css_selector("body > div:nth-child(2) > aside:nth-child(2) > section:nth-child(1) > ul:nth-child(2) > li:nth-child(4) > a:nth-child(1) > span:nth-child(2)").click()
WLAN = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/aside[1]/section[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]/span[1]").click()
WAdd = driver.find_element_by_css_selector(".fa.fa-plus").click()
WName = driver.find_element_by_id("DisplayWLANname").send_keys("secure470")
SSID = driver.find_element_by_id("SSID").click()
AccessType = driver.find_element_by_id("Network_Type")
drp = Select(AccessType)
drp.select_by_visible_text('Quantum Secure')

