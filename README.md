# Snowman Meltdown ⛄

A terminal-based word guessing game — a wintry take on Hangman. Guess the hidden word letter by letter before the snowman melts! Built in Python with ASCII art stages and clean modular code.

## Demo

```
------------------------------
    _===_
   (     )
    (o o)
    ( : )
   (  :  )

Word: _ _ _ _ _
Mistakes: 0/6
Guessed letters:
------------------------------

Guess a letter: e
Guess a letter: a

Word: _ a _ _ _
Mistakes: 1/6
Guessed letters: e, a
```

## Features

- ⛄ **ASCII snowman** — melts stage by stage with each wrong guess (7 stages total)
- 🎲 **Random word selection** — picks a random word from a built-in word list on each game
- ✅ **Input validation** — rejects non-letters, multiple characters, and already-guessed letters
- 🏆 **Win/lose detection** — announces the result and reveals the word on a loss
- 🧩 **Modular structure** — game logic, ASCII art, words, and entry point separated into distinct files

## Project Structure

```
Snowman-Meltdown/
├── snowman.py       # Entry point — starts the game
├── game_logic.py    # Core game loop, display, and win/lose logic
├── ascii_art.py     # 7 ASCII snowman melt stages
└── words.py         # Word list for random selection
```

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/vincentkoenig/Snowman-Meltdown.git
cd Snowman-Meltdown
```

**2. Run the game**
```bash
python snowman.py
```

No dependencies required — pure Python standard library only.

## How to Play

1. A random word is selected and displayed as underscores
2. Enter one letter at a time to guess
3. Correct guesses reveal the letter in the word
4. Wrong guesses melt the snowman — 6 mistakes and it's over
5. Guess all letters before the snowman melts to win!

## What I Learned

- Separating a project into logical modules (`game_logic`, `ascii_art`, `words`)
- Implementing a game loop with state tracking (guesses, mistakes, win/lose)
- Input validation for interactive CLI programs
- Using `random` for word selection
- Representing progressive game states with ASCII art stages
