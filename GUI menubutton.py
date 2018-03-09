from tkinter import *
import tkinter

top = Tk()
top.title("select technology")
mb = Menubutton(top, text = "Python webdevlopment", relief = RAISED)
mb.grid()
mb.menu = Menu(mb, tearoff = 0)
mb["menu"] = mb.menu

Django = IntVar()
Flask = IntVar()

mb.menu.add_checkbutton(label = "Django", variable = Django)
mb.menu.add_checkbutton(label = "Flask", variable = Flask)
mb.pack()
top.mainloop()
