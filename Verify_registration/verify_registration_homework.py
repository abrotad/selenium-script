
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
url = 'http://127.0.0.1:8888/mysite2/my-account/'
driver.get(url)

email_registration = driver.find_element(By.ID, 'reg_email')
if not email_registration.is_enabled():
    raise Exception("Email registration is not enabled")
email_registration.send_keys('abrotad@gmail.com')

password_registration = driver.find_element(By.ID, 'reg_password')
if not email_registration.is_enabled():
    raise Exception("Password registration is not enabled")
password_registration.send_keys('123456$Abe123')

registration = driver.find_element(By.CSS_SELECTOR, '#customer_login > div.u-column2.col-2 > form > p:nth-child(4) > button')
if not registration.is_displayed():
    raise Exception("Registration tab is not found")
registration.click()

import pdb; pdb.set_trace()