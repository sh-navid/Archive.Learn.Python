from tkinter import *

window = Tk()
window.geometry("400x200")

L = Label(text="Move your mouse")
L.pack(fill="both", expand=True)


def call(ev, name):
    L.config(text=f"{name}\nxr:{ev.x_root}, yr:{ev.y_root}, x:{ev.x}, y:{ev.y}")


window.bind("<Motion>", lambda ev: call(ev, "Motion"))
window.bind("<B1-Motion>", lambda ev: call(ev, "B1-Motion"))
window.bind("<B2-Motion>", lambda ev: call(ev, "B2-Motion"))
window.bind("<B3-Motion>", lambda ev: call(ev, "B3-Motion"))

window.mainloop()
