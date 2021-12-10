from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scorebord import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height=600)
screen.title("Pong")

screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scorebord = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect collision with the right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 and ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # R paddle miss
    if ball.xcor() > 380:
        ball.reset_pos()
        scorebord.l_point()
    # L paddle miss
    if ball.xcor() < -380:
        ball.reset_pos()
        scorebord.r_point()

screen.exitonclick()
