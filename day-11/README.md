# Black Jack Game
Blackjack also known as 21,is a game that's played using cards.And the goal of the game is to add up your cards to the largest number without going over 21. If the cards in your hand add up two more than 21, then it's called a bust and it means that you lose immediately.. Now the way that the cards are counted is that all the cards from 2 to 10 count as their face value.But the Jack, Queen and King each count as 10 and the other special card is the Ace.Now the Ace can either count as a one towards your total,or it can count as an 11. And depending on whether,if you've gone over 21 or whether if you're under 21,
We're going to assume that each of these cards in the list have equal chance of getting drawn and cards are not removed fom deck to keep game simple.
- In this script,player plays against computer
- The computer can keep dealing cards given that it's total has not exceeded 17.

## Prerequisites

Python must be installed on your computer. Click [here.](https://www.python.org/downloads/) to install if it is not installed.

## How to run the script

`python black_jack.py`

## Output expected
```
Do you want to play a game of Blackjack? Type 'y' or 'n': y

.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           

Your cards:[10, 6],current score: 16
Computer's first card:10
Type 'y' to get another card or 'n' to pass: y
Your cards:[10, 6, 8],current score: 24
Computer's first card:10

Your final hand: [10, 6, 8], final score: 24
Computer's final hand: [10, 6, 10], final score: 26
You went overboard.You lose!
Do you want to play a game of Blackjack? Type 'y' or 'n': n
Goodbye
```
