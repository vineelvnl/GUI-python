from tkinter import *
import tkinter

top = Tk()
top.title("Second semester subjects")

listbox = Listbox(top)
listbox.insert(1, "1. Ap22")
listbox.insert(2, "2. AN")
listbox.insert(3, "3. Ap.tech")
listbox.insert(4, "4. DSS")
listbox.insert(5, "5. DBMS")


listbox.pack()
top.mainloop()
