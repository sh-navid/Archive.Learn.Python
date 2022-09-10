from tkinter import *


def open_custom_dialog():
    dialog = Toplevel(window)
    txt = Entry(dialog)
    txt.pack()

    def send_value_and_close_dialog():
        lbl.config(text=txt.get())
        dialog.destroy()

    Button(dialog, text="Done", command=send_value_and_close_dialog).pack()


window = Tk()
lbl = Label(window, text="Nothing")
lbl.pack()
Button(window, text="Open Dialog", command=open_custom_dialog).pack()
window.mainloop()
