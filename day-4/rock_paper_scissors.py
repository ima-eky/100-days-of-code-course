import random

# Write your code below this line
game_to_deal=['rock','paper','scissors']
user_choice=int(input(f"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:"))
computer_choice=random.randint(0,2)
if user_choice >2 or user_choice <0:
  print('Invalid number')
elif user_choice == computer_choice:
  print(f'It is a draw')
  print(f'Computer chose {game_to_deal[computer_choice]} and you chose {game_to_deal[user_choice]}')
elif user_choice == 1 and computer_choice==0:
  print(f'You win\nComputer chose {game_to_deal[computer_choice]} and you chose {game_to_deal[user_choice]}')
elif user_choice == 0 and computer_choice==2:
  print(f'You win\nComputer chose {game_to_deal[computer_choice]} and you {game_to_deal[user_choice]}')
elif user_choice ==2 and computer_choice ==1:
  print(f'You win\nComputer chose {game_to_deal[computer_choice]} and you chose {game_to_deal[user_choice]}')
else:
  print(f'Computer wins\nComputer chose {game_to_deal[computer_choice]} and you chose {game_to_deal[user_choice]}')