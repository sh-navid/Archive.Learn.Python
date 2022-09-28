from tkinter import *

window = Tk()
window.geometry("300x200")

L = Label(text="Nothing")
L.pack(fill="both", expand=True)

window.bind("<Button-1>", lambda ev: L.config(text="Button 1 - Mouse Left Key Down"))
window.bind("<Button-2>", lambda ev: L.config(text="Button 2 - Mouse Wheel Click"))
window.bind("<Button-3>", lambda ev: L.config(text="Button 3 - Mouse Right Key Down"))
window.bind("<Button-4>", lambda ev: L.config(text="Button 4 - Mouse Wheel Up"))
window.bind("<Button-5>", lambda ev: L.config(text="Button 5 - Mouse Wheel Down"))

window.bind("<Double-Button-1>", lambda ev: L.config(text="Double Button 1 - Mouse Left Key Down"))
window.bind("<Double-Button-2>", lambda ev: L.config(text="Double Button 2 - Mouse Wheel Click"))
window.bind("<Double-Button-3>", lambda ev: L.config(text="Double Button 3 - Mouse Right Key Down"))
window.bind("<Double-Button-4>", lambda ev: L.config(text="Double Button 4 - Mouse Wheel Up"))
window.bind("<Double-Button-5>", lambda ev: L.config(text="Double Button 5 - Mouse Wheel Down"))

window.bind("<ButtonRelease-1>", lambda ev: L.config(text="Button Release 1 - Mouse Left Key Down"))
window.bind("<ButtonRelease-2>", lambda ev: L.config(text="Button Release 2 - Mouse Wheel Click"))
window.bind("<ButtonRelease-3>", lambda ev: L.config(text="Button Release 3 - Mouse Right Key Down"))
window.bind("<ButtonRelease-4>", lambda ev: L.config(text="Button Release 4 - Mouse Wheel Up"))
window.bind("<ButtonRelease-5>", lambda ev: L.config(text="Button Release 5 - Mouse Wheel Down"))

window.mainloop()
