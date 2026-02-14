

import json


def generate_data(intents):
    data = {"intents": []}
    for intent in intents:
        data["intents"].append(
            {"patterns": intent["patterns"], "responses": intent["responses"]}
        )
    return data


intents = [
    {"patterns": [], "responses": []},
]
file_path = "f.json"
generated_data = generate_data(intents)

try:
    with open(file_path, "r") as file:
        existing_data = json.load(file)
except FileNotFoundError:
    existing_data = {}

# Merge the generated data with the existing data
existing_data["intents"] += generated_data["intents"]

# Write the merged data back to the file
with open(file_path, "w") as file:
    json.dump(existing_data, file, indent=4)
