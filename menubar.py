from tkinter import *

top = Tk()

top.title("Menu")

menu_bar = Menu(top)
#add file menu
File = Menu(menu_bar)
menu_bar.add_cascade(label="File",menu = File)
File.add_command(label="New_File",command=None)
File.add_command(label="Open",command=None)
File.add_command(label="Save",command=None)
File.add_separator()
File.add_command(label="Exit",command=top.destroy)

View = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="View1",menu = View)
View.add_command(label="Share",command=None)
View.add_command(label="Copy",command=None)
View.add_separator()
View.add_command(label="Problems",command=None)



top.config(background = "white")
top.config(menu = menu_bar)
top.mainloop()