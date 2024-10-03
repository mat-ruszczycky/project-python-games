# Display methods
def display_word(word, guessed_letters):
    """Display the current state of the word with guessed letters revealed."""
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def is_valid_guess(guess, guessed_letters):
    """Check if the guessed letter is valid."""
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        return False

    if guess in guessed_letters:
        print("You already guessed that letter.")
        return False

    return True