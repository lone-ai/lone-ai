import random

# List of compliments
compliments = [
    "You are amazing just the way you are!",
    "You have a beautiful soul.",
    "You make the world a better place.",
    "You're doing great, don't forget that!",
    "You have so much potential, keep going!"
]

# Function to provide a random compliment
def give_compliment():
    return random.choice(compliments)

# Main function to interact with the user
def main():
    print("Hi there! I'm here to brighten your day. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower().strip() == 'bye':
            print("Lone AI: Take care! You're never alone. Bye!")
            break
        
        # Give a random compliment
        response = give_compliment()
        print(f"Lone AI: {response}")

# Run the compliment bot
if __name__ == "__main__":
    main()
