from turtle import Turtle, Screen , colormode 
import random
# import colorgram 
# colors = colorgram.extract('hirst-painting/pictures/damien_hirst-dotted.jpg' ,30)
# rgb_colors =[]
# def create_rgb():
#     for color in colors: 
#         r = color.rgb.r
#         g = color.rgb.b
#         b = color.rgb.g
#         new_color = (r,g,b)
#         rgb_colors.append(new_color)
#     return rgb_colors
colormode(255)
color_list = [
     (204, 107, 159),
    (231, 109, 213), (134, 192, 168), (44, 144, 105), (152, 53, 78),
    (199, 164, 142), (15, 53, 32), (181, 42, 159), (148, 87, 65),
    (141, 155, 178), (205, 70, 91), (64, 92, 117), (195, 118, 89),
    (225, 187, 170), (15, 27, 38), (59, 19, 34), (227, 166, 175),
    (48, 182, 158), (238, 4, 213), (87, 112, 155), (121, 53, 35),
    (177, 216, 188), (35, 110, 58), (169, 184, 206), (60, 36, 21),
    (14, 71, 96)
]

damien_hirst = Turtle()
damien_hirst.speed("fastest")  
damien_hirst.penup()
damien_hirst.hideturtle()
rows = 10
cols = 10  
spacing = 50 
grid_width = spacing * cols
grid_height = spacing * rows
start_x = -grid_width / 2
start_y = grid_height / 2
damien_hirst.goto(start_x, start_y)
def random_color(): 
    return random.choice(color_list)

def create_table(rows,cols):
    spacing = 50 
    for row in range(0,rows):
        for col in range(0,cols):
            damien_hirst.dot(20,random_color())
            damien_hirst.penup()
            damien_hirst.forward(spacing)
        damien_hirst.backward(spacing * cols)
        damien_hirst.right(90)
        damien_hirst.forward(spacing)
        damien_hirst.left(90)
        
create_table(rows,cols)

screen = Screen()
screen.exitonclick()
