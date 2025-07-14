import turtle as t 
from turtle import Screen 
import random 
tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)
   

STEP = 30
LIMIT = 390  # trừ đi nửa bước vẽ và độ dày để tránh lọt mép

directions = [0,90,180,270]
tim.pensize(15)
tim.speed(0)
for _ in range(100000):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
     # Dự đoán vị trí tiếp theo nếu đi thêm STEP
    next_x = tim.xcor() + STEP * round(tim.heading() == 0) - STEP * round(tim.heading() == 180)
    next_y = tim.ycor() + STEP * round(tim.heading() == 90) - STEP * round(tim.heading() == 270)

    # Nếu bước tiếp theo vượt khung → quay đầu 180°
    if not (-LIMIT < next_x < LIMIT and -LIMIT < next_y < LIMIT):
        tim.setheading((tim.heading() + 180) % 360)


screen = Screen()
screen.exitonclick()