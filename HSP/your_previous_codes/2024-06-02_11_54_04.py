from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Initialize the Chrome WebDriver
s = Service("G:\\FREEEEEEEE\\Driver\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
# Navigate to the webpage
driver.get("https://you.com/?chatMode=default")
# Execute JavaScript code
sleep(15)
script = 'document.getElementById("search-input-textarea").value = "red";'
driver.execute_script(script)
sleep(100)
