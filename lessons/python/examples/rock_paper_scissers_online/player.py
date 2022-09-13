from tkinter import *
import random
import urllib3
from threading import Timer

http = urllib3.PoolManager()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PATH = "http://127.0.0.1:4000"


def update():
    resp = http.request("GET", f"{PATH}/update")
    lbl_result.config(text=resp.data)
    Timer(0.25, update).start()


Timer(5, update).start()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
window = Tk()
window.title("")

id = random.randint(1000, 9999)
Label(window, text=str(id)).pack()

lbl_result = Label(window, text="Wait for connection ...",height=10)
lbl_result.pack()


def click(choice):
    resp = http.request("GET", f"{PATH}/play/{id}/{choice}")
    lbl_result.config(text=resp.data)


def reset():
    resp = http.request("GET", f"{PATH}/reset")
    lbl_result.config(text=resp.data)


Button(window, text="[reset]", width=20, command=lambda: reset()).pack()
Button(window, text="rock", width=20, command=lambda: click("rock")).pack()
Button(window, text="paper", width=20, command=lambda: click("paper")).pack()
Button(window, text="scissers", width=20, command=lambda: click("scissers")).pack()

window.mainloop()
