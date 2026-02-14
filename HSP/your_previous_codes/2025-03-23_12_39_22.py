from random import choice
from time import sleep
from pyautogui import hotkey, typewrite,click
from pyperclip import paste,copy
from all_important_functions import _drive_selection_
with open(f"{_drive_selection_()}\\temp\\temp2.txt","r",encoding="utf-8") as file:
    length = len(file.readlines())
    with open(f"{_drive_selection_()}\\temp\\temp2.txt","r",encoding="utf-8") as file:
        r = file.readline().lower()
        red = r.split(" ")
        r = r.replace(".","")
        print(r)
        if r=="hello" or r in ["hi","hey","oye","hello","kaise ho"] and len(red)<3:
            answer = ["Hii...","Hello...", "Hey...", "Hi there!", "Hello! How can I help you?", "Hey! What's up?"]
            answer = choice(answer)
            hotkey("alt","tab")
            sleep(1)
            click(693,1027)
            sleep(1)
            typewrite(answer)
        if r=="mujhe ek baat batao":
            answer = ["haan ji pochiye,"]
            answer = choice(answer)
            hotkey("alt","tab")
            sleep(1)
            click(693,1027)
            sleep(1)
            typewrite(answer)
        if r=="hm i love you" or r=="i love you":
            answer = ["I LOVE YOU TOOO MUMMA"]
            answer = choice(answer)
            hotkey("alt","tab")
            sleep(1)
            click(693,1027)
            sleep(1)
            typewrite(answer)
        