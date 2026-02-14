from random import randint
with open("study.txt", "r") as f:
        read = len(f.readlines())
r = 0
for i in range(10):
    with open("study.txt", "r") as f:
        for i in range(randint(0,read-1)):
            line = f.readline()
            try:
                line = line.split("=")
                dimension_name = line[0].strip()  # Get the dimension name
                dimension_value = line[1].strip()  # Get the dimension value
                if "-1" in dimension_value:
                    pass
                elif "1" in dimension_value:
                    dimension_value = dimension_value.replace("1","")
                print(f"What are the dimensions of {dimension_name}?")
                user_input = input("")
                cleaned_value = dimension_value.replace("[", "").replace("]", "").replace(" ", "")
                if user_input == cleaned_value:
                    print("Correct!")
                    r = r + 1
                else:
                    print("Incorrect!")
                    print(f"The corret Answer is {dimension_value}")
                    r = r - 1
            except:pass
print(f"your numbers are {r}\nPercentage {int(r) / 10*100}")