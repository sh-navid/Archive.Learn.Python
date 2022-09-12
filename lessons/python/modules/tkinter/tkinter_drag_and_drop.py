from tkinter import *
import tkinter


class DragHelper:
    mx, my = None, None

    def __init__(self, entity) -> None:
        self.entity = entity
        entity.bind("<Button-1>", self.start_drag)
        entity.bind("<B1-Motion>", self.move_drag)

    def start_drag(self, event: tkinter.Event):
        self.mx = event.x_root
        self.my = event.y_root

    def move_drag(self, event):
        ex, ey = self.entity.winfo_rootx(), self.entity.winfo_rooty()
        x = event.x_root
        y = event.y_root

        print(">", x, y)
        # x -= self.mx
        # y -= self.my
        # print(x, y)
        self.entity.place(x=x, y=y)


window = Tk()
window.geometry("600x600")

frame = Frame(window, bg="gray", width=100, height=100)
frame.place(x=100, y=100)
DragHelper(frame)

window.mainloop()
