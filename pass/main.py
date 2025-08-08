
from tkinter import * 
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []
def random_pass():
    password_list.extend(random.choice(letters) for _ in range(nr_letters))
    password_list.extend(random.choice(symbols) for _ in range(nr_symbols))
    password_list.extend(random.choice(numbers) for _ in range(nr_numbers))
    random.shuffle(password_list)
    # password = ""
    # for char in password_list:
    #     password += char
    password = "".join(password_list)
    en3.delete(0,END)
    en3.insert(0,password)
    pyperclip.copy(f"{password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web = en1.get()
    email = en2.get()
    pas = en3.get()
    if len(web) == 0 or len(pas) == 0 or len(email) == 0:
        warning = messagebox.showwarning(title="Warning!",message="Your Entries are empty")
        return warning
    is_okay = messagebox.askokcancel(title=web,message=f"These are the details:\nEmail: {email}\nPassword: {pas}\nIs it okay to save?")
    if is_okay:
        with open("./pass/data.txt","a") as file:
            file.write(f"{web} | {email} | {pas}\n")
            en1.delete(0,END)
            en3.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #


window =Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
canvas = Canvas(height=200,width=200)
image = PhotoImage(file="./pass/logo.png")
canvas.create_image(100,100,image=image)
canvas.grid(row=0,column=1)



# label 
lb1 = Label(text="Website:")
lb1.grid(row=1,column=0)
lb2 = Label(text="Email/Username:")
lb2.grid(row=2,column=0)
lb3 = Label(text="Password")
lb3.grid(row=3,column=0)
# but
but1 = Button(text="Generate Password",command=random_pass)
but1.grid(row=3,column=2)
but2 = Button(text="Add",width=36,command=save)
but2.grid(column=1,row=4,columnspan=2)
# entry
en1 = Entry(width=35)
en1.grid(row=1,column=1,columnspan=2)
en1.focus()
en2 = Entry(width=35)
en2.grid(row=2,column=1,columnspan=2) 
en2.insert(0,"kelvin@gmail.com")
en3 = Entry(width=17)
en3.grid(row=3,column=1) 
window.mainloop()