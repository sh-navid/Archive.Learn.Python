from enum import Enum


class Type(Enum):
    UNSET = -1
    SHOE = 0
    GLASSES = 1
    COAT = 2


class Color(Enum):
    GREEN = "Green"
    BLUE = "Blue"
    BLACK = "Black"
    UNDEFINED = "Undefined"
    MULTICOLOR = "Multicolor"


class Brand(Enum):
    BrandA = "A"
    BrandB = "B"
    BrandC = "C"
    UNKNOWN = "Unknown"


class Size(Enum):
    SMALL = "S"
    MEDIUM = "M"
    LARGE = "L"
    FREESIZE = "FS"
    UNDEFINED = "U"


D = [
    {"type": Type.SHOE,     "brand": Brand.BrandA,  "size": [45, 46, 47],              "color": [Color.BLACK,Color.MULTICOLOR]},
    {"type": Type.UNSET,    "brand": Brand.UNKNOWN, "size": [46, 48, 50],              "color": [Color.GREEN]},
    {"type": Type.GLASSES,  "brand": Brand.BrandB,  "size": [Size.SMALL,Size.LARGE],   "color": [Color.UNDEFINED]},
    {"type": Type.UNSET,    "brand": Brand.BrandC,  "size": [Size.FREESIZE],           "color": [Color.MULTICOLOR]},
    {"type": Type.COAT,     "brand": Brand.UNKNOWN, "size": [Size.MEDIUM],             "color": [Color.BLACK,Color.BLUE]},
    {"type": Type.COAT,     "brand": Brand.UNKNOWN, "size": [56],                      "color": [Color.UNDEFINED]},
]


print(D)

# تمرین
# لیست و دیکشنریهای بالا را به مجموعه ای با ساختار کلاس تبدیل کنید