
#You can call clear() to clear the output in the console.
from art import logo
from replit import clear

print(logo)
print(f'Welcome to the secret auction program')
dict={}
choice =True

while(choice):
  clear()
  name=input(f'What is your name?: ')
  dict[name]=int(input(f'What\'s your bid?: $'))
  choice=input(f'Is there any other bider yes or no?:').lower()
  if choice=='yes':
    clear()
  else:
    choice=not True
highest_bid=0
for key in dict:
  if dict[key]>highest_bid:
    highest_bid=dict[key]
    winner=key
  print(f'The winner is {winner} and the highest_bid is {highest_bid}')