from sys import path

phone_numbers = []

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer 1 <-----
class PhoneNumber:
    def __init__(self, name: str, last: str, number: str) -> None:
        self.name = name
        self.last = last
        self.number = number

    def __str__(self) -> str:
        return f"{self.name} {self.last}: {self.number}"

    def __repr__(self) -> str:
        return self.__str__()


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer 2 <-----
phone_numbers.append(PhoneNumber("Hamid","Family 1","00-001"))
phone_numbers.append(PhoneNumber("Saeed","Family 2","01-002"))
phone_numbers.append(PhoneNumber("Majid","Family 3","02-003"))
phone_numbers.append(PhoneNumber("Navid","Family 4","03-004"))
phone_numbers.append(PhoneNumber("David","Family 5","04-005"))
phone_numbers.append(PhoneNumber("Farid","Family 6","05-006"))


print(phone_numbers)


with open(f"{path[0]}/saved-phone-numbers.txt", "w") as file:
    file.write(str(phone_numbers))
