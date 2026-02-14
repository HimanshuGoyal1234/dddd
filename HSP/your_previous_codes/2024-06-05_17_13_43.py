# IT REMOVE all the dupicate items in the list
li = []
redss = []
for i in range(len(li)):
    if li[i] not in redss:
        redss.append(li[i])
    else:
        pass
print(redss)