from turtle import Screen
from paddle import Paddle
from ball import Ball
import time 
from score import Score
import random
screen = Screen()
random_x = random.randint(-580,580)
random_y = random.randint(-580,580)
ball_cor = [random_x,random_y]
right_paddle = [350,0]
left_paddle = [-350,0]
screen.bgcolor("black")
screen.setup(800,600)
screen.tracer(0)
screen.listen()
pad1 = Paddle(right_paddle)
pad2 = Paddle(left_paddle)
ball = Ball(ball_cor)
score = Score()
screen.onkey(pad1.up,"w")
screen.onkey(pad1.down,"s")
screen.onkey(pad2.up,"Up")
screen.onkey(pad2.down,"Down")



game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280: 
        ball.bounce_y()

    if (ball.distance(pad1) < 50 and ball.xcor() > 340) or (ball.distance(pad2) < 50 and ball.xcor() > -340):
        score.increase()
        ball.bounce_x() 

    
    if ball.xcor() >= 400 or ball.xcor() <= -400:
        ball.resetd()
        score.game_over()
        game_on = False 

        
         



        








screen.exitonclick()