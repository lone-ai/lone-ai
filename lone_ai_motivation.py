import random

# List of motivational quotes
quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Don't watch the clock; do what it does. Keep going. – Sam Levenson",
    "You are never too old to set another goal or to dream a new dream. – C.S. Lewis",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill"
]

# Function to provide a random motivational quote
def give_quote():
    return random.choice(quotes)

# Main function to interact with the user
def main():
    print("Welcome to Lone AI! Type 'bye' to exit and get inspired.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower().strip() == 'bye':
            print("Lone AI: Keep pushing forward! Goodbye!")
            break
        
        # Give a random motivational quote
        response = give_quote()
        print(f"Lone AI: {response}")

# Run the motivational quote bot
if __name__ == "__main__":
    main()
