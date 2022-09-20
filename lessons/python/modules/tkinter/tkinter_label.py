from tkinter import *


BACK_COLOR = "#1e1e1e"
FORE_COLOR = "#fefefe"


window = Tk()
window.title("Label")
window.geometry("250x150")
window.config(background=BACK_COLOR)


lbl = Label(window, text="Label")
lbl.config(background=BACK_COLOR)
lbl.config(foreground=FORE_COLOR)
lbl.place(x=40, y=40, width=250 - 80, height=150 - 80)


window.mainloop()
