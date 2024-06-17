# Step 1: Import the random module
import random

# Step 2: Create a list containing the names of your 5 favorite fruits
fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

# Step 3: Assign this list to a variable called word_list
word_list = fruits

# Step 4: Print out the newly created list to the standard output (screen)
print(word_list)

# Step 5: Use random.choice to select a random word from word_list
word = random.choice(word_list)

# Step 6: Print the randomly selected word to the standard output
print(word)

# Step 7: Using the input function, ask the user to enter a single letter
guess = input("Enter a single letter: ")

# Step 8: Check that the input is a single alphabetical character
if len(guess) == 1 and guess.isalpha():
    # Step 9: Print a message if the input is valid
    print("Good guess!")
else:
    # Step 10: Print a message if the input is not valid
    print("Oops! That is not a valid input.")



