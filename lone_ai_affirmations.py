import random

# List of positive affirmations
affirmations = [
    "I believe in you.",
    "You are enough.",
    "You are worthy of love and happiness.",
    "Every day is a new opportunity.",
    "You are capable of achieving amazing things."
]

# Function to provide a random affirmation
def give_affirmation():
    return random.choice(affirmations)

# Main function to interact with the user
def main():
    print("Hello! Let's start with some positive affirmations. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower().strip() == 'bye':
            print("Lone AI: You are amazing! Take care!")
            break
        
        # Give a random affirmation
        response = give_affirmation()
        print(f"Lone AI: {response}")

# Run the affirmation bot
if __name__ == "__main__":
    main()
