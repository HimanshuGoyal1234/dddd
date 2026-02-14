import random
from pyautogui import *
import faker

keyDown("alt")
press("tab")
keyUp("alt")


for i in range(109):
    keyDown("shift")
    press("f10")
    keyUp("shift")
    press("m")
    keyDown("ctrl")
    press("a")
    keyUp("ctrl")
    Fkaer = faker.Faker()
    dd = Fkaer.password()
    typewrite(f".jpeg")
    sleep(0.5)
    press("enter")
    sleep(0.5)
    press("enter")
    sleep(0.5)
    press("enter")
    sleep(0.5)
    press("down")
    sleep(0.5)
    press("down")
    sleep(0.5)


keyDown("win")
press("d")

keyUp("win")
