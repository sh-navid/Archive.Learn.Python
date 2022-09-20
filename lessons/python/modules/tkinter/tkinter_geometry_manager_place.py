from tkinter import *

BACK_COLOR = "#1e1e1e"
FORE_COLOR = "#fefefe"

window = Tk()
window.title("Place")
window.config(background=BACK_COLOR)


btn1 = Button(window, text="Center Btn", background=BACK_COLOR, foreground=FORE_COLOR)
btn1.place(anchor="center", relwidth=0.5, relheight=0.3, relx=0.5, rely=0.5)


btn2 = Button(window, text="NW Btn", background=BACK_COLOR, foreground=FORE_COLOR)
btn2.place(bordermode="outside", anchor="nw", x=10, y=10, width=100, height=30)


window.mainloop()
