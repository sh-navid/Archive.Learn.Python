from tkinter import *

window = Tk()
window.geometry("300x300")

lbl = Label(window, text="Label 1")
lbl.pack(expand=True, fill="both")

btn = Button(window, text="Button 1")
btn.pack(side="right", anchor="s", padx=8, pady=6, ipadx=5, ipady=5)

btn = Button(window, text="Button 2")
btn.pack(side="right", anchor="s", pady=6, ipadx=5, ipady=5)

window.mainloop()
