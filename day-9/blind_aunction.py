
#HINT: You can call clear() to clear the output in the console.
import  os
from art import logo
print(logo)
print(f'Welcome to the secret auction program')
dict={}
choice =True
while(choice):
  name=input(f'What is your name?: ')
  dict[name]=int(input(f'What\'s your bid?: $'))
  choice=input(f'Is there any other bider yes or no?:').lower()
  if choice=='yes':
    choice=True
    os.system("clear")
  else:
    choice=not True
highest_bid=0
for key in dict:
  if dict[key]>highest_bid:
    highest_bid=dict[key]
    winner=key
  print(f'The winner is {winner} and the highest_bid is {highest_bid}')