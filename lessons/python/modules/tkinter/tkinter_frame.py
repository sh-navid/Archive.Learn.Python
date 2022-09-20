from tkinter import *


BACK_COLOR = "#1e1e1e"
FORE_COLOR = "#fefefe"


window = Tk()
window.title("Frame")
window.geometry("250x150")
window.config(background=BACK_COLOR)


frm = Frame(window)
frm.config(background=FORE_COLOR)
frm.place(x=40, y=40, width=250 - 80, height=150 - 80)


window.mainloop()
