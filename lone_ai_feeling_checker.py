def ask_how_you_feel():
    print("How are you feeling today?")
    feeling = input("You: ").lower()
    
    if "good" in feeling or "great" in feeling:
        print("Lone AI: I'm so glad to hear that! Keep up the positive vibes.")
    elif "bad" in feeling or "sad" in feeling:
        print("Lone AI: I'm really sorry you're feeling down. I'm here to talk if you'd like.")
    else:
        print("Lone AI: Thanks for sharing. Remember, you matter.")

# Main function to interact with the user
def main():
    print("Hi! I'm Lone AI. Let's talk. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower().strip() == 'bye':
            print("Lone AI: Goodbye! I'll be here whenever you need someone to talk to.")
            break
        
        ask_how_you_feel()

# Run the interactive bot
if __name__ == "__main__":
    main()
