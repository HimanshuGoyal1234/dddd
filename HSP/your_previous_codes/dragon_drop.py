import os


from all_important_functions import alpha
def delete():
    path = input("PATH: ")
    if "& '" in path:
        path = path.replace("& ","")
        path = path.replace("'","")
    if os.path.isdir(path):
        os.removedirs(path)
        alpha("folder is deleted,sir")
    elif os.path.isfile(path):
        os.remove(path)
        alpha("file is deleted,sir")
        