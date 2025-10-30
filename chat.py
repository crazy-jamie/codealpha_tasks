


def create_account():
    print("👤 Let's create your chat account!")
    name = input("Enter your name: ").strip().capitalize()
    print(f"\nWelcome, {name}! Your account has been created successfully. \n")
    return name


# Step 2: Chatbot reply logic
def chatbot_reply(message, name):
    message = message.lower()

    if message in ["hi", "hello", "hey"]:
        return f"Hey {name}!  How’s your day going?"

    elif "how are you" in message:
        return f"I’m doing great, {name}! Thanks for asking. What about you?"

    elif "fine" in message or "good" in message:
        return f"That’s wonderful to hear, {name}! "

    elif "your name" in message:
        return "I’m your chat partner — ChatBotX , always ready to talk!"

    elif "help" in message:
        return "Sure! You can greet me, ask how I am, or talk about anything."

    elif "thank" in message:
        return f"Aww, you’re so kind, {name}! "

    elif "bye" in message or "exit" in message or "quit" in message:
        return f"Goodbye {name}! It was nice chatting with you. Take care! "

    else:
        return f"Hmm... I’m not sure I understood that, {name}. Could you say it another way?"


# Step 3: Start the conversation
def start_chat():
    user_name = create_account()  # Create the user account first
    print(f" ChatBotX: Hello {user_name}! I'm ChatBotX — your friendly chatbot.")
    print("You can type 'bye' anytime to end the chat.\n")

    while True:
        user_input = input(f"{user_name}: ")
        bot_reply = chatbot_reply(user_input, user_name)
        print(" ChatBotX:", bot_reply)

        # End chat if user says bye
        if "bye" in user_input.lower() or "exit" in user_input.lower() or "quit" in user_input.lower():
            break


# Step 4: Run the chatbot
start_chat()

