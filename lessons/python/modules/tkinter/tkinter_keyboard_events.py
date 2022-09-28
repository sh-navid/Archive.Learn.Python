from tkinter import *

window = Tk()
window.geometry("400x200")

L = Label(text="Press a Key")
L.pack(fill="both", expand=True)


def call(ev: Event, name):
    # L.config(text=f"{name}\nxr:{ev.x_root}, yr:{ev.y_root}, x:{ev.x}, y:{ev.y}")
    L.config(
        text=f"{name}\nKey Code:{ev.keycode}, Key Symbol:{ev.keysym}, Char Code:{ev.keysym_num}"
    )


window.bind("1", lambda ev: call(ev, "1"))
window.bind("R", lambda ev: call(ev, "R"))
window.bind("r", lambda ev: call(ev, "r"))
window.bind("<Key>", lambda ev: call(ev, "Key"))
window.bind("<space>", lambda ev: call(ev, "Space"))

window.bind("<Shift-Up>", lambda ev: call(ev, "Shift-Up"))
window.bind("<Shift-Down>", lambda ev: call(ev, "Shift-Down"))

window.bind("<Shift-A>", lambda ev: call(ev, "Shift-A"))
window.bind("<Alt-Shift-B>", lambda ev: call(ev, "Alt-Shift-B"))
window.bind("<Control-Shift-A>", lambda ev: call(ev, "Control-Shift-A"))
window.bind("<Control-Alt-Shift-X>", lambda ev: call(ev, "Control-Alt-Shift-X"))


window.mainloop()
