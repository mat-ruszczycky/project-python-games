import random

from src.wordlist import WORDS
from src.display import *

def play_hangman():
    isPlaying = 'y'

    while isPlaying == 'y':
        word = random.choice(WORDS)  # Randomly select a word from the list
        guessed_letters = set()       # Store letters the player has guessed
        tries = 6                     # Number of incorrect guesses allowed

        print("Welcome to Hangman!")
        print("Guess the word!")
    
        while tries > 0:
            displayStatus(word, guessed_letters, tries)

            guess = input("Guess a letter: ").lower()

            if not is_valid_guess(guess, guessed_letters):
                continue  # Skip to the next iteration if the guess is invalid

            guessed_letters.add(guess)  # Add the guessed letter to the set

            if guess in word:
                print(f"Good guess! '{guess}' is in the word.")
            else:
                print(f"Sorry, '{guess}' is not in the word.")
                tries -= 1  # Decrement the number of tries

            if all(letter in guessed_letters for letter in word):
                print(f"\nCongratulations! You guessed the word: '{word}'")
                isPlaying = is_playing()
                break
        else:
            print(f"\nSorry, you've run out of tries. The word was: '{word}'")
            isPlaying = is_playing()