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
        self.secret_word = random.choice(word_list).lower()
        self.guessed_word = ['_' for _ in self.secret_word]
        self.remaining_letters = len(set(self.secret_word))
        self.guessed_letters = []

    def _update_guessed_word(self, guess):
        """
        Update the guessed_word list with the guessed letter.

        Args:
            guess (str): The guessed letter.
        """
        for index, letter in enumerate(self.secret_word):
            if letter == guess:
                self.guessed_word[index] = guess
        self.remaining_letters -= 1

    def _print_game_status(self):
        """Print the current state of the guessed word and remaining lives."""
        print("Current word:", " ".join(self.guessed_word))
        print(f"You have {self.num_lives} lives left.")

    def check_guess(self, guess):
        """
        Check if the guessed letter is in the secret word.

        Args:
            guess (str): The guessed letter.
        """
        guess = guess.lower()
        if guess in self.secret_word:
            print(f"Good guess! '{guess}' is in the word.")
            self._update_guessed_word(guess)
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            self.num_lives -= 1
        self._print_game_status()

    def ask_for_input(self):
        """Prompt the user to enter a single letter and validate the input."""
        while True:
            guess = input("Enter a single letter: ").lower()
            if not self._is_valid_guess(guess):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.guessed_letters:
                print("You already tried that letter!")
            else:
                self.guessed_letters.append(guess)
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

def play_game(word_list):
    """
    Play the Hangman game.

    Args:
        word_list (list): List of possible words for the game.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)
    print("A secret word has been chosen. Let's start the game!")
    while True:
        if game.num_lives == 0:
            print("You lost! The word was:", game.secret_word)
            break
        elif game.remaining_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations! You won the game! The word was:", game.secret_word)
            break

if __name__ == "__main__":
    word_list = ['apple', 'banana', 'cherry', 'date', 'mango']
    play_game(word_list)

