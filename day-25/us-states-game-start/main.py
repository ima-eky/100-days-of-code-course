import turtle
from turtle import  Turtle,Screen
import pandas

screen=Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game_is_on =True
score =0
correct_guesses = []
while game_is_on:
    user_answer=screen.textinput(title=f"{score}/50 States Correct",prompt="What's another state's name")
    user_answer=user_answer.title()

    #using the pandas library to get data
    data=pandas.read_csv("50_states.csv")
    list_of_states=data['state'].to_list()
    if user_answer == 'Exit':
        game_is_on =False
    elif user_answer in list_of_states:
        if user_answer in correct_guesses:
            continue
        else:
            score += 1
            correct_guesses.append(user_answer)
            state_data=data[data.state == user_answer]
            x_cor=int(state_data.x)
            y_cor=int(state_data.y)
            turtle=Turtle()
            turtle.penup()
            turtle.hideturtle()
            turtle.goto(x_cor,y_cor)
            #turtle.write(user_answer,align='center',font=('Courier',10,'normal'))
            turtle.write(state_data.state.item())
    else:
        continue
missing_states=[ element for element in list_of_states if  element not  in correct_guesses]

new_data=pandas.DataFrame(missing_states)
new_data.to_csv('states_to_learn.csv')