from tkinter.colorchooser import askcolor
from tkinter import *

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
x, y = None, None
selected_color = "#ffffff"
FORE_COLOR = "#fefefe"
BACK_COLOR = "#1e1e1e"

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def mouse_click(e):
    global x, y
    x, y = e.x, e.y


def mouse_move(e):
    global x, y
    boom.create_line(x, y, e.x, e.y, width=15, fill=selected_color)
    x, y = e.x, e.y


def open_color_palette():
    global selected_color
    selected_color = askcolor()[1]


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
window = Tk()
window.title("Simple Paint")
window.config(bg=BACK_COLOR)

lbl = Label(window, text="Draw on Screen")
lbl.config(bg=BACK_COLOR)
lbl.config(foreground=FORE_COLOR)
lbl.pack()

boom = Canvas(width=500, height=500)
boom.config(bg=BACK_COLOR)
boom.config(borderwidth=0)
boom.config(highlightthickness=0)
boom.pack()

btn_color = Button(window, text="Change Color", command=open_color_palette)
btn_color.config(bg=BACK_COLOR)
btn_color.config(foreground=FORE_COLOR)
btn_color.pack()


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
window.bind("<ButtonPress-1>", mouse_click)
window.bind("<B1-Motion>", mouse_move)

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
window.mainloop()
