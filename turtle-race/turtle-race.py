from turtle import Turtle, Screen 
import random

turtles = {}
screen = Screen()
screen.setup(500,400)
colors = ["red","blue","green","yellow","black"]
     
def create_turtles(turtle_numbers):
    spacing = 30
    if turtle_numbers > len(colors):
        print("Not enough unique colors")  
        return
    used_colors = random.sample(colors,turtle_numbers)
    for i in range(turtle_numbers):
        new_turtle = Turtle("turtle")
        new_turtle.color(used_colors[i])
        new_turtle.penup()
        new_turtle.goto(-230, -100 + i * spacing)
        turtles[f"turtle_{i+1}"] = new_turtle

def random_steps():
    return random.randint(0,30)
def run():
    turtle_num = screen.numinput("Quantity","Enter Turtles Quantity")
    bet_noti = screen.textinput("Bet","Enter Turtles Color")
    create_turtles(int(turtle_num))
    if bet_noti in colors:
        race_on = True
        while race_on:
            for i in range(int(turtle_num)):
                runner = turtles[f"turtle_{i+1}"]
                runner.forward(random_steps())
                winner = runner.pencolor()
                if runner.xcor() >= 230: 
                    print(f"{winner}is the winner!")
                    if winner == bet_noti:
                        print(f"You are the winner!")
                        break
                    else: 
                        print(f"You are not the winner!")
                        race_on = False

run()
screen.exitonclick()