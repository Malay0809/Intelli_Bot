import webbrowser
import subprocess
import os
import requests
import ast


def search_meaning(word):

    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        pass_ = 0
        meanings = response.json()
        meanings = str(meanings)
        try:
            data_list = ast.literal_eval(meanings)
            definitions = data_list[0]["meanings"][0]["definitions"]

            pass_ = 1
        except Exception as e:
            print(e)
            return ["No definition found."]

        if pass_ == 1:

            meanings = {item["definition"] for item in definitions}
            print(meanings)
            return list(meanings)
        else:
            return ["No definition found."]
    else:
        return ["Failed to retrieve meaning."]


while True:
    # Get user input
    user_input = input("You: ").lower()
    if user_input == "open youtube":
        webbrowser.open("https://www.youtube.com/")
        print("Bot: Opened youtube")
    elif user_input == "open notepad":
        subprocess.Popen(["notepad.exe"])
        # os.system("start notepad.exe")
        print("Bot:  Opened Notepad")
    elif user_input == "bye":
        print("Bot: Byee")
        exit()
    elif user_input == "open chrome":
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get("chrome").open_new_tab("https://www.google.com")
        print("Bot: Opened Chrome")
    elif user_input.startswith("mean "):
        word_to_search = user_input.split(" ", 1)[1]  # Extract the word to search
        print("Bot: Seraching For ", str(word_to_search))
        meanings = search_meaning(word_to_search)
        print("Bot: Here is list of Defination I found", str(meanings))
        # bot_response = "\n".join(meanings)
    elif user_input == "Todays Date":
        print("Bot: Todays Date is", datetime.now().strftime("%Y-%m-%d"))
    else:
        print("Bot: I don't know how to do that yet")
