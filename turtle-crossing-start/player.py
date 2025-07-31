from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280
HEADING = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create()



    def create(self):
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(HEADING)

    def up(self):
        self.goto(0,self.ycor() + MOVE_DISTANCE)
    
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)
