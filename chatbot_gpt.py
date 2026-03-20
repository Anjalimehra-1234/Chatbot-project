import random

# Predefined responses
responses = {
    "hello": ["Hi!", "Hello!", "Hey!"],
    "hi": ["Hi there!", "Hello!"],
    "how are you": ["I'm fine!", "Doing great!", "All good!"],
    "what is ai": ["AI means Artificial Intelligence."],
    "bye": ["Goodbye!", "See you!", "Bye!"]
}

def chatbot(user_input):
    user_input = user_input.lower()

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return "Sorry, I don't understand."

# Main loop
print("🤖 Simple Chatbot (type 'bye' to exit)\n")

while True:
    user = input("You: ")

    if user.lower() == "bye":
        print("Chatbot: Goodbye!")
        break

    reply = chatbot(user)
    print("Chatbot:", reply)