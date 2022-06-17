from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
FONT=('Courier',40,'normal')

class Player (Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.shape('turtle')
        self.color('red')
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def refresh_level(self):
        self.goto(STARTING_POSITION)

