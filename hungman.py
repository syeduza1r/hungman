import random
from words import words  # Importing a list of words from the words module
from visuals import lives_visual_dict  # Importing visuals for lives from the visuals module
import string


def get_valid_word(words):
    """
    Function to get a valid word from the list of words.
    Ensures the word does not contain '-' or spaces.
    """
    word = random.choice(words)  # Randomly chooses a word from the list
    while '-' in word or ' ' in word:  # Ensures the word does not contain '-' or spaces
        word = random.choice(words)

    return word.upper()  # Returns the word in uppercase


def hangman():
    """+
    Main function to play the Hangman game.
    """
    word = get_valid_word(words)  # Get a valid word for the game
    word_letters = set(word)  # Set of unique letters in the word
    alphabet = set(string.ascii_uppercase)  # Set of uppercase English letters
    used_letters = set()  # Set to track letters guessed by the user

    lives = 7  # Number of lives the user has

    # Game loop: continues until the user guesses the word or runs out of lives
    while len(word_letters) > 0 and lives > 0:
        # Display the number of lives left and the letters already guessed
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # Display the current state of the word (e.g., W - R D for "WORD")
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])  # Display the visual representation of lives
        print('Current word: ', ' '.join(word_list))

        # Get user input for a letter guess
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:  # If the letter is valid and not guessed before
            used_letters.add(user_letter)  # Add the letter to the set of used letters
            if user_letter in word_letters:  # If the guessed letter is in the word
                word_letters.remove(user_letter)  # Remove the letter from the set of word letters
                print('')

            else:
                lives = lives - 1  # Decrease a life if the guess is incorrect
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:  # If the letter was already guessed
            print('\nYou have already used that letter. Guess another letter.')

        else:  # If the input is invalid
            print('\nThat is not a valid letter.')

    # End of the game: either the user guessed the word or ran out of lives
    if lives == 0:  # If the user ran out of lives
        print(lives_visual_dict[lives])  # Display the final visual representation
        print('You died, sorry. The word was', word)  # Reveal the word
    else:  # If the user guessed the word
        print('YAY! You guessed the word', word, '!!')  # Congratulate the user


hangman()  # Start the game