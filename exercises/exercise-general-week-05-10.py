from enum import Enum

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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
    name_is_for = Gender.NOT_GENDER_SPECIFIC
    frequency = Frequency.FREQUENT

    def __init__(self, name: str, name_is_for: Gender, frequency: Frequency) -> None:
        self.name = name
        self.name_is_for = name_is_for
        self.frequency = frequency

    def __str__(self) -> str:
        name = self.name.ljust(12)
        gender = self.name_is_for.name.ljust(5)
        return f"{self.frequency.value} - {name} > {gender}"


baby_names = []

baby_names.append(BabyName("Saeed", Gender.BOY, Frequency.NORMAL))
baby_names.append(BabyName("Maryam", Gender.GIRL, Frequency.NORMAL))
baby_names.append(BabyName("Ali", Gender.BOY, Frequency.FREQUENT))
baby_names.append(BabyName("Rostam", Gender.BOY, Frequency.RARE))

for baby_name in baby_names:
    print(baby_name)
