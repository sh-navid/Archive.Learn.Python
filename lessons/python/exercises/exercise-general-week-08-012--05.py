from tkinter import *

win = Tk()
canvas = Canvas(win)
canvas.pack()

D = {
    1: {"name": "Name1", "last": "Last Name1"},
    2: {"name": "Name2", "last": "Last Name2"},
    3: {"name": "Name3", "last": "Last Name3"},
    4: {"name": "Name4", "last": "Last Name4"},
}

t, o, size = 10, 40, 200
for i in D.keys():
    # ----------------------------------------------------
    top = t+(o*(i-1))
    btm = top+o
    o2 = o/2
    # ----------------------------------------------------
    canvas.create_line(0, top, size, top)
    canvas.create_line(0, btm, size, btm)
    canvas.create_line(size, btm, size+o2, top+o2)
    canvas.create_line(size+o2, top+o2, size+1000, top+o2)
    canvas.create_line(size+o2, top+o2, size, top)
    # ----------------------------------------------------
    canvas.create_text(10, top+o/2, text=i)
    canvas.create_text(40, top+o/2, text=D[i]["name"])
    canvas.create_text(120, top+o/2, text=D[i]["last"])
    # ----------------------------------------------------

win.mainloop()
