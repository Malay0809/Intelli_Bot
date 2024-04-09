import json
import random

# File path for storing responses
RESPONSES_FILE = "Response.json"


# Load responses from JSON file
def load_responses():
    try:
        with open(RESPONSES_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


# Save responses to JSON file
def save_responses(responses):
    with open(RESPONSES_FILE, "w") as file:
        json.dump(responses, file, indent=4)


# Main loop for chat
def main():
    # Load responses from JSON file
    responses = load_responses()

    while True:
        # Get user input
        user_input = input("You: ").lower()  # Convert to lowercase

        # Exit the loop if user types 'exit' or 'bye'
        if user_input in ["exit", "bye"]:
            print("Bot: Goodbye!")
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

        # Save responses to JSON file
        save_responses(responses)

        # Print bot response
        print("Bot:", bot_response)


if __name__ == "__main__":
    main()
