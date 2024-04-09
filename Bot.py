import json
import random

# Load responses from file or initialize an empty dictionary
try:
    with open("Response.json", "r") as file:
        responses = json.load(file)
except FileNotFoundError:
    responses = {}

# Main loop for chat
while True:
    # Get user input
    user_input = input("You: ").lower()  # Convert to lowercase

    # Exit the loop if user types 'exit' or 'bye'
    if user_input in ["exit", "bye"]:
        print("Bot: Goodbye! Have a great Day")
        break

    # Check if the user input is in the responses dictionary
    if user_input in responses:
        bot_response = random.choice(responses[user_input])
    else:
        # If the input is not in the responses dictionary, ask the user to teach the bot
        print("Bot: I'm sorry, I don't know how to respond to that.")
        print(
            "Bot: Please teach me! What should I say when you say '{}'?".format(
                user_input
            )
        )
        response_to_learn = input("You: ")
        responses[user_input] = [
            response_to_learn
        ]  # Add the new response to the dictionary
        bot_response = "Got it! I'll remember that."

    # Print bot response
    print("Bot:", bot_response)

# Save responses to file before exiting
with open("Response.json", "w") as file:
    json.dump(responses, file)
