from turtle import Turtle,Screen
import time
class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.coordinates=coordinates
        self.create_paddle(coordinates)
    def create_paddle(self,coordinates):
        self.shape('square')
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coordinates)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def left_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def left_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

