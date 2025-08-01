import pandas 
import turtle 
ENDING_POS = (0,0)
FONT = ("Arial",24,"normal")
screen = turtle.Screen()
image = "./vietnam-provinces/vietnam1.gif"
screen.setup(800,600)
screen.title("VietNam Guessing Game")
screen.addshape(image)
map_turtle = turtle.Turtle()
map_turtle.shape(image)

#lấy tọa độ xy 
# def get_xcor_ycor(x, y):
#     print(f"{int(x)},{int(y)}")

# screen.onscreenclick(get_xcor_ycor)
data = pandas.read_csv("./vietnam-provinces/vietnam_provinces.csv")
# print(data)
# tự in ra thành data frame 
#set correct ans 
correct_ans = 0
#cho data thành list
data_provinces = data.province.tolist()
correct_ans_list = []
# print(data_list)
#generate game over 
def game_over():
    gg = turtle.Turtle()
    gg.hideturtle()
    gg.goto(ENDING_POS)
    gg.write(f"Game Over! {correct_ans}/63 correct!",align="center",font=FONT)

def create_pro():
    pro = turtle.Turtle()
    pro.penup()
    pro.hideturtle()
    pro.goto(province_data.x.item(),province_data.y.item())
    pro.write(ans)
while len(correct_ans_list) < 63:
    ans = screen.textinput(title=f"{correct_ans}/63",prompt="Enter your guess:").title()
    if ans == "Exit":
        game_over()
        break 

    if ans in data_provinces:
        correct_ans_list.append(ans)
        correct_ans += 1 
        province_data = data[data.province == ans]
        pro = turtle.Turtle()
        create_pro()



        


screen.mainloop()