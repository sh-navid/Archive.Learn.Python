from tkinter import *

window = Tk()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
window.geometry("250x110")
window.title("نرم افزار تشخیص نام رنگ")

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
entry = Entry()
entry.place(x=10, y=15, width=230)

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
colors = ("red", "green", "blue", "orange", "yellow", "white", "black")
farsi = ("قرمز", "سبز", "آبی", "نارنجی", "زرد", "سفید", "مشکی")
# این نسخه از نرم افزار علاوه بر رنگ های انگلیسی، رنگ های فارسی را
# نیز تشخیص میدهد
# سوال؟
# اگر فردی رنگ "سیاه" را وارد کند چه میشود؟
# اگر فردی بجای "آبی" مقدار "ابی" را وارد کند چه میشود؟
# راه حل؟
# اگر بخواهیم به لیست رنگ صورتی اضافه کنیم؟
# راه حل؟

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def check_color():
    color_name = entry.get()
    print(color_name)

    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # میتوانید تصور کنید در این قسمت برنامه چه اتفاقی می افتد؟
    color_name = color_name.replace("ي", "ی")
    color_name = color_name.replace("ا", "آ")

    if color_name.lower() in colors:
        label.config(text="یک رنگ است" + " " + color_name.capitalize())
        label.config(bg=color_name)
    elif color_name in farsi:
        color_index = farsi.index(color_name)
        label.config(text=color_name + " " + "یک رنگ فارسی است")
        label.config(bg=colors[color_index])
    else:
        label.config(text="رنگ مورد نظر قابل تشخیص نیست")
        label.config(bg="white")


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
button = Button()
button.config(text="کلیک کنید")
button.config(command=check_color)
button.place(x=10, y=45, width=230)

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
label = Label()
label.config(text="ابتدا نام رنگ را وارد کنید")
label.place(x=10, y=75, width=230)

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
window.mainloop()
