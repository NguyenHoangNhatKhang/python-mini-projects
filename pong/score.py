from turtle import Turtle

ALLIGNMENT = "center"
SIZE = 24 
FONT = "Arial"
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.score = 0
        self.update_score()


    
    def update_score(self):
        self.write(f"Score: {self.score}",align=ALLIGNMENT,font=(FONT,SIZE,"normal"))

    def increase(self):
        self.clear()
        self.score += 1 
        self.write(f"Score: {self.score}",align=ALLIGNMENT,font=(FONT,SIZE,"normal"))

    def game_over(self): 
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER",align=ALLIGNMENT,font=(FONT,SIZE,"normal"))