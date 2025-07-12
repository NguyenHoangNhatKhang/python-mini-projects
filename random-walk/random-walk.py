from turtle import Turtle , Screen
from random import choice

tim = Turtle()
colors = ["medium turquoise",
          "khaki","azure","medium blue",
          "lime green","aquamarine","firebrick",
          "navy","white","white smoke","light gray",
          "silver","black","royal blue","midnight blue","dodger blue",
          "forest green","orange","dark red","medium slate blue","dark slate blue","dark violet",
          "violet","purple","medium violet red","plum",]


def random_colors():
    return choice(colors)
direction = ["left","right","up","down"]
print(choice(direction))
tim_run = 10000
tim.pensize(7)
tim.speed(0)
while tim_run:
    dir_choice = choice(direction)
    if dir_choice == "left":
        tim.color(random_colors())
        tim.left(90)
        tim_run-=1
    elif dir_choice == "right":
        tim.color(random_colors())
        tim.right(90)
        tim_run-=1
    elif dir_choice == "up":
        tim.color(random_colors())
        tim.forward(10)
        tim_run-=1
    elif dir_choice == "down":
        tim.color(random_colors())
        tim.backward(10)
        tim_run-=1













screen = Screen()
screen.exitonclick()