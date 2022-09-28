from enum import Enum
import sys


class Gender(Enum):
    NOT_GENDER_SPECIFIC = "~"
    GIRL = "G"
    BOY = "B"


class Frequency(Enum):
    RARE = "R"
    NORMAL = "N"
    FREQUENT = "F"


class BabyName:
    name = None
    gender = Gender.NOT_GENDER_SPECIFIC
    frequency = Frequency.FREQUENT
    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Answer 2 <-----
    is_persian = True

    def __init__(
        self, name: str, gender: Gender, frequency: Frequency, is_persian=True
    ):
        self.name = name
        self.gender = gender
        self.frequency = frequency
        self.is_persian = is_persian

    def __str__(self) -> str:
        name = self.name.ljust(12)
        gender = self.gender.name.ljust(5)
        persian = "Persian" if self.is_persian else "Not Persian"
        return f"{self.frequency.value} - {name} > {gender} {persian}"

    def __repr__(self) -> str:
        return self.__str__()


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer 1 <-----
baby_names = []
baby_names.append(BabyName("Saeed", Gender.BOY, Frequency.NORMAL))
baby_names.append(BabyName("Maryam", Gender.GIRL, Frequency.NORMAL))
baby_names.append(BabyName("Ali", Gender.BOY, Frequency.FREQUENT))
baby_names.append(BabyName("Rostam", Gender.BOY, Frequency.RARE))
baby_names.append(BabyName("David", Gender.BOY, Frequency.FREQUENT, is_persian=False))
baby_names.append(BabyName("Mahshid", Gender.GIRL, Frequency.FREQUENT))


# for baby_name in baby_names:
#     print(baby_name)

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer 3 <-----
L, c = len(baby_names), 0
while c < L:
    print(baby_names[c])
    c += 1

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer 4 <-----
with open(sys.path[0] + "/temp.txt", "w") as file:
    file.write(str(baby_names))
