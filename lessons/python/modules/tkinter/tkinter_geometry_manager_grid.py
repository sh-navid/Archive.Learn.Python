from tkinter import *

BACK_COLOR = "#1e1e1e"
FORE_COLOR = "#fefefe"

window = Tk()
window.title("Grid")
window.config(background=BACK_COLOR)

b1 = Button(text="B1", background=BACK_COLOR, foreground=FORE_COLOR)
b2 = Button(text="B2", background=BACK_COLOR, foreground=FORE_COLOR)
b3 = Button(text="B3", background=BACK_COLOR, foreground=FORE_COLOR, width=9)
b4 = Button(text="B4", background=BACK_COLOR, foreground=FORE_COLOR)
b5 = Button(text="B5", background=BACK_COLOR, foreground=FORE_COLOR)
b6 = Button(text="B6", background=BACK_COLOR, foreground=FORE_COLOR)
b7 = Button(text="B7", background=BACK_COLOR, foreground=FORE_COLOR)

b1.grid(row=1, column=1, columnspan=3, ipadx=8, ipady=8)

b2.grid(row=2, column=1)
b3.grid(row=2, column=2)
b4.grid(row=2, column=3)

b5.grid(row=3, column=1, columnspan=4, padx=10, pady=10)
b6.grid(row=4, column=1, columnspan=4, padx=10, pady=10, sticky="ew")

b7.grid(row=0, column=0, rowspan=6, padx=10, pady=10, sticky="ns")

window.mainloop()
