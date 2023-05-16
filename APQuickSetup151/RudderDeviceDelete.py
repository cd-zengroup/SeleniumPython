import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

# import elementn
# from telnetlib import EC


driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.maximize_window()
driver.implicitly_wait(15)
mywait = WebDriverWait(driver, 20)

driver.get("https://rudder.qntmnet.com/login")

Username = driver.find_element_by_name("email").send_keys("hemang4it2@gmail.com")
Next = driver.find_element_by_id("user_check").click()

time.sleep(1)

Password = driver.find_element_by_name("password").send_keys("P@$$w0rd")
time.sleep(1)
Login = driver.find_element_by_id("passwrd_step").click()

time.sleep(1)

Sites = driver.find_element_by_xpath("/html/body/div[2]/aside/section/ul/li[2]/a/span").click()
time.sleep(1)
SiteName = driver.find_element_by_css_selector("#ajax_list_sites > tbody > tr:nth-child(6) > td:nth-child(2) > a").click()

time.sleep(1)

Wireless = driver.find_element_by_css_selector("#LISiteConfiguration > a").click()
Wlan = driver.find_element_by_css_selector("#LISiteWireless > a > span").click()
Menu = driver.find_element_by_xpath("//i[@class='fas fa-ellipsis-v']").click()
Edit = driver.find_element_by_css_selector(".btn.btn-success.btn-xs.editme.actionBtnmargin").click()

time.sleep(1)

RoutingOption = driver.find_element_by_xpath("//select[@id='RoutingOption']")
drp = Select(RoutingOption)
drp.select_by_visible_text('Bridge To WAN')

time.sleep(1)

Vlan = driver.find_element_by_id("VLAN_ID").clear()
driver.find_element_by_id("VLAN_ID").send_keys("1")

time.sleep(2)

submit = driver.find_element_by_id("btnWireless")
driver.execute_script("arguments[0].click();", submit)

time.sleep(5)

AccessPoint = driver.find_element_by_css_selector("#LISiteAccessPoint > a > span").click()
More = driver.find_element_by_css_selector("a[class='show_action_buttons'] i[class='fas fa-ellipsis-v']").click()
Delete = driver.find_element_by_xpath("//button[@type='button'][normalize-space()='Delete']").click()

time.sleep(1)

ConfirmDialogue = driver.find_element_by_xpath("//button[@class='swal-button swal-button--confirm swal-button--danger']").click()

time.sleep(2)

CloudName = driver.find_element_by_xpath("/html/body/div[2]/header/nav/div[2]/ul/li[5]/a/span").click()
Logout = driver.find_element_by_css_selector("#logout > span").click()

#driver.quit()
#driver.close()

print("Device deleted from cloud")