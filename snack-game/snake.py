from turtle import Turtle 
class Snake:
    segments = []
    game_is_on = True
    position = [(0,0),(-20,0),(-40,0)]
    def __init__(self):
        pass

    @classmethod    
    def create_snake(cls):
        for i in range(0,3):
            segment = Turtle('turtle')
            segment.color("white")
            segment.penup()
            segment.goto(cls.position[i])
            cls.segments.append(segment)
    
    @classmethod 
    def start(cls):
        while cls.game_is_on:
            for i in range(len(cls.segments)-1,0,-1):
                new_x = cls.segments[i-1].xcor()
                new_y = cls.segments[i-1].ycor()
                cls.segments[i].goto(new_x,new_y)
            cls.segments[0].forward(20)