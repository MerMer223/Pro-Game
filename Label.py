from tkinter import *

top = Tk()

top.title("log in")

top.geometry("450x450")

top.config(background="black")

Username = Label(top,text="Username").place(x=20,y=100)

Password = Label(top,text="Password").place(x=20,y=150)

Username_entry = Entry(top,width=30).place(x=100,y=100)

Password_entry = Entry(top,width=30,show="*").place(x=100,y=150)

Submit = Button(top,text="Submit",command=top.destroy).place(x=35,y=200)



top.mainloop()