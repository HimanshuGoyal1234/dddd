import json
import os
# from time import sleep

from pyautogui import keyDown, keyUp, press
# def save_information_by_me(data):
#     file_path = "data.json"
#     try:
#         with open(file_path, "r") as file:
#             existing_data = json.load(file)
#     except FileNotFoundError:
#         existing_data = {}
#     existing_data.update(data)
#     with open(file_path, "w") as file:
#         json.dump(existing_data, file, indent=4)
# def save_information_by_me_main():
#     a = input().lower()
#     if a == "":
#         a = ""
#     new_data = {
#             f"{a}": f"{hindisong}",
#     }
#     print(f"Question: {a}\nAnswer:{hindisong}")
#     save_information_by_me(data=new_data)
hindisong = "F:\\Songs\\Slow-Reversed"
hindisongs = hindisong
song = os.listdir(hindisong)
red = len(song) - 1 
for i in range(red):
    hindisong = f"{hindisongs}\\{song[i]}"
    os.startfile(hindisong)

    sleep(0.5)
    keyDown("alt")
    press("tab")
    keyUp("alt")
    save_information_by_me_main()
