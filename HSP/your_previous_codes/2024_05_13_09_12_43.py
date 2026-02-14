import os
import random

from pyautogui import keyDown, keyUp, press, sleep
e = "E:\\New folder\\main"
a = os.listdir(e)
for i in range(100):
    re = random.choice(a)
    os.startfile(f"{e}\\{re}")
    sleep(3)
    keyDown("alt")
    press("f4")
    keyUp("alt")