
with open("red","a") as f:
    f.writelines(f"elif {input()} in query or ")
while True:
    with open("red","a") as f:
        f.writelines(f" {input()} in query or ")