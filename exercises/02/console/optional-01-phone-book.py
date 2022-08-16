N = 60
TITLE = "PHONE BOOK"

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
phone_book = {
    "00000": "Name0",
    "00001": "Name1",
}

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def show_list_of_phone_numbers():
    for phone in phone_book:
        name = phone_book[phone]
        print(phone, ":", name)


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def ask_user_to_enter_a_phone_number():
    answer = input("Enter new number> PHONE,NAME: ")
    if "," in answer:
        (phone, name) = answer.split(",")
        phone_book[phone] = name
        print("Phone added to list successfully")
    else:
        print("Phone and Name are in Wrong Format")


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def ask_user_to_enter_a_phone_number_to_remove():
    answer = input("Enter the phone number to REMOVE: ")
    phone_book.pop(answer)


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
