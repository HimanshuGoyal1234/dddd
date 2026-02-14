
import json
import re
def clean_text(text):
    return re.sub(r'[^\w\s]', '', text).lower()
def process_json(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)
    for intent in data["intents"]:
        intent["patterns"] = [clean_text(pattern) for pattern in intent["patterns"]]
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)
process_json('df.json', 'cleaned_chatbot_intents.json')