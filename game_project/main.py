from turtle import Turtle,Screen
import random
from Paddle import p_addle
from ball import Ball
import time
from Scoreboard import scoreboard


screen=Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")

screen.tracer(0) # makes animation off nad you need to continuously refresh and update it to make it show things

l_paddle=p_addle((-350,0))
r_paddle=p_addle((350,0))
ball=Ball()
score=scoreboard()
ball.speed(1)

screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detecting collisions
    if ball.ycor() > 280 or ball.ycor()<-280 :
        ball.rebound_y()
    # detecting the R miss
    elif ball.xcor()>380 :
        ball.refresh_ball()
        score.l_points()

   # detecting the L miss
    elif ball.xcor()<-380:
        ball.refresh_ball()
        score.r_points()

    # now detecting collisions with the paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.rebound_x()
        # increasing the speed of ball each time we hit the paddle
        # speed will be managed by the time sleep

        # here less than 50 is written because we have a stretched paddle here and distance is measured from
        # center to center otherwise it will not consider the  collision
        # but here rebound is in x direction that is opposing the x direction
    if score.l_score==10 :
        game_is_on=False
        score.game_over()

    elif score.r_score==10:
        game_is_on=False
        score.game_over()
screen.exitonclick()
