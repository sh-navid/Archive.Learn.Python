from enum import Enum
from math import floor

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Color(Enum):
    RED = 1
    BLUE = 4
    GRAY = 0
    GREEN = 2
    WHITE = 7
    YELLOW = 3
    MAGENTA = 5
    LIGHTBLUE = 6

    @staticmethod
    def set(color: Enum):
        print(f"\033[9{color.value}m", end="")


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def line():
    Color.set(Color.RED)
    print("-" * N)


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
fruit_data = [
    {"id": 1, "character": "A", "name": "Apple"},
    {"id": 2, "character": "O", "name": "Orange"},
    {"id": 3, "character": "K", "name": "Kiwy"},
    {"id": 4, "character": "G", "name": "Grapes"},
    {"id": 5, "character": "P", "name": "Peach"},
]

N, FL, KEYS = 70, floor(70 / 3), fruit_data[0].keys()

line()

for title in KEYS:
    Color.set(Color.RED)
    print("|", end="")
    Color.set(Color.GRAY)
    print(f"{title}".upper().center(FL - 1), end="")
Color.set(Color.RED)
print("|")

line()
Color.set(Color.GREEN)
for entity in fruit_data:
    for key in KEYS:
        print((" " + f"{entity[key]}".capitalize()).ljust(FL), end="")
    print()

line()


"""
----------------------------------------------------------------------
|          ID          |      CHARACTER       |         NAME         |
----------------------------------------------------------------------
 1                      A                      Apple                 
 2                      O                      Orange                
 3                      K                      Kiwy                  
 4                      G                      Grapes                
 5                      P                      Peach                 
----------------------------------------------------------------------
"""