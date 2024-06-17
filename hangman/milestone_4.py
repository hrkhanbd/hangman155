import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """Initialize the attributes of the Hangman game."""
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        """Check if the guessed letter is in the secret word."""
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            print(f"Sorry, '{guess}' is not in the word. Try again.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")
        print("Current word:", " ".join(self.word_guessed))

    def ask_for_input(self):
        """Prompt the user to enter a single letter and validate the input."""
        while True:
            guess = input("Enter a single letter: ").lower()  # Convert to lower case for case insensitive comparison
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def main():
    """Main function to run the Hangman game."""
    word_list = ['apple', 'banana', 'cherry', 'jackfruit', 'mango']
    game = Hangman(word_list)
    print("A secret word has been chosen (for testing purposes):", game.word)
    while game.num_lives > 0 and game.num_letters > 0:
        game.ask_for_input()
    if game.num_lives == 0:
        print("Sorry, you ran out of lives. The word was:", game.word)
    else:
        print("Congratulations! You guessed the word:", game.word)

if __name__ == "__main__":
    main()
