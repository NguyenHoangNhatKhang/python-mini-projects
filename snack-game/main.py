from turtle import Screen, Turtle
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
snake_list = []
x_posistions = [-40,-20,0]
for i in range(0,3):
    snake = Turtle("square")
    snake.speed("fastest")
    snake.color("white")
    snake.penup()
    snake.goto(x_posistions[i],0)
    snake_list.append(snake)
    


screen.exitonclick()