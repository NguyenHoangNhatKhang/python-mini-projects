FIXED_POSITION = [(100,-200),(-100,200)]

from turtle import Turtle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        for position in FIXED_POSITION:
            self.create(position)


    def create(self,position): 
        self.shape("square")
        self.color("white")
        self.shapesize(1,5)
        self.penup()
        self.goto(position)

    def move_up(self):
        self.forward(20)
    def move_down(self):
        self.backward(20)