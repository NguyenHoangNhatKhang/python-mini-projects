import turtle 
import pandas
screen = turtle.Screen()
screen.title("US.States Game")
img = "./50_states/blank_states_img.gif"
screen.addshape(img)
t = turtle.Turtle(img)


# def get_x_y(x,y):
#     print(x,y)

# screen.onscreenclick(get_x_y)
def game_over():
    g = turtle.Turtle()
    g.color("black")
    g.hideturtle()
    g.write(f"GAME OVER! You have {correct_ans} correct answers",align="center",font=("Arial",20,"normal"))
    g.penup()
    g.goto(0,0)
data = pandas.read_csv("./50_states/50_states.csv")
all_states = data.state.to_list()
guessed_states = []
correct_ans = 0
while len(guessed_states) <50: 
# def list_converted(country):
#    print(data[data["state"] == country])
    answer_state = screen.textinput(title=f"{correct_ans}/50 states",prompt="Whats another states name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        game_over()
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break 
    if answer_state in all_states:
        guessed_states.append(answer_state)
        correct_ans += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data["x"].item(),state_data["y"].item())
        t.write(state_data.state.item())
    
    else:  
        break 

turtle.mainloop()
    





























screen.exitonclick()