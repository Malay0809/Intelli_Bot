import webbrowser
import subprocess
import os
import requests
import ast
import json

# """
# Imports the `webbrowser` module to open web pages in the user's default browser.
# Imports the `subprocess` module to execute external commands.
# Imports the `os` module to interact with the operating system.
# Imports the `requests` module to make HTTP requests.
# Imports the `ast` module to parse and manipulate Python abstract syntax trees.
# """
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

def CalenderApI(Type):
    BASE_URL = "http://localhost:5000"

    if Type == "date":
        endpoint="/current_date"
    elif Type == "day":
        endpoint="/current_day"
    elif Type == "time":
        endpoint="/current_time"
    response = requests.get(BASE_URL+endpoint)
    if response.status_code == 200:
        data=response.json()
        return data
    else:
        return "Failed to retrieve date"

RESPONSES_FILE = "Response.json"
def load_responses():      # Load responses from JSON file
    try:
        with open(RESPONSES_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Failed to load response Data.")
        return {}

def save_responses(responses):     # Save responses to JSON file
    try:
        with open(RESPONSES_FILE, "w") as file:
            json.dump(responses, file, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Failed to save responses.")
        return {}


if __name__ == "__main__":
    print("Module is being run directly")
