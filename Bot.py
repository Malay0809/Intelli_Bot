import json
import random
import Methods_Module as T
import webbrowser
import subprocess
import os
import requests
import ast

# Load responses from file or initialize an empty dictionary

responses = T.load_responses()

# Main loop for chat
while True:
    # Get user input
    user_input = input("You: ").lower()  # Convert to lowercase

    if user_input in ["exit", "bye"]:
        print("Intelli_Bot: Goodbye! Have a great Day")
        exit()
    elif user_input == "open youtube":
        webbrowser.open("https://www.youtube.com/")
        print("Intelli_Bot: Opened youtube")
    elif user_input == "open notepad":
        subprocess.Popen(["notepad.exe"])
                                                                            # os.system("start notepad.exe")
        print("Intelli_Bot:  Opened Notepad")
    elif user_input == "open chrome":
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe" 
        webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get("chrome").open_new_tab("https://www.google.com")
        print("Intelli_Bot: Opened Chrome")
    elif user_input.startswith("mean "):
        word_to_search = user_input.split(" ", 1)[1]                 # Extract the word to search
        print("Intelli_Bot: Seraching For ", str(word_to_search))
        meanings = T.search_meaning(word_to_search)
        print("Intelli_Bot: Here is list of Defination I found", str(meanings))
        # bot_response = "\n".join(meanings)
    elif user_input == "date":
        date= str("date")
        print("Intelli_Bot: Todays Date is",T.CalenderApI(date))
    elif user_input == "time":
        time= str("time")
        print("Intelli_Bot: Current time is",T.CalenderApI(time))
    elif user_input == "day":
        day= str("day")
        print("Intelli_Bot: Today is",T.CalenderApI(day))
    elif user_input in responses:
        bot_response = (responses[user_input])
        print("Intelli_Bot:", bot_response)
    
    else:
                                                                    # If the input is not in the responses dictionary, ask the user to teach the bot
        print("Intelli_Bot: I'm sorry, I don't know how to respond to that.")
        print(
            "Intelli_Bot: Please teach me! What should I say when you say '{}'?".format(
                user_input
            )
        )
        response_to_learn = input("You: ")
        responses[user_input] = [response_to_learn]                                                   # Add the new response to the dictionary
        bot_response = "Got it! I'll remember that."
        T.save_responses(responses)

        
        print("Intelli_Bot:", bot_response)

