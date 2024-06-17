import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initialize the attributes of the Hangman game.

        Args:
            word_list (list): List of possible words for the game.
            num_lives (int): Number of lives the player has.
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def _update_word_guessed(self, guess):
        """
        Update the word_guessed list with the guessed letter.

        Args:
            guess (str): The guessed letter.
        """
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess
        self.num_letters -= 1

    def _print_current_state(self):
        """Print the current state of the guessed word and lives left."""
        print("Current word:", " ".join(self.word_guessed))
        print(f"You have {self.num_lives} lives left.")

    def check_guess(self, guess):
        """
        Check if the guessed letter is in the secret word.

        Args:
            guess (str): The guessed letter.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            self._update_word_guessed(guess)
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            self.num_lives -= 1
        self._print_current_state()

    def ask_for_input(self):
        """Prompt the user to enter a single letter and validate the input."""
        while True:
            guess = input("Enter a single letter: ").lower()
            if not self._is_valid_guess(guess):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break

    def _is_valid_guess(self, guess):
        """
        Validate the guessed letter.

        Args:
            guess (str): The guessed letter.

        Returns:
            bool: True if the guess is valid, False otherwise.
        """
        return len(guess) == 1 and guess.isalpha()

def main():
    """Main function to run the Hangman game."""
    word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
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

