# Collect data from starting_letter for the letters prototype

with open('./Input/Letters/starting_letter.txt') as read_letter:
    content=read_letter.read()

#Generate a list of all the names that are to receive the letters

with open('./Input/Names/invited_names.txt') as file:
    names=file.readlines()

#Customize each starting_letter to fit an individual

for name in names:
    individual_name='[name]'
    new_letter=content.replace(individual_name,name.strip())
    with open(f'./Output/ReadyToSend/letter_for_{name.strip()}.txt','w') as completed_letter:
        completed_letter.write(new_letter)
        #letters are ready to send now
