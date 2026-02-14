import os
path = input()
if os.path.isdir(path):
    print("folder is deleted,sir")
    os.removedirs(path)
elif os.path.isfile(path):
    print("file is deleted,sir")
    os.remove(path)