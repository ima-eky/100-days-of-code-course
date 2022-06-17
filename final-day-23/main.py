import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

score=Scoreboard()
player=Player()
car=CarManager()

screen.listen()
screen.onkeypress(key='Up',fun=player.move_forward)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()
    # detect sucessful crossing
    if player.ycor() > 280:
        car.refresh_level_speed()
        score.increase_level()
        player.refresh_level()
    #detect collision with car
    for car_distance in car.all_cars:
       if player.distance(car_distance) < 20:
           game_is_on=False
           score.game_over()

screen.exitonclick()