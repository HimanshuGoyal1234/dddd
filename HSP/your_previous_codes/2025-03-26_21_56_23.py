from all_important_functions import _drive_selection_, alpha
import datetime
def add_5():
    file_path = f"{_drive_selection_()}\\important_things\\exercise.txt"
    with open(file_path, "r") as f:
        lines = f.readlines()
    exercises_to_update = ["push ups", "plank", "crunches", "hand grip strengther", "triceps"]
    updated_lines = []
    for line in lines:
        updated_line = line.strip()
        for exercise in exercises_to_update:
            if exercise in line:
                parts = line.split("=")
                if len(parts) == 2:
                    value_part = parts[1].strip().split(" ")[0]
                    try:
                        new_value = int(value_part) + 5
                        extra_info = " ".join(parts[1].strip().split(" ")[1:])
                        if extra_info:
                            updated_line = f"{parts[0].strip()} = {new_value} {extra_info}"
                        else:
                            updated_line = f"{parts[0].strip()} = {new_value}"
                    except ValueError:
                        pass
        updated_lines.append(updated_line)
    with open(file_path, "w") as f:
        f.writelines("\n".join(updated_lines))

def main():
    poi = 1
    with open(f"{_drive_selection_()}\\important_things\\last_date_for_exercise.txt", "r") as f:
        e = datetime.datetime.now()
        e = str(e).split(" ")[0]
        read_date = f.readline()
        if read_date!=e:
            alpha("It's time to complete your workout...")
            with open(f"{_drive_selection_()}\\important_things\\exercise.txt", "r") as f:
                re = len(f.readlines())
            with open(f"{_drive_selection_()}\\important_things\\exercise.txt", "r") as f:
                for i in range(re):
                    red = f.readline().strip()
                    print(red)
                    finished = input("Did You Finish? (yes/no): ")
                    if finished.lower() == "" or finished.lower() == "yes":
                        print("CHECKED OFF")
                    if finished.lower() =="remind me later": 
                        poi = 0
                        break
                    else:
                        print("Not Completed")
            if poi==0:
                pass
            else:
                with open(f"{_drive_selection_()}\\important_things\\last_date_for_exercise.txt","w") as f: f.writelines(f"{e}")
                with open(f"{_drive_selection_()}\\important_things\\exercise_update.txt", "r",encoding="utf-8") as f:
                    read = f.readline()
                    if read == "1":
                        with open(f"{_drive_selection_()}\\important_things\\exercise_update.txt", "w") as f:
                            f.writelines("2")
                    elif read == "2":
                        with open(f"{_drive_selection_()}\\important_things\\exercise_update.txt", "w") as f:
                            f.writelines("1")
                            add_5()