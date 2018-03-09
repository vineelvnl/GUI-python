from tkinter import *
from tkinter import messagebox

top =Tk()
top.geometry("500x500")
top.title("GUI CANVAS APPLICATION")
#create canves widget
C = Canvas(top, bg="Black", cursor="arrow",height=250, width=350)
#create arc item
coord=50,90,240,210
arc=C.create_arc(coord, start=0, extent=180, fill="yellow")
#create line item
lne = C.create_line(10,10,200,200, fill="white")
C.place(x=200,y=150)
C.pack()
top.mainloop()
