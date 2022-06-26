import random

print(f'Welcome to the Number Guessing Game\nI am thinking of a number between 1 and 100')
difficulty_type = input(f'Choose a difficulty.Type "easy" or "hard":').lower()
random_number = random.randint(1, 100)
if difficulty_type == 'easy':
    attempts = 10
elif difficulty_type == 'hard':
    attempts = 5
while (attempts > 0):
    if attempts != 1:
        print(f'You have {attempts} attempts to guess the number.')
    else:
        print(f'You have {attempts} attempt to guess the number.')
    user_guess = int(input(f'Guess a number:'))
    if user_guess != random_number:
        attempts -= 1
        if user_guess > random_number:
            print(f'Too high')
        else:
            print(f'Too low')
    else:
        attempts = 0
        print(f'You have guessed the number {random_number} correctly!\nCongratulations')
else:
    print(f'You have {attempts} attempts to guess the number.The number wass {random_number}')




