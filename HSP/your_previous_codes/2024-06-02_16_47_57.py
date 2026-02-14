from time import sleep


with open("ddd.txt","r",encoding="utf-8") as f:
    length = len(f.readlines())

# with open("ddd.txt","r",encoding="utf-8") as f:
#     for i in range(length):
#         rr = f.readline()
#         poi = rr.split(":")
#         r = poi[0]
#         r = r.replace(",","")
#         r = r.replace(".","")
#         r = r.replace('"',"")
#         r = r.replace('?',"")
#         print(r)
        # with open("fff.txt","a",encoding="utf-8") as red:
        #     red.writelines(f"{r}:{poi[1]}")

with open("ddd.txt","r",encoding="utf-8") as f:
    for i in range(length):
        rr = f.readline()
        rr = f.readline()
        poi = rr.split("          ")
        r = poi[0].lower()
        rrrr = poi[1]
        r = r.replace(",","")
        r = r.replace(".","")
        r = r.replace('"',"")
        r = r.replace('?',"")
        print(r)
        print("")
        print(rrrr)
        with open("sds.txt","r") as slkdjf:
            royal = slkdjf.readline()
        if r==royal:
            pass
        elif r!=royal:
            with open("fff.txt","a",encoding="utf-8") as red:
                red.writelines(f"{r}:{poi[1]}")
        with open("sds.txt","w") as sslkjslkfj:
            sslkjslkfj.writelines(f"{r}")
            sslkjslkfj.close()