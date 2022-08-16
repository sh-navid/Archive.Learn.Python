from tkinter import *

window = Tk()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
window.geometry("250x110")
window.title("نرم افزار تشخیص نام رنگ")

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
entry = Entry()
entry.place(x=10, y=15, width=230)

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
colors = ["red", "green", "blue", "orange", "yellow", "white", "black"]
# این نرم افزار نام رنگ رو به انگلیسی از شما دریافت و در صورتی
# که در لیستش موجود باشه به شما نمایش میده
# آیا میتونید به این لیست چند رنگ دیگر اضافه کنید؟
# آیا نرم افزار با رنگهای جدید شما به خوبی کار میکنه؟
# در مورد کدهای رنگی هگز تحقیق کنید

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def check_color():
    color_name = entry.get()
    print(color_name)

    if color_name.lower() in colors:
        label.config(text="یک رنگ است" + " " + color_name.capitalize())
        label.config(bg=color_name)
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
