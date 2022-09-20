from cgitb import text
from tkinter import *


BACK_COLOR = "#1e1e1e"
FORE_COLOR = "#fefefe"


window = Tk()
window.title("Entry")
window.geometry("250x150")
window.config(background=BACK_COLOR)


entry = Entry(window)
entry.config(background=BACK_COLOR)
entry.config(foreground=FORE_COLOR)
entry.place(x=40, y=40, width=250 - 80, height=150 - 80)


window.mainloop()
