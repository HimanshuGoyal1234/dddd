import importlib
import wikipedia
import requests
from bs4 import BeautifulSoup
import pywhatkit
from all_important_functions import alpha,thinking,_drive_selection_
def google_search(query):
    thinking()
    try:
        url = f"https://www.google.com/search?q={query}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = soup.find_all('div', class_='BNeawe')
        if search_results:
            result = search_results[0].text
            words = result.split()
            last_word = words[-1]
            if last_word == "Wikipedia":
                try:
                    page = wikipedia.page(query)
                    summary_sentences = page.summary.split('.')
                    result = ('. '.join(summary_sentences[:4]) + '.')  # Print only the first three sentences
                    search_result_dlg()
                    alpha(result)
                    return result
                except wikipedia.exceptions.PageError:
                    print("Page not found.")
                    return None
                except wikipedia.exceptions.DisambiguationError as e:
                    print(f"Disambiguation Error: {e}")
                    return None
            elif last_word != "Wikipedia":
                search_result_dlg()
                results = str(result).split(" ")
                results = len(results)
                if results<10:
                    pywhatkit.search(f"{query}")
                else:
                    alpha(result)
                    return "REED"
        else:
            print("No search results found.")
            return None
    except requests.RequestException as e:
        print(f"I'm Sorry Sir There Was an issue in search please check your internet connection")
        return None
    except Exception as e:
        print(f"Error:")
        return None
def save_to_txt(query, result):
    file_path = f"{_drive_selection_()}\\information_of_you\\data.json"
    with open(file_path,"r",encoding="utf-8") as f:
        length = len(f.readlines()) -1
        r = "{"
        rr = "}"
        with open(file_path,"r",encoding="utf-8") as f:
            line_number = len(f.readlines()) -1
        poi = str(result)
        poi = poi.replace('"',"'")
        poi = poi.replace('\n'," ")
        text_to_print = f''',{r}"patterns": ["{query}"],"responses": ["{poi}"]{rr}'''
        if poi=="":
            pass
        else:
            with open(file_path, "r",encoding="utf-8") as file:
                lines = file.readlines()
            lines.insert(line_number - 1, f"{text_to_print}\n")
            with open(file_path, "w",encoding="utf-8") as file:
                file.writelines(lines)
def search_result_dlg():
    import Dialogs.Dialog as Dialog
    importlib.reload(Dialog)
    Dialog.main(Dialog.search_result)
def main():
    try:
        with open(f"{_drive_selection_()}\\important_things\\query.txt","r") as file:  # Use a relative path or environment variable
            _text = file.readline()
            text = _text.split("search on google ")
            query = text[1]
            result = google_search(query)
            if result=="REED":
                pass
            else:
                save_to_txt(query, result)
    except Exception as e:
        print(f"Error: {e}")

# main()