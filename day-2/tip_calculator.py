print('Welcome to the the calculator!')

# gets user's input
bill = float(input(f'What was the total bill?: $'))
#input () returns a string as output
tip = int(input(f'How much tip would you like to give? 10, 12, or 15?: '))
number_of_people = int(input(f'How many people to split the bill?:'))

tip_percent = tip/100
total_tip= bill *tip_percent
total_bill=total_tip + bill
individual_bill=total_bill/number_of_people
rounded_individual_bill='{:.2f}'.format(individual_bill)
print(f'Each person should pay: ${rounded_individual_bill}')