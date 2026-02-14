import os
from faker import Faker

fake = Faker()
a = "C:\\Users\\ABC\\OneDrive\\Desktop\\New folder (3)"
read = os.listdir(a)
length = len(read)
for i in range(length):
    random_name = fake.name()
    r = read[i]
    os.rename(f"{a}\\{r}",f"{a}\\{i+1}.mp4")
