phone_numbers = []

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# منطق، کلاس و مدل یک دفترچه تلفن در ساده ترین حالت ممکن را در نظر بگیرید

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# تمرین ۱
# این کلاس را به گونه ای تغییر دهید که علاوه بر نام، نام خانوادگی نیز
# قبول کند
class PhoneNumber:
    def __init__(self, name: str, number: str) -> None:
        self.name = name
        self.number = number

    def __str__(self) -> str:
        return f"{self.name} -> {self.number}"

    def __repr__(self) -> str:  # To print list as string
        return self.__str__()


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# تمرین ۲
# در موارد زیر علاوه بر نام و شماره تلفن، نام خانوادگی نیز وارد کنید
phone_numbers.append(PhoneNumber("Hamid", "00-001"))
phone_numbers.append(PhoneNumber("Saeed", "01-002"))
phone_numbers.append(PhoneNumber("Majid", "02-003"))
phone_numbers.append(PhoneNumber("Navid", "03-004"))
phone_numbers.append(PhoneNumber("David", "04-005"))
phone_numbers.append(PhoneNumber("Farid", "05-006"))


print(phone_numbers)


from sys import path
with open(f"{path[0]}/saved-phone-numbers.txt", "w") as file:
    file.write(str(phone_numbers))