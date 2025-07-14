from turtle import Turtle, Screen , colormode
import random 


tim = Turtle()
tim.speed("fastest") #equipvalent to 0 
colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color
def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        tim.pensize(5)
        tim.circle(100) 
        tim.color(random_color())
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)


gap = int(input("Nhập khoảng cách góc (VD: 5, 10, 15...): "))
if 1 <= gap <= 360:
    draw_spirograph(size_of_gap=gap)
else: 
    print("INVALID")


screen = Screen()
screen.exitonclick()