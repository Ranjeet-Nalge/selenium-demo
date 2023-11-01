from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

my_service =Service(executable_path='C:\\Users\\admin\\Downloads\\Compressed\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=my_service)
driver.maximize_window()
driver.get('https://www.orangehrm.com/')
# driver.get('https://www.google.com/')

find = driver.find_element(By.ID,'Form_submitForm_EmailHomePage')
find.send_keys('python123@gmail.com')
time.sleep(10)
find.find_element(By.NAME,'action_request')
find.click()

time.sleep(15)