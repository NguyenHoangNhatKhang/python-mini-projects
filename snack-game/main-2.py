from turtle import Screen
from snake2 import Snake 
from food import Food
from score import Score
import time 
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My  Snake Game")
snake = Snake()
food = Food()
score = Score()
screen.listen()
game_is_on = True
screen.onkey(snake.move_up,"w")
screen.onkey(snake.move_down,"s")
screen.onkey(snake.move_left,"a")
screen.onkey(snake.move_right,"d")
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food) < 15:
        snake.extend() 
        food.random_location()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10: 
            score.reset()
            snake.reset()


screen.exitonclick()