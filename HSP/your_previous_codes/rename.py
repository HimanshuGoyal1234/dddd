import os 
import random   
i = 0
er = open("data.txt","r")
e = er.readline()
while True:
    song = os.listdir(e)
    random_= random.choice(song)
    splt = random_[-4:]
    if splt!="jpeg":
        i = 0
        number = random.randint(100000000,999999999)
        os.rename(f"{e}\\{random_}",
                f"{e}\\{number}.jpeg")
        print(number)
        print("done")
    else: 
        i = i + 1
        if i==100:
            print("not found more files")
            exit()