import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

# import elementn
# from telnetlib import EC


driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

mywait = WebDriverWait(driver, 20)

driver.get("http://169.254.1.1")

time.sleep(3)

driver.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[3]/div[2]/a/span[2]").click()

time.sleep(3)

driver.find_element_by_id("btnIPConfigNext").click()

time.sleep(3)

driver.find_element_by_name("c_email").send_keys("hemang4it2@gmail.com")
driver.find_element_by_id("txt_c_password").send_keys("P@$$w0rd")
driver.find_element_by_id("btnOpModenext").click()

time.sleep(7)

element = driver.find_element_by_id("dropdwnSiteName")
drp = Select(element)

time.sleep(2)

drp.select_by_visible_text('Mayur')

time.sleep(2)

driver.find_element_by_id("btnCloudSiteSetupNext").click()

time.sleep(3)

driver.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[15]/div[1]/div/label[2]").click()

time.sleep(1)

driver.find_element_by_id("btnMasterAPnext").click()

time.sleep(1)

driver.find_element_by_id("txt_c_wlan").send_keys("scenario151")
driver.find_element_by_id("txt_c_ssid").send_keys("scenario151")
driver.find_element_by_id("txt_c_wlankey").send_keys("12345678")
driver.find_element_by_id("txtCloudLSIP").send_keys("192.168.1.1")
driver.find_element_by_id("txtCloudLSMask").send_keys("255.255.255.0")

time.sleep(1)

driver.find_element_by_id("btnCloudSSIDnext").click()
time.sleep(5)

element = driver.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[18]/div[2]/div/span[2]")
driver.execute_script("arguments[0].click();", element)

#button = mywait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div/div[2]/div[18]/div[2]/div/span[2]')))

#button.click()

#driver.find_element_by_id("btnFinishconfigure").click()

#time.sleep(17)

#driver.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[18]/div[2]/div/span[2]").click()

#wait = WebDriverWait(driver, 30)
#configure = wait.until(element_to_be_clickable((By.ID, 'btnFinishconfigure')))
#driver.implicitly_wait(20)
#driver.find_element_by_id("btnFinishconfigure")
#element = WebDriverWait(driver, 20).until(

# EC.presence_of_element_located((By.ID, "btnFinishconfigure")))
#element.click()


#last.click()

#WebDriverWait wt = new WebDriverWait(driver, 10)

#driver.find_element_by_id("btnFinishconfigure").click()

#driver.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[18]/div[2]/div/span[2]").click()

print("AP On-Boarded Successfully")