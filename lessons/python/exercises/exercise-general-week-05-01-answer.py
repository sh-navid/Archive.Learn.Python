from tkinter import *
from tkinter import messagebox

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer 1 <-----

my_dictionary = {
    "red": "قرمز",
    "blue": "آبی",
    "green": "سبز",
    "black": "مشکی",
    "white": "سفید",
    "yellow": "زرد",
    "orange": "نارنجی",
    "gray": "خاکستری",
    "pink": "صورتی",
    "silver": "نقره ای",
    "gold": "طلایی",
}

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer 3 Part 1 <-----
def clear_text(txt):
    txt = txt.replace("آ","ا")
    return txt

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer 2 <-----

_ = {}
for k, v in my_dictionary.items():
    _[v] = clear_text(k)
my_dictionary = _.copy()
del _
print(my_dictionary)

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer 3 Part 2 <-----
my_dictionary["سیاه"] = "black" 

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def translate():
    word = txt.get().strip().lower()
    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Answer 3 <-----
    word = clear_text(word)  
    if word in my_dictionary.keys():
        lbl.config(text=my_dictionary[word])
    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Answer 4,5 <-----
    else:
        lbl.config(text="موجود نیست")
        messagebox.showinfo("دیکشنری","موجود نیست")
    print(word)

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
win = Tk()
win.title("نرم افزار دیکشنری")
win.geometry("350x100")

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
txt = Entry(win)
txt.pack()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
lbl = Label(win, text="معنا")
lbl.pack()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
btn = Button(win, text="ترجمه", command=translate)
btn.pack()

win.mainloop()
