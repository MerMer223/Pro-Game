from tkinter import *
from tkinter.ttk import *
import time


top = Tk()

top.title("Progress")

top.geometry("450x450")

top.config(background="white")

Progress = Progressbar(top,orient=HORIZONTAL,length = 100)
def update():
    Progress["value"] = 10
   # top.update_idletasks()
    time.sleep(1)
    Progress["value"] = 15
    top.update_idletasks()
    time.sleep(1)
    Progress["value"] = 30
    top.update_idletasks()
    time.sleep(1)
    Progress["value"] = 40
    top.update_idletasks()
    time.sleep(1)
    Progress["value"] = 45
    top.update_idletasks()
    time.sleep(1)
    Progress["value"] = 70
    top.update_idletasks()
    time.sleep(1)
    Progress["value"] = 80
    top.update_idletasks()
    time.sleep(1)
    Progress["value"] = 100

Progress.pack()
Start = Button(top,text="Start",command=update)
Start.pack()

spinbox = Spinbox(top,from_= 0, to = 100)
spinbox.pack()


top.mainloop()