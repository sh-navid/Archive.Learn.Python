from enum import Enum, auto

# THIS IS NOT THE BEST PRACTICE
# THIS IS JUST FOR TEACHING


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


class Brand(Enum):
    BRAND_A = auto()
    BRAND_B = auto()
    BRAND_C = auto()
    BRAND_D = auto()
    BRAND_E = auto()
    UNDEFINED = auto()


class Reflect:
    def __str__(self) -> str:
        V=vars(self)

    def __repr__(self) -> str:
        return self.__str__()


class Cloth:
    name = ""
    brand: Brand


class Skirt(Cloth):
    name = "Skirt"


class Hat(Cloth):
    name = "Hat"


class Pants(Cloth):
    name = "Pants"


class Coat(Cloth):
    name = "Coat"


class Variant:
    size: Size
    color: Color


class Product:
    cloth: Cloth
    variant: Variant


class Products:
    collection: list(Product)

    @classmethod
    def add(cls, name: str, size: list[Size], brand: Brand, color: Color, count: int):
        cloth
