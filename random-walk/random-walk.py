import turtle as t 
from turtle import Screen 
import random 
tim = t.Turtle()
colors = ["medium turquoise",
          "khaki","azure","medium blue",
          "lime green","aquamarine","firebrick",
          "navy","white","white smoke","light gray",
          "silver","black","royal blue","midnight blue","dodger blue",
          "forest green","orange","dark red","medium slate blue","dark slate blue","dark violet",
          "violet","purple","medium violet red","plum",]

directions = [0,90,180,270]
tim.pensize(15)
tim.speed(0)
for _ in range(3000):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()