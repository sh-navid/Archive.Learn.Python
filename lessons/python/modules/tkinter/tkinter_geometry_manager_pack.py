from tkinter import *


BACK_COLOR = "#1e1e1e"
FORE_COLOR = "#fefefe"


window = Tk()
window.title("Pack")
window.geometry("250x150")
window.config(background=BACK_COLOR)


lbl = Label(window, text="Label 1")
lbl.config(background=BACK_COLOR)
lbl.config(foreground=FORE_COLOR)
lbl.pack(expand=True, fill="both")


btn = Button(window, text="Button 1")
btn.config(background=BACK_COLOR)
btn.config(foreground=FORE_COLOR)
btn.pack(side="right", anchor="s", padx=8, pady=6, ipadx=5, ipady=5)


btn2 = Button(window, text="Button 2")
btn2.config(background=BACK_COLOR)
btn2.config(foreground=FORE_COLOR)
btn2.pack(side="right", anchor="s", pady=6, ipadx=5, ipady=5)


window.mainloop()
