import os
e = input()
r = "}"
re = "{"
red = e.lower()
e = e.replace(" ","_")
with open(f"G:\\MYJARVIS\\study_material\\{e}.txt","a") as f:
    f.write("\n\n\n")
with open("G:\\MYJARVIS\\function\\study_material.py","a") as f:
    f.writelines(f'''elif ep=="{red}":
        a = open(f"{re}_drive_selection_(){r}\\\\study_material\\\\{e}.txt","r")
        rra = len(a.readlines())
        a = open(f"{re}_drive_selection_(){r}\\\\study_material\\\\{e}.txt","r")
        for i in range(rra):
            print(a.readline(),end="")
    ''')
os.system(f"code G:\\MYJARVIS\\study_material\\{e}.txt")
