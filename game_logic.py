from ascii_art import STAGES
from snowman import WORDS
import random

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print("\n" + "-" * 30)
    print(STAGES[mistakes])

    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word.strip())
    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}")
    print("Guessed letters:", ", ".join(guessed_letters))
    print("-" * 30 + "\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    display_game_state(mistakes, secret_word, guessed_letters)

    while True:
        guess = input("Guess a letter: ").lower()

        # Input Validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Double guess
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        # Mistakes
        if guess not in secret_word:
            mistakes += 1

        display_game_state(mistakes, secret_word, guessed_letters)

        # Win
        if all(letter in guessed_letters for letter in secret_word):
            print("You saved the snowman!")
            break

        # Lose
        if mistakes >= len(STAGES) - 1:
            print("The snowman melted!")
            print("The word was:", secret_word)
            break


if __name__ == "__main__":
    while True:
        play_game()

        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break