# input_ = input()
# input_ = input_.split(" ")
# number = 0
# with open("red","r") as f:
#     length = len(f.readlines())
# with open("red","r") as f:
#     for i in range(length):
#         red = f.readline()
#         if red==input_:
#             print(red)
#         else:
#             a = input("answer: ")
#             with open("red","r") as f:
#                 length = len(f.readlines())
#                 for i in range(length):
#                     with open("red","a") as f:
#                         f.writelines(f"{input_}::{a}\n")
a = input("YOU: ")
with open("red.txt","r") as f:
    length = len(f.readlines())
with open("red.txt","r") as f:
    for i in range(length):
        red = f.readline()
        red = red.split("::")
        start = red[0]
        end = red[1]
        if a==start:
            print(f"AI: {end}")
        else:
            with open("red.txt","a") as sfsdf:
                print("I don't know you tell me")
                b= input("")
                sfsdf.writelines(f"{a}::{b}\n")