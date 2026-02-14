
file_path = "G:\\MYJARVIS\\695ed5cb-29ce-47c0-b698-901e35052268.txt"
with open(file_path, "r") as f:
    lines = len(f.readlines())
r = "},"
p = "{"
# Step 3: Append specific data to the file
with open(file_path,"r") as f:
    with open("fff.txt", "a") as fsd:
        for i in range(lines):
            poi = f.readline()
            poi = poi.split(",")
            title = poi[5].strip()
            year = poi[10].strip()
            time = f"{poi[9].strip()} min"
            rating = poi[8].strip()
            data = {f'{p}"title": {title},"year": "{year}","time": "{time}","rating": "{rating}"{r}\n'}
            fsd.writelines(data)