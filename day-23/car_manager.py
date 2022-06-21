from turtle import  Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.speed_rate=STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance=random.randint(1,6)
        if random_chance == 1 or random_chance ==5 :
            new_car=Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.y_cor=random.randint(-250,250)
            new_car.goto(300, new_car.y_cor)
            self.all_cars.append(new_car)
    def move_car(self):
        for car in self.all_cars:
            car.backward(self.speed_rate)

    def refresh_level_speed(self):
        self.speed_rate +=MOVE_INCREMENT
