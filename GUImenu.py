from tkinter import *
def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()

root = Tk()
menubar = Menu(root)
root.geometry("400x400")
root.title("GUI MENU APPLICATION")
#CREATE COMMAND FOR FILE MENU
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "NEW", command=donothing)
filemenu.add_command(label = "open", command=donothing)
filemenu.add_command(label = "save", command=donothing)
filemenu.add_command(label = "save as", command=donothing)
filemenu.add_command(label = "close", command=donothing)
#add command to exit the file

filemenu.add_command(label = "exit", command=root.quit)

filemenu.add_separator()
menubar.add_cascade(label="FILE", menu=filemenu)
#CREATE COMMAND FOR EDIT MENU
editmenu = Menu(menubar, tearoff = 0)
editmenu.add_command(label = "UNDO", command=donothing)
editmenu.add_command(label = "CUT", command=donothing)
editmenu.add_command(label = "COPY", command=donothing)
editmenu.add_command(label = "PASTE", command=donothing)
editmenu.add_command(label = "DELETE", command=donothing)
editmenu.add_command(label = "SELECT ALL", command=donothing)

editmenu.add_separator()
menubar.add_cascade(label="EDIT", menu=editmenu)
#CREATE COMMAND FOR HELP
helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "FINDMORE..", command=donothing)
helpmenu.add_command(label = "HELP INDEX..", command=donothing)
helpmenu.add_command(label = "ABOUT..", command=donothing)
helpmenu.add_command(label = "HELP", command=donothing)

menubar.add_cascade(label="HELP", menu=helpmenu)
root.config(menu = menubar)
root.mainloop()
