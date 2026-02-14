import os
from time import sleep
import pyautogui

def take_screen_shot():
    x, y, width, height = 590, 169, 1330, 870
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save("G:\\MY_AI\\MY_AI\\temp\\cropped_area.png")
sleep(2)
take_screen_shot()