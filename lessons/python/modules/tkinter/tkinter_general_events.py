from tkinter import *

window = Tk()
window.geometry("400x200")

Label(text="Move mouse inside screen\nOR\nChange position or size of screen").pack()
L = Label(text="Nothing")
L.pack(fill="both", expand=True)


def call(ev, name):
    L.config(text=f"{name}\nxr:{ev.x_root}, yr:{ev.y_root}, x:{ev.x}, y:{ev.y}")


window.bind("<Enter>", lambda ev: call(ev, "Enter"))
window.bind("<Leave>", lambda ev: call(ev, "Leave"))
window.bind("<FocusIn>", lambda ev: call(ev, "FocusIn"))
window.bind("<FocusOut>", lambda ev: call(ev, "FocusOut"))

window.bind("<Configure>", lambda ev: print("Configured", ev))

window.mainloop()
