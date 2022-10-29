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


class Type(Enum):
    UNDEFINED= auto()
    COAT= auto()
    PANTS= auto()
    SKIRT= auto()
    SHIRT= auto()
    HAT= auto()


class Reflector:
    def __str__(self) -> str:
        V = dir(self)
        S = ""
        for v in V:
            if not v.startswith("__"):
                S += f"{self.__getattribute__(v)}, "
        return f"[{S[:-2] if len(S)>=2 else S}]"

    def __repr__(self) -> str:
        return self.__str__()


class Cloth(Reflector):
    name = ""
    type: Type

    def __init__(self, name: str, type: Type) -> None:
        super().__init__()
        self.name = name
        self.type = type


class Variant(Reflector):
    size: Size
    color: Color

    def __init__(self, size: Size, color: Color) -> None:
        super().__init__()
        self.size = size
        self.color = color


class Product(Reflector):
    cloth: Cloth
    variant: Variant
    brand: Brand

    def __init__(self, brand: Brand, cloth: Cloth, variant: Color) -> None:
        super().__init__()
        self.brand = brand
        self.cloth = cloth
        self.variant = variant


V = {
    1001: Variant(Size.FREE_SIZE, Color.BLACK),
    1002: Variant(Size.FREE_SIZE, Color.GRAY),
    1003: Variant(Size.MEDIUM, Color.BLACK),
    1004: Variant(Size.MEDIUM, Color.BLUE),
    1005: Variant(Size.X_LARGE, Color.MULTICOLOR),
    1006: Variant(Size.X_SMALL, Color.MULTICOLOR),
}


C = {
    2001: Cloth("Round", Type.HAT),
    2002: Cloth("Cowboy", Type.HAT),
    2003: Cloth("Cap", Type.HAT),
    2004: Cloth("Long", Type.SHIRT),
    2005: Cloth("Long", Type.SKIRT),
}


L = [
    Product(Brand.BRAND_A, C[2003], V[1003]),
    Product(Brand.BRAND_A, C[2003], V[1004]),
    Product(Brand.BRAND_B, C[2004], V[1003]),
    Product(Brand.BRAND_B, C[2005], V[1003]),
    Product(Brand.BRAND_C, C[2004], V[1005]),
    Product(Brand.BRAND_C, C[2005], V[1006]),
]


for product in L:
    print(product)
