import random

def create_word_list():
    """Create a list of favorite fruits."""
    return ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

def select_random_word(word_list):
    """Select a random word from the given list."""
    return random.choice(word_list)

def get_user_guess():
    """Prompt the user to enter a single letter and return the guess."""
    return input("Enter a single letter: ")

def validate_guess(guess):
    """Validate that the guess is a single alphabetical character."""
    return len(guess) == 1 and guess.isalpha()

def main():
    """Main function to run the Hangman game."""
    # Step 1: Create a list of words
    word_list = create_word_list()
    print("Word list:", word_list)

    # Step 2: Select a random word from the list
    selected_word = select_random_word(word_list)
    print("Selected word (for testing):", selected_word)

    # Step 3: Get user guess
    guess = get_user_guess()

    # Step 4: Validate the guess
    if validate_guess(guess):
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")

if __name__ == "__main__":
    main()




