import random
from hangman_art import  stages

# Update the word list to use the 'word_list' from hangman_words.py

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(f"{' '.join(display)}")
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have guessed this letter before")
        continue
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f'{guess} is not in the word,you have lost a life\nYou have {lives} left')
        if lives == 0:
            end_of_game = True
            print(f"You lose.\nTry again another time")
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Import the stages from hangman_art.py
    print(stages[lives])
else:
    print(f"The correct word was {chosen_word}")
