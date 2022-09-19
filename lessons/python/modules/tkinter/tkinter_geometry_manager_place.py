from tkinter import *

window = Tk()
window.title("Place")

btn1 = Button(window, text="Center Btn")
btn1.place(anchor="center", relwidth=0.5, relheight=0.3, relx=0.5, rely=0.5)

btn2 = Button(window, text="NW Btn")
btn2.place(bordermode="outside", anchor="nw", x=10, y=10, width=100, height=30)

window.mainloop()
