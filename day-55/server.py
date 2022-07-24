import random
from flask import Flask

def generate_random_number():
    return random.randint(0,9)

#creating a new flask application
app=Flask(__name__)

#home route
@app.route("/")
def game_info():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="Guess!">'


random_number=generate_random_number()

# creating a route that detects the number entered by the user
@app.route("/<int:number>")
def check_guess(number):
    global  random_number
    if number < random_number:
        return '<h1 style ="color :black">Too low,try again! 😶 </h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="Guess again!">'
    elif number > random_number:
        return '<h1 style="color: red">Too high,try again! 😶 </h1>' \
               '<img src ="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="Guess again!">'
    else:
        random_number = generate_random_number()
        return '<h1 style="color:blue">You found me 😁!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="Correct!">'




if __name__ == "__main__":
    app.run(debug=True)