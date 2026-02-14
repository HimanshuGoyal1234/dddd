with open("ddd.txt","r",encoding="utf-8") as f:
    length = len(f.readlines())

with open("ddd.txt","r",encoding="utf-8") as f:
    for i in range(length):
        rr = f.readline()
        poi = rr.split(":")
        r = poi[0]
        r = r.replace(",","")
        r = r.replace(".","")
        r = r.replace('"',"")
        r = r.replace('?',"")
        print(r)
        with open("fff.txt","a",encoding="utf-8") as red:
            red.writelines(f"{r}:{poi[1]}")