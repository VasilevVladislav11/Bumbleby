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
#sidebar
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[1]/div/div[2]").click()
time.sleep(1)
#open "Study"
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[1]/div/div[2]/ul/li[2]/a/div[2]").click()
time.sleep(1)
#Open Chat
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/section/div[2]/div[2]").click()
time.sleep(1)
#Print message
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/section/div[2]/div[1]/div/div[3]/input").send_keys("Где админка?")
#Send message
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/section/div[2]/div[2]").click()
