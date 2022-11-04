import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('/Users/vladislav/Test/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get("https://qa.neapro.site/login/")
driver.maximize_window()
#Sign In
driver.find_element(By.XPATH, "//*[@id='__layout']/div/section/div[2]/div/div/div/form/div[1]/div[1]/div/input").send_keys("vladislav.vasilyev94@gmail.com")
driver.find_element(By.XPATH, "//*[@id='__layout']/div/section/div[2]/div/div/div/form/div[1]/div[2]/div/input").send_keys("10101154")
driver.find_element(By.XPATH, "//*[@id='__layout']/div/section/div[2]/div/div/div/form/div[2]/button").click()
time.sleep(3)
#changing of phone number
#sidebar
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[1]/div/div[2]").click()
time.sleep(1)
#account
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[1]/div/div[1]/div[2]/a/div").click()
time.sleep(1)
#security and sign in
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/div/div[2]/ul/li[2]/a").click()
time.sleep(1)
#change number
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div").click()
time.sleep(1)
#clear of input
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/div/div[2]/div/div/div/div[2]/form/div/div/input").clear()
#number entry
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/div/div[2]/div/div/div/div[2]/form/div/div/input").send_keys("1111111111")
time.sleep(1)
#confirm
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/div/div[2]/div/div/div/div[2]/form/button").click()
#close
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/div/div[2]/div/div/div/div[1]/div[2]/img").click()

