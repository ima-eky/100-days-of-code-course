import time
from turtle import Screen,Turtle
from paddle import Paddle
from scoreboard import  Score
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")

screen.tracer(0)


right_paddle=Paddle((350,0))
left_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Score()

screen.listen()
screen.onkeypress(key="Up",fun=right_paddle.up)
screen.onkeypress(key="Down",fun=right_paddle.down)
screen.onkeypress(key="w",fun=left_paddle.left_up)
screen.onkeypress(key="s",fun=left_paddle.left_down)







game_is_on=True

while game_is_on:
    time.sleep(ball.speed_rate)
    screen.update()
    ball.play()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()
    #detect collision with paddle
    if ball.distance(right_paddle) <55 and ball.xcor() > 330 or ball.distance(left_paddle) <55 and ball.xcor() < -330:
        ball.bounce_x()

    #detect if ball goes out of bounds
      #detect if right paddle misses ball
    elif ball.xcor() > 380:
        scoreboard.left_point()
        ball.reset_coordinates()
      #detect if left paddle misses ball
    elif ball.xcor() <-380:
        scoreboard.right_point()
        ball.reset_coordinates()





screen.exitonclick()