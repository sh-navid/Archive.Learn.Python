from enum import Enum, auto


class Size(Enum):
    FREE_SIZE = auto()
    UNDEFUNED = auto()
    X_SMALL = auto()
    SMALL = auto()
    MEDIUM = auto()
    LARGE = auto()
    X_LARGE = auto()


class Color(Enum):
    UNDEFINED = auto()
    MULTICOLOR = auto()
    BLACK = auto()
    BLUE = auto()
    GREEN = auto()
    YELLOW = auto()
    ORANGE = auto()
    PURPLE = auto()
    GRAY = auto()


class BRAND(Enum):
    BRAND_A = auto()
    BRAND_B = auto()
    BRAND_C = auto()
    BRAND_D = auto()
    BRAND_E = auto()
    UNDEFINED = auto()


class Cloth:
    def move(self):
        pass


class Items:
    products: list[Cloth] = []
