## pip install matplotlib
## sudo apt install python3-pil.imagetk


##---------------------------------------------------------------------------##
# IMPORTS
from tkinter import *
from tkinter import simpledialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as TkCanvas


##---------------------------------------------------------------------------##
# CONSTANTS
BACK_COLOR = "#1e1e1e"
FORE_COLOR = "#fefefe"


##---------------------------------------------------------------------------##
# MUTABLES
weights = [78, 77, 78, 75, 73, 70]


##---------------------------------------------------------------------------##
# CONFIGURATIONS
plt.style.use("dark_background")


##---------------------------------------------------------------------------##
# Functions
def add():
    weights.append(simpledialog.askfloat("New Weight", "Enter your new weight"))
    clear()
    plot()


canvas: TkCanvas = None
figure: plt.Figure = None


def plot():
    global canvas, figure
    figure = plt.Figure(dpi=100)
    canvas = TkCanvas(figure, window)
    canvas.get_tk_widget().pack(fill="both", expand=True)
    ax = figure.add_subplot()
    ax.plot(["Week " + str(x) for x in range(len(weights))], weights)
    canvas.draw()


def clear():
    global canvas, figure
    canvas.get_tk_widget().pack_forget()
    #del canvas
    del figure


##---------------------------------------------------------------------------##
# APPLICATION
window = Tk()
window.geometry("600x400")
window.title("Weekly Weight App")
window.config(background=BACK_COLOR)


btn = Button(window, text="Add new weight", command=add)
btn.config(background=BACK_COLOR)
btn.config(foreground=FORE_COLOR)
btn.pack()
plot()


##---------------------------------------------------------------------------##
# MAIN LOOP
window.mainloop()
