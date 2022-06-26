# Cofee Machine
In this script, a simple cofee machine is created.
- Prompts user asking for their choice of cofee
- Turn off the Coffee Machine by entering “off” to the prompt or report gets printed by entering "report"
- Checks if resources sufficient and process coins if resources are sufficient
-  Transaction is successful if user inserts enough money to purchase drink they selected

## Prerequisites
python 3

## How to run code
`python cofee_machine.py`
## Out expected
```
What would you like? (espresso/latte/cappuccino):latte
Please insert coins
How many quarters?:4
How many dimes?:50
How many nickels?:0
How many pennies?:2
Here is $3.52 dollars in change.
Here is your latte. Enjoy!
What would you like? (espresso/latte/cappuccino):cappuccino
Sorry there is not enough  water
Sorry there is not enough  milk
What would you like? (espresso/latte/cappuccino):report
Water:100ml
Milk:50ml
Coffee:76g
Money:$2.5
What would you like? (espresso/latte/cappuccino):espresso
Please insert coins
How many quarters?:0
How many dimes?:4
How many nickels?:51
How many pennies?:0
Here is $1.45 dollars in change.
Here is your latte. Enjoy!
What would you like? (espresso/latte/cappuccino):off
```
