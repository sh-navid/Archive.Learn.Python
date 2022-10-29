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


class Brand(Enum):
    BRAND_A = auto()
    BRAND_B = auto()
    BRAND_C = auto()
    BRAND_D = auto()
    BRAND_E = auto()
    UNDEFINED = auto()


class Cloth:
    name=""
    size: Size
    brand: Brand


class Skirt(Cloth):
    name="Skirt"


class Hat(Cloth):
    name="Hat"


class Pants(Cloth):
    name="Pants"


class Coat(Cloth):
    name="Coat"


class Product:
    cloth: Cloth
    count: int
    color: Color


class Products:
    collection:list(Product)
