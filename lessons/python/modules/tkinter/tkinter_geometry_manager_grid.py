from tkinter import *

window = Tk()

b1 = Button(text="B1")
b2 = Button(text="B2")
b3 = Button(text="B3")
b4 = Button(text="B4")
b5 = Button(text="B5")
b6 = Button(text="B6")
b7 = Button(text="B7")

b1.grid(row=1, column=1, columnspan=3, ipadx=10, ipady=10)

b2.grid(row=2, column=1)
b3.grid(row=2, column=2)
b4.grid(row=2, column=3)

b5.grid(row=3, column=1, columnspan=4, padx=10, pady=10)
b6.grid(row=4, column=1, columnspan=4, padx=10, pady=10, sticky="ew")

b7.grid(row=0, column=0, rowspan=6, padx=10, pady=10, sticky="ns")

window.mainloop()
