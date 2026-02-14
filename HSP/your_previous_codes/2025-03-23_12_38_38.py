

import os

while True:
    with open("NEW_CODE.py","a") as f:
        a = input("query: ").lower()
        a = a.replace(".","")
        r = '"'
        red = f'''if r=="{a}":
            answer = [{r}{input("answer: ")}{r}]
            answer = choice(answer)
            hotkey("alt","tab")
            sleep(1)
            click(693,1027)
            sleep(1)
            typewrite(answer)
        '''
        f.writelines(red)