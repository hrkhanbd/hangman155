import random

def create_fruit_list():
    """Create a list of favorite fruits."""
    return ['apple', 'banana', 'cherry', 'date', 'elderberry']

def select_random_fruit(fruit_list):
    """Select a random fruit from the given list."""
    return random.choice(fruit_list)

def check_guess(guess, secret_fruit):
    """Check if the guessed letter is in the secret fruit."""
    if guess in secret_fruit:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_guess(secret_fruit):
    """Prompt the user to enter a single letter and validate the input."""
    while True:
        guess = input("Enter a single letter: ").lower()  # Convert to lower case for case insensitive comparison
        if is_valid_guess(guess):
            check_guess(guess, secret_fruit)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

def is_valid_guess(guess):
    """Check if the guess is a single alphabetical character."""
    return len(guess) == 1 and guess.isalpha()

def main():
    """Main function to run the Hangman game."""
    print("Welcome to Hangman!")
    
    # Create a list of fruits and select a random fruit
    fruit_list = create_fruit_list()
    secret_fruit = select_random_fruit(fruit_list)
    
    print("A secret word has been chosen (for testing purposes):", secret_fruit)
    
    # Ask for user input and check the guess
    ask_for_guess(secret_fruit)

if __name__ == "__main__":
    main()



