import json
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
    new_data = {web:{
        "email": email,
        "password":pas
    }
    }
    if len(web) == 0 or len(pas) == 0 or len(email) == 0:
        warning = messagebox.showwarning(title="Warning!",message="Your Entries are empty")
        return warning
    else:
        try:
            with open("./pass/data.json","r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("./pass/data.json","w") as file:
                json.dump(new_data,file,indent=4)
        else:
            data.update(new_data)
            with open("./pass/data.json","w") as file:
                json.dump(data,file,indent=4)
        finally:
            en1.delete(0,END)
            en3.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
# find password
def find_password():
    web = en1.get()
    try:
        with open("./pass/data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found")
    else:
        if web in data:
                email = data[web]["email"]
                pas = data[web]["password"]
                messagebox.showinfo(title=web,message=f"Email: {email}\nPassword: {pas}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {web} exists.")
window =Tk()
window.title("Password Manager")
window.config(padx=5,pady=5)
window.columnconfigure(1, weight=1)
canvas = Canvas(height=200,width=200)
image = PhotoImage(file="./pass/logo.png")
canvas.create_image(100,100,image=image)
canvas.grid(row=0,column=1)



# label 
lb1 = Label(text="Website:")
lb1.grid(row=1,column=0,sticky="E")
lb2 = Label(text="Email/Username:")
lb2.grid(row=2,column=0, sticky="E")
lb3 = Label(text="Password")
lb3.grid(row=3,column=0, sticky="E")
# but
but1 = Button(text="Generate Password",command=random_pass)
but1.grid(row=3,column=2)
but2 = Button(text="Add",width=35,command=save)
but2.grid(column=1,row=4,columnspan=2,sticky="EW")
but3 = Button(text="Search",command=find_password,width=15)
but3.grid(row=1,column=2)
# entry
en1 = Entry(width=35)
en1.grid(row=1,column=1,sticky="W")
en1.focus()
en2 = Entry(width=35)
en2.grid(row=2,column=1,columnspan=2,sticky="EW") 
en2.insert(0,"kelvin@gmail.com")
en3 = Entry(width=35)
en3.grid(row=3,column=1,sticky="W") 
window.mainloop()