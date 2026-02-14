import json

with open("ddd.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Opening the output file once, appending processed lines
with open("fff.txt", "w", encoding="utf-8") as f_out:
    for line in lines:
        poi = line.strip().split(",")  # Strip to remove any trailing newlines
        if len(poi) < 7:  # Ensure there are enough elements in the line
            continue
        
        # Extracting data with proper indexing
        title = poi[1].strip()
        year = poi[2].strip()
        year = year.replace("(","")
        year = year.replace(")","")
        time = poi[3].strip()
        rating = poi[4].strip()
        
        # Creating a dictionary for JSON output
        data = {
            "title": title,
            "year": year,
            "time": time,
            "rating": rating
        }
        
        # Converting dictionary to JSON string and appending '},' at the end
        json_string = json.dumps(data) + ","
        
        # Writing the JSON string to the output file
        f_out.write(json_string + "\n")
