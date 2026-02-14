from pyautogui import *

red = [
    "boxville",
    "benson",
    "mesa",
    "rcgoblin",
    "hotrinb",
    "bloodra",
    "bloodrb",
    "vicechee",
]
keyDown("alt")
press("tab")
keyUp("alt")
for i in range(97):
    press("f2")
    typewrite(f"{red[i]}")
    press("enter")
    sleep(0.5)
    keyDown("ctrl")
    press("e")
    keyUp("ctrl")
    sleep(0.5)
    press("enter")
    sleep(0.5)
    press("f3")
    keyDown("ctrl")
    press("e")
    keyUp("ctrl")
    sleep(0.5)
    press("enter")