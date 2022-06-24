## Hangman
Hangman is a popular word guessing game where the player attempts to build a missing word by guessing one letter at a time. After a certain number of incorrect guesses(six in this script), the game ends and the player loses. The game also ends if the player correctly identifies all the letters of missing word.
As the player makes wrong guesses,a picture of hangman(stages) is drawn.
- You might  have to import hangman_art.py if you haven't(also in day-7 directory) to access these drawings of hangman for each stage of failure using ``` from hangman_art import stages ``` or ``` import hangman_art```(to use stages,`hangman_art.stages` can be used) or  you can rename the module ``` import hangman_art as player_status```(to use stages,`player_status.stages` can be used)
- You can read more on [Python Modules](https://www.w3schools.com/python/python_modules.asp)

## Recommended Resources
- [Python range() Function](https://www.w3schools.com/python/ref_func_range.asp)
- [Python User Input](https://www.w3schools.com/python/python_user_input.asp)
- [Python while loops](https://www.w3schools.com/python/python_while_loops.asp)
- [Python String join() method](https://www.w3schools.com/python/ref_string_join.asp)
- [Python Random choice() method](https://www.w3schools.com/python/ref_random_choice.asp)
 
 ## Prerequisites

Python must be installed on your computer. Click [here.](https://www.python.org/downloads/) to install if it is not installed.

## How to run the script

`python hangman.py`

## Output expected
```
_ _ _ _
Guess a letter: i
i is not in the word,you have lost a life
You have 5 left
_ _ _ _

  +---+
  |   |
  O   |
      |
      |
      |
=========

Guess a letter: a
a is not in the word,you have lost a life
You have 4 left
_ _ _ _

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

Guess a letter: e
_ _ _ e

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

Guess a letter: m
m is not in the word,you have lost a life
You have 3 left
_ _ _ e

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
Guess a letter: d
_ _ d e

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
Guess a letter: f
f is not in the word,you have lost a life
You have 2 left
_ _ d e

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

Guess a letter: c
c _ d e

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

Guess a letter: d
You have guessed this letter before
Guess a letter: o
c o d e
You win.

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

The correct word was code
```
