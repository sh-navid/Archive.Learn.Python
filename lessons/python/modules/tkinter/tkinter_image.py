from sys import path
from tkinter import *
from PIL import Image, ImageTk


BACK_COLOR = "#1e1e1e"
FORE_COLOR = "#fefefe"


window = Tk()
window.title("Image")
window.geometry("250x215")
window.config(background=BACK_COLOR)


image1 = Image.open(path[0] + "/tkinter_image_happy.png")
image2 = Image.open(path[0] + "/tkinter_image_sad.png")


photo = ImageTk.PhotoImage(image1)
label = Label(image=photo)
label.pack()


def change_image_to_sad():
    global photo
    photo = ImageTk.PhotoImage(image2)
    label.config(image=photo)


def change_image_to_happy():
    global photo
    photo = ImageTk.PhotoImage(image1)
    label.config(image=photo)


btn1 = Button(text="happy", command=change_image_to_happy)
btn1.config(background=BACK_COLOR, foreground=FORE_COLOR)
btn1.pack(fill="x", expand=True)


btn2 = Button(text="sad", command=change_image_to_sad)
btn2.config(background=BACK_COLOR, foreground=FORE_COLOR)
btn2.pack(fill="x", expand=True)


window.mainloop()
