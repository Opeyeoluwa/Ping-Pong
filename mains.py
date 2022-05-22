from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
#screen.bgcolor("black")
screen.bgpic("b.png")
screen.title("PING PONG PRO")
screen.tracer(0)
screen.listen()



l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ping_ball = Ball()
score= Score()

game_on = True

# Use keys 1 and 2 for left paddle
screen.onkey(l_paddle.up, "1")
screen.onkey(l_paddle.down, "2")

# Use Up and Down arrow keys for right paddle
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

while game_on:
    time.sleep(ping_ball.meter)
    screen.update()
    ping_ball.move()

# detect collission with wall
    if ping_ball.ycor() > 280 or ping_ball.ycor() < -280:
        ping_ball.bounce_y()

# hit padle
    if ping_ball.distance(r_paddle) < 50 and ping_ball.xcor() > 320 or ping_ball.distance(l_paddle) < 50 and ping_ball.xcor() < -320:
       ping_ball.bounce_x()


# if right misses
    if ping_ball.xcor() > 380:
        ping_ball.refresh()
        score.l_scored()

# if left misses
    if ping_ball.xcor() < -380:
        ping_ball.refresh()
        score.r_scored()

screen.exitonclick()