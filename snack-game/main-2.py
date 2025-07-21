from turtle import Screen, Turtle
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
snake_list = []
starting_posittions = [(0,0),(-20,0),(-40,0)]
for i in range(0,3):
    snake = Turtle("square")
    snake.speed("fastest")
    snake.color("white")
    snake.penup()
    snake.goto(starting_posittions[i])
    snake_list.append(snake)
game_is_on = True
while game_is_on:
    for i in snake_list:
        snake

screen.exitonclick()