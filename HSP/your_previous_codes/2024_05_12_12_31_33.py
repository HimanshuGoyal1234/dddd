import json

from all_important_functions import _drive_selection_
def save_information_by_me(data):
    file_path = f"{_drive_selection_()}\\information_of_you\\data.json"
    try:
        with open(file_path, "r") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}
    existing_data.update(data)
    with open(file_path, "w") as file:
        json.dump(existing_data, file, indent=4)
def save_information_by_me_main():
    print("what is the question")
    a = input().lower()
    print("what is the answer")
    b = input().lower()
    if a == "":
        a = ""
        b = ""
    if b == "":
        b = ""
        a = ""
    new_data = {
            f"{a}": f"{b}",
    }
    print(f"Question: {a}\nAnswer:{b}")
    save_information_by_me(data=new_data)
    print("done Sir")
while True:
    save_information_by_me_main()