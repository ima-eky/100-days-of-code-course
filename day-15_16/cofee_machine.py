MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {"water": 300, "milk": 200, "coffee": 100, 'money': 0}
transaction_successful= True
customer_cash=0
while (transaction_successful):
    user_choice=input(f"What would you like? (espresso/latte/cappuccino):").lower().strip()
    if user_choice == 'off':
        transaction_successful = False
    elif user_choice == 'report':
        for key in resources:
            if key=='water' or key=='milk':
                print(f'{key.title()}:{resources[key]}ml')
            elif key== 'coffee':
                print(f'{key.title()}:{resources[key]}g')
            else:
                print(f'{key.title()}:${resources[key]}')

    else:
        drink_resource = MENU[user_choice]
        should_continue=True
        amount_of_check=0
        for ingredients in drink_resource["ingredients"]:
            check= resources[ingredients]-(drink_resource["ingredients"])[ingredients]
            if check < 0:
                amount_of_check+=1
                print(f'Sorry there is not enough  {ingredients}')
                should_continue=False

        if should_continue:
            print(f'Please insert coins')
            customer_cash=int(input(f'How many quarters?:')) *0.25
            customer_cash+= int(input(f'How many dimes?:'))*0.1
            customer_cash+= int(input(f'How many nickels?:')) *0.05
            customer_cash += int(input(f'How many pennies?:'))*0.01
            cost_of_drink=drink_resource['cost']
            if customer_cash >= cost_of_drink:
                resources['money'] = (resources['money']) + cost_of_drink
                customer_change=customer_cash-cost_of_drink
                if customer_change > 0:
                    rounded_change = '{:.2f}'.format(customer_change)
                    print(f'Here is ${rounded_change} dollars in change.')
                print(f'Here is your latte. Enjoy!')
                for ingredients in drink_resource["ingredients"]:
                    if ingredients != 'money':
                         resources[ingredients]-=(drink_resource["ingredients"])[ingredients]




            else:
                print(f'Sorry that\'s not enough money. Money refunded.')










