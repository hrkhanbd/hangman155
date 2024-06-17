import random

def create_word_list():
    """Create a list of favorite fruits."""
    return ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

def select_random_word(word_list):
    """Select a random word from the given list."""
    return random.choice(word_list).lower()  # Convert to lower case for case insensitive comparison

def check_guess(guess, secret_word):
    """Check if the guessed letter is in the secret word."""
    guess = guess.lower()
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_input(secret_word):
    """Prompt the user to enter a single letter and validate the input."""
    while True:
        guess = input("Enter a single letter: ").lower()  # Convert to lower case for case insensitive comparison
        if len(guess) == 1 and guess.isalpha():
            check_guess(guess, secret_word)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

def main():
    """Main function to run the Hangman game."""
    print("Welcome to Hangman!")
    
    # Create a list of words and select a random word
    word_list = create_word_list()
    secret_word = select_random_word(word_list)
    
    print("A secret word has been chosen (for testing purposes):", secret_word)
    
    # Ask for user input and check the guess
    ask_for_input(secret_word)

if __name__ == "__main__":
    main()


