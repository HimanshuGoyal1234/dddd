re = "C:\\Users\\ABC\\OneDrive\\Desktop\\"
import os
lis = os.listdir(re)
for i in range(34):
    r = lis
    rer = lis[i]
    year = rer[:-14]
    month = rer[4:-12]
    date = rer[6:-10]
    hour = rer[8:-8]
    mins = rer[10:-6]
    sec = rer[12:-4]
    rerr = rer[23:]
    prr = f"[{date},{month},{year}],[{hour},{mins},{sec}]"
    print(prr)
