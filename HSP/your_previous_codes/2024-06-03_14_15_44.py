from all_important_functions import _drive_selection_
import json
import random
import re
from all_important_functions import alpha
file_path = "G:\\MYJARVIS\\cleaned_chatbot_intents.json"
class Chatbot:
    def __init__(self, config_file):
        self.config_file = config_file
        self.load_intents()
    def load_intents(self):
        with open(self.config_file, "r") as file:
            self.intents = json.load(file)["intents"]
    def get_response(self, user_input):
        user_input = user_input.lower()
        for intent in self.intents:
            for pattern in intent["patterns"]:
                if re.search(r"\b" + re.escape(pattern.lower()) + r"\b", user_input):
                    return random.choice(intent["responses"])
        return False
while True:
    bot = Chatbot(file_path)
    ep = open(f"{_drive_selection_()}\\important_things\\query.txt","r")
    user_input = ep.readline()
    user_input = input()
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
    response = bot.get_response(user_input)
    if response==False:
        with open(file_path,"r") as f:
            length = len(f.readlines()) -1
        r = "{"
        rr = "}"
        with open(file_path,"r") as f:
            line_number = len(f.readlines()) -1
        poi = input()
        text_to_print = f',{r}"patterns": ["{user_input}"],"responses": ["{poi}"]{rr}'
        if poi=="":
            pass
        else:
            with open(file_path, "r") as file:
                lines = file.readlines()
            lines.insert(line_number - 1, f"{text_to_print}\n")
            with open(file_path, "w") as file:
                file.writelines(lines)
    if response!=False:
        alpha(f"{response}")
        pass