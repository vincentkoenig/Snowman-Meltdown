from ascii_art import STAGES
from snowman import WORDS
import random

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])

    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        if guess in secret_word:
            guessed_letters.append(guess)
        else:
            mistakes += 1
            print(f"Mistakes: {mistakes}")

        display_game_state(mistakes, secret_word, guessed_letters)

        if all(letter in guessed_letters for letter in secret_word):
            print("You saved the snowman!")
            break

        if mistakes >= len(STAGES) - 1:
            print("The snowman melted!")
            print("The word was:", secret_word)
            break


if __name__ == "__main__":
    play_game()