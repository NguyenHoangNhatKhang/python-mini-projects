POSITION = [(350,0),(-350,0)]
from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(pos)

    def up(self):
        new_y = self.ycor()+40
        self.goto(self.xcor(),new_y)


    
    def down(self):
        new_y = self.ycor()-40
        self.goto(self.xcor(),new_y)

    