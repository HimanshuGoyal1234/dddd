with open("red.txt","a") as f:
    f.write(f'elif "{input()}" or \n')
for i in range(1000):
    with open("red.txt","a") as f:
        f.write(f'"{input()}" or \n')
