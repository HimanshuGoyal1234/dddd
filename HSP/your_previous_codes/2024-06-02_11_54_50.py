from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service("G:\\FREEEEEEEE\\Driver\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.keybr.com") 
sleep(40)
element = driver.find_element(By.XPATH, "/html/body/main/section/div[2]/div")
element.send_keys("hello")
sleep(100)