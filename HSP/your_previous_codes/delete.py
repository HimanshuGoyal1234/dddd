import os
import random

er = open("data.txt","r")
red = er.readline()
i = 0
while True:
    song = os.listdir(red)
    random_= random.choice(song)
    print(random_)
    last_svg = random_[-3:]
    if last_svg=="svg":
        i = 0
        os.remove(f"{red}\\{random_}")
    last__ = random_[-1:]
    if last__==")":
        i = 0
        os.remove(f"{red}\\{random_}")
    last_webp = random_[-4:]
    if last_webp=="webp":
        i = 0
        os.remove(f"{red}\\{random_}")
    last_jpg = random_[-3:]
    if last_jpg=="jpg":
        i = 0
        os.remove(f"{red}\\{random_}")
    last_png = random_[-3:]
    if last_png=="png":
        i = 0
        os.remove(f"{red}\\{random_}")
    last_download = random_[-8:]
    if last_download=="download":
        i = 0
        os.remove(f"{red}\\{random_}")
    last_css = random_[-3:]
    if last_css=="css":
        i = 0
        os.remove(f"{red}\\{random_}")
    last_html = random_[-4:]
    if last_html=="html":
        i = 0
        os.remove(f"{red}\\{random_}")
    last_th = random_[-2:]
    if last_th=="th":
        i = 0
        os.remove(f"{red}\\{random_}")
    last_odf = random_[:3]
    if last_odf=="ODF":
        i = 0
        os.remove(f"{red}\\{random_}")
    else:
        i += 1
        if i==100:
            print("Not More files Found")
            exit()