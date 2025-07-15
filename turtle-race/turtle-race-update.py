from turtle import Turtle, Screen 
import random

turtles = {}
screen = Screen()
screen.setup(width=500,height=400)
is_race_on = False
colors = ["red","blue","green","yellow","black","brown"]
your_bet = screen.textinput("YOUR BET","ENTER YOUR TURTLE COLOR").lower().strip()
y_posittions = [-100,-70,-40,-10,20,50]
for i in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    turtles[i] = new_turtle
    turtles[i].color(colors[i])
    turtles[i].goto(x=-230,y=y_posittions[i])

if your_bet in colors:
    is_race_on = True 
    noti = screen.textinput("ARE YOU READY?","Yes/No").lower().strip()
    if noti == "yes":
        while is_race_on:
            for i in turtles: 
                turtles[i].forward(random.randint(0,10))
                if turtles[i].xcor() >= 230:
                    winner = turtles[i].pencolor()
                    if winner == your_bet:
                        print(f"Winner is: {winner}!!You are the winner")
                        is_race_on = False
                    else: 
                        print(f"Winner is {winner}!!You are not the winner!")
                        is_race_on = False
    elif noti == "no":
        screen.exitonclick()
    else: 
        print("INVALID")
        screen.exitonclick()

     
