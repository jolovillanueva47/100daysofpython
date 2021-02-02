from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

R_START_POSITION=(350,0)
L_START_POSITION=(-350,0)

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)
r_paddle=Paddle(R_START_POSITION)
l_paddle=Paddle(L_START_POSITION)
ball=Ball()
scoreboard=ScoreBoard()

screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #Detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    
    #Detect collision with paddle
    if  ball.distance(r_paddle)< 50 and ball.xcor()>320 or ball.distance(l_paddle)< 50 and ball.xcor()<-320:
        ball.bounce_x()
    
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
        
    
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()