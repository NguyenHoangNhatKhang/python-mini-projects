from paddle import Paddle
import time
from turtle import Screen 



screen = Screen()
screen.tracer(0)
screen.title("Pong")
screen.setup(800,600)
screen.bgcolor("black")

game_is_on = True 
while game_is_on: 
    screen.update()
    t = Paddle()
    
    

screen.listen()
screen.onkey(t.move_up,"w")
screen.onkey(t.move_down,"s")
screen.exitonclick()


