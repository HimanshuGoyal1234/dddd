from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time

# # Correct path to your ChromeDriver
# s = Service("G:\\MY_AI\\MY_AI\\chromedriver-win32\\chromedriver.exe")
# driver = webdriver.Chrome(service=s)

# # Open Instagram
# driver.get("https://www.instagram.com/")
# username = driver.find_element("xpath", "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[1]/div/label/input")
# username.send_keys("HimanshuDW31")
# print("time1")
# time.sleep(1)

# passowrd = driver.find_element("xpath", "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[2]/div/label/input")
# passowrd.send_keys("Hacker is arise")
# print("time2")
# time.sleep(1)

# login_button = driver.find_element("xpath", "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[3]/button")
# login_button.click()
# print("3")
# time.sleep(10)

# driver.get("https://www.instagram.com/direct/t/17844927699107632/")
# # Click on 'Not Now' after login
# login_buttons = driver.find_element("xpath", "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[5]")
# login_buttons.click()
# print("4")
# time.sleep(10)

# # Click on 'Not Now' for notifications
# login_buttons = driver.find_element("xpath", "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
# login_buttons.click()
# print("5")
# time.sleep(5)


# # Send Message
# message_box = driver.find_element("xpath", "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div/div/div[2]")
# message_box.send_keys("OHHH JI SUNTI HO")
# print("7")

# # Press Enter to Send Message
# message_box.send_keys(Keys.ENTER)
# print("8")
# time.sleep(1000)