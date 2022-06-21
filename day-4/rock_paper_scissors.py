import random

# Write your code below this line
number_of_games=int(input(f"How many times do you want to play?:"))
game_to_deal=['rock','paper','scissors']

user_score=0
computer_score=0
while number_of_games > 0:
  user_choice=int(input(f"\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:"))
  computer_choice=random.randint(0,2)
  if user_choice >2 or user_choice <0:
    print('Invalid number')
  elif user_choice == computer_choice:
    print(f'It is a draw')
    print(f'Computer chose {game_to_deal[computer_choice]} and you chose {game_to_deal[user_choice]}')
  elif user_choice == 1 and computer_choice==0:
    print(f'You win\nComputer chose {game_to_deal[computer_choice]} and you chose {game_to_deal[user_choice]}')
    user_score +=1
  elif user_choice == 0 and computer_choice==2:
    print(f'You win\nComputer chose {game_to_deal[computer_choice]} and you {game_to_deal[user_choice]}')
    user_score +=1
  elif user_choice ==2 and computer_choice ==1:
    print(f'You win\nComputer chose {game_to_deal[computer_choice]} and you chose {game_to_deal[user_choice]}')
    user_score += 1
  else:
    print(f'Computer wins\nComputer chose {game_to_deal[computer_choice]} and you chose {game_to_deal[user_choice]}')
    computer_score +=1
  print(f"User score: {user_score}              Computer_score: {computer_score}")
  number_of_games -=1
  print(f"{number_of_games} trials left\n")
else:
  print(f"User score: {user_score}              Computer_score: {computer_score}")
  if user_score > computer_score:
    print('Congratulations,You won')
  elif user_score == computer_score:
    print(f'It is a draw')
  else:
    print("You lose")
