from enum import Enum
from datetime import date, time, datetime

##---------------------------------------------------------------------------##
# 
# 
# 

##---------------------------------------------------------------------------##
class Gender(Enum):
    MALE = "M"
    FEMALE = "F"


##---------------------------------------------------------------------------##
class Person:
    name: str = None
    last: str = None
    gender: Gender = None
    birth: date = None

    def __init__(self, name: str, last: str, gender: Gender, birth: date) -> None:
        self.name = name
        self.last = last
        self.gender = gender
        self.birth = birth

    def __str__(self) -> str:
        return "({}) {} {} {}".format(
            self.gender.value, self.name, self.last, self.birth
        )

    def __repr__(self) -> str:
        return self.__str__()

##---------------------------------------------------------------------------##
# تمرین ۱
# 
# 

##---------------------------------------------------------------------------##
# تمرین ۲
# 
# 

##---------------------------------------------------------------------------##
# تمرین ۳
# 
# 

##---------------------------------------------------------------------------##
class People:
    people = []

    @classmethod
    def add(cls, person: Person):
        cls.people.append(person)

    @classmethod
    def filter(cls, year: int):
        for person in cls.people:
            if person.birth.year > year:
                yield person


##---------------------------------------------------------------------------##
People.add(Person("Kate", "K", Gender.MALE, date(1941, 3, 11)))
People.add(Person("Roz", "R", Gender.FEMALE, date(1982, 2, 15)))
People.add(Person("Kevin", "K", Gender.MALE, date(1985, 9, 16)))
People.add(Person("David", "Hat", Gender.MALE, date(1990, 5, 12)))
People.add(Person("John", "JJ", Gender.FEMALE, date(1971, 11, 13)))


##---------------------------------------------------------------------------##
print(People.people)
print()
for person in People.filter(1950):
    print(person)
