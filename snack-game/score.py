from turtle import Turtle
ALLIGNMENT = "center"
FONT = "Courier"
SIZE = 24 
STYLE = "normal"
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.update_score()
        self.hideturtle()
    
    def update_score(self):
        self.write(f"Score: {self.score}",align=ALLIGNMENT,font=(FONT,SIZE,STYLE))
    def increase_score(self):
        self.score +=  1 
        self.clear()
        self.update_score()
    
    def game_over(self): 
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER",align=ALLIGNMENT,font=(FONT,SIZE,STYLE))
    
    