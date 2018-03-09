from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x400")
root.title("GUI Application")
def helloCallBack():
    msg = messagebox.showinfo("Vineel Application", "Hello vineel, this is your first GUI application")
B = Button(root, text = "Hello", command=helloCallBack)
B.place(x = 180, y = 100)

