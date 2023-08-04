import random
words = ["apple", "banana", "cherry", "dragon", "elephant", "flower", "giraffe", "honey", "icecream", "jungle"]


word = random.choice(words)

# The number of chances
chances = 6

# The letters that have been guessed
guessed = []

# The word as a list of underscores
hidden = ["_"] * len(word)

# A flag to indicate if the game is over
game_over = False

# A function to display the current state of the game
def display():
    print("Word: " + " ".join(hidden))
    print("Chances: " + str(chances))
    print("Guessed: " + ", ".join(guessed))

# A function to check if the player has won or lost
def check():
    global game_over
    if "_" not in hidden:
        print("You win! The word was " + word)
        game_over = True
    elif chances == 0:
        print("You lose! The word was " + word)
        game_over = True

# Start the game
print("Welcome to Hangman!")
display()

# Loop until the game is over
while not game_over:
    # Ask the player to guess a letter
    guess = input("Guess a letter: ").lower()

    # Check if the letter is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
    # Check if the letter has been guessed before
    elif guess in guessed:
        print("You have already guessed this letter.")
    # Check if the letter is in the word
    elif guess in word:
        print("Good guess!")
        # Reveal the letter in the hidden word
        for i in range(len(word)):
            if word[i] == guess:
                hidden[i] = guess
        # Add the letter to the guessed list
        guessed.append(guess)
    # If the letter is not in the word
    else:
        print("Sorry, that letter is not in the word.")
        # Reduce the number of chances by one
        chances -= 1
        # Add the letter to the guessed list
        guessed.append(guess)

    # Display the current state of the game
    display()
    # Check if the player has won or lost
    check()