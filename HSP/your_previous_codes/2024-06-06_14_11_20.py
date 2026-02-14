from random import choice
import random
import pyttsx3
from all_important_functions import _drive_selection_
goodbye = [
    f"okay, farewell",
    f"okay, goodbye",
    f"okay, see you later",
    f"okay, until next time",
    f"alright, adieu",
    f"alright, take care",
    f"alright, goodbye for now",
    f"sure, see you around",
    f"sure, until we meet again",
    f"understood, farewell",
    f"understood, bye",
    f"understood, take care",
    f"affirmative, goodbye"]
def alpha(audio):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("rate", 180)
    voice_path = f"{_drive_selection_()}\\important_things\\voice.txt"
    
    with open(voice_path, "r") as file:
        voice = int(file.readline().strip())
    
    engine.setProperty("voice", voices[voice].id)
    
    ere = f"{audio}"
    highlighted_text = highlight_random_word(ere)
    
    print(highlighted_text)  # Print the text with a random word highlighted
    engine.say(ere)  # The TTS will say the original text without highlighting
    engine.runAndWait()
def highlight_random_word(text):
    words = text.split()
    if not words:
        return text
    random_word_index = random.randint(0, len(words) - 1)
    words[random_word_index] = f"{RED}{words[random_word_index]}{RESET}"
    return " ".join(words)
RED = "\033[38;2;255;0;0m"
RESET = "\033[0m"
print("hello how are you")
alpha("hello how are you")
# rr = choice(a)