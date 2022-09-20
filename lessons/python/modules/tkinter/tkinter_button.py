from tkinter import *


BACK_COLOR = "#1e1e1e"
FORE_COLOR = "#fefefe"


window = Tk()
window.title("Button")
window.geometry("250x150")
window.config(background=BACK_COLOR)


btn = Button(window, text="Button")
btn.config(background=BACK_COLOR)
btn.config(foreground=FORE_COLOR)
btn.place(x=40, y=40, width=250 - 80, height=150 - 80)


window.mainloop()
