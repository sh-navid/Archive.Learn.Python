###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# این برنامه یک دفترچه تلفن خیلی ساده برای ترمینال است
# تا این نسخه اطلاعات ذخیره نمیشوند

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# میتوانید بررسی کنید متغیر
# N
# در این برنامه چه کاربردی دارد؟
N = 60
TITLE = "PHONE BOOK"

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# این یک دیکشنری است
# اطلاعات تلفن و نام اشخاص را در این ساختار ذخیره کرده ایم
# به طور پیشفرض دو مقدار در این دیکشنری وجود دارد
# آیا میتوانید یک نام و شماره تلفن دیگر بصورت پیشفرض به این
# برنامه اضافه کنید
phone_book = {
    "00000": "Name0",
    "00001": "Name1",
}

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# هر زمان این تابع صدا زده شود لیست افراد و شماره تلفن آنها
# نمایش داده میشود
def show_list_of_phone_numbers():
    for phone in phone_book:
        name = phone_book[phone]
        print(phone, ":", name)


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# برای سوال از کاربر و افزودن یک شماره تلفن جدید از این تابع
# استفاده میشود
def ask_user_to_enter_a_phone_number():
    answer = input("Enter new number> PHONE,NAME: ")
    if "," in answer:
        (phone, name) = answer.split(",")
        phone_book[phone] = name
        print("Phone added to list successfully")
    else:
        print("Phone and Name are in Wrong Format")


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# برای اینکه بتوانید یک فرد را حذف کنید باید شماره تلفن آن را
# وارد کنید؛ این تابع از کاربر یک شماره تلفن دریافت میکند تا
# بتواند آن را حذف کند
# آیا میتوانید برنامه را به شکلی تغییر دهید که حذف یک فرد بر
# اساس نام آن فرد انجام بگیرد؟
def ask_user_to_enter_a_phone_number_to_remove():
    answer = input("Enter the phone number to REMOVE: ")
    phone_book.pop(answer)


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# برای جستجو باید شماره تلفن یک فرد را وارد کنید؛ این تابع
# از کاربر یک شماره میگیرد و تلاش میکند فرد متناظر با آن شماره
# را حذف کند
# آیا میتوانید برنامه را به شکلی تغییر دهید که جستجو بر اساس
# نام یک فرد صورت بگیرد؟
def ask_user_to_enter_a_phone_number_to_search():
    answer = input("Enter the phone number to SEARCH: ")
    try:
        print(phone_book[answer])
    except:
        print("Cannot find this number")


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("-" * N)
print("|" + TITLE.center(N - 2) + "|")


while True:
    print("-" * N)
    print("|" + "A:Add, L:List, S:Search, R:Remove, Q:Quit".center(N - 2) + "|")
    print("-" * N)

    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # می توانید بررسی کنید در این قسمت چه اتفاقی رخ میدهد؟
    command = input("").upper()
    if command == "A":
        ask_user_to_enter_a_phone_number()
        show_list_of_phone_numbers()
    elif command == "L":
        show_list_of_phone_numbers()
    elif command == "S":
        ask_user_to_enter_a_phone_number_to_search()
    elif command == "R":
        ask_user_to_enter_a_phone_number_to_remove()
    elif command == "Q":
        quit()
