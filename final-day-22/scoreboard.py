from turtle import Turtle
ALIGNMENT='center'
FONT=('Courier',50,'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score=0
        self.right_score=0

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 230)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 230)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)

    def left_point(self):
        self.left_score +=1
        self.update_scoreboard()
    def right_point(self):
        self.right_score +=1
        self.update_scoreboard()