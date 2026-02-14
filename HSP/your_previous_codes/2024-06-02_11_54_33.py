from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service("G:\\FREEEEEEEE\\Driver\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://chatgpt.com/")
sleep(15)
element = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div[1]/div[2]/div[1]/div/form/div/div[2]/div/textarea")
sleep(10000)