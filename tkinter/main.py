
# from tkinter import *
# window = Tk()
# window.title("My first GUI program")
# window.minsize(width=500,height=300)

# #label
# my_label = Label(text="I am a label",font=("Arial",24,"bold"))
# my_label.pack(side="left")

# my_label["text"] = "centerrrr"

# #button 
# def button_clicked():
#     print("i got clicked")
#     new_text = input.get()
#     my_label.config(text=new_text)
#     # my_label.config(text=input.get())

# button = Button(text="click me",command=button_clicked)
# button.pack()

# #entry 
# input = Entry(width=10)
# input.pack()
# window.mainloop()



# #pack khó căn chỉnh ở vị chí chính xác

# #  place chính xác cao corr
# #  and grid dùng cột hàng 

from tkinter import *
window = Tk()
window.title("My first GUI")
window.minsize(width=800,height=500)

# window.config(padx=100,pady=200)

my_label = Label(text="HÔM NAY TÔI BUỒN")
my_label.grid(row=0,column=0)
my_label.config(padx=20,pady=20)

user_input = Entry(width=30)
user_input.grid(row=2,column=3)
def got_clicked():
    my_label["text"] = user_input.get()
my_button = Button(text="Click",command=got_clicked)
my_button.grid(row=1,column=1)
def got_clickeda():
    print("i got clicked")
new_button = Button(text="Testing button",command=got_clickeda)
new_button.grid(row=0,column=2)

window.mainloop()

# label 
