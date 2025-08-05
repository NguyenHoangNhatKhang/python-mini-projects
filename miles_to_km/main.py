from tkinter import * 
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300,height=100)
window.config(padx=20,pady=20)


# label
lb1 = Label(text="is equal to")
lb1.grid(row=2,column=0)
lb2 = Label(text="Miles")
lb2.grid(row=1,column=2)
lb3 = Label(text=str(0))
lb3.grid(row=2,column=1)
lb4 = Label(text="Km")
lb4.grid(row=2,column=2)

# entry 
en1 = Entry(width=5)
en1.grid(row=1,column=1)
# function 
def converter():
    lb3["text"] = f"{int(en1.get()) * 1.60934}"
# button 
but1 = Button(text="Calculate",command=converter)
but1.grid(row=3,column=1)





window.mainloop()