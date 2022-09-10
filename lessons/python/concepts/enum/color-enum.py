from enum import Enum

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


if __name__ == "__main__":
    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print(Color.BLUE, Color.BLUE.value)

    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Color.set(Color.YELLOW)
    print("Text in yellow")

    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Color.set(Color.BLUE)
    print("Text in blue")

    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Color.set(Color.GREEN)
    print("Text in green")

    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Color.set(Color.RED)
    print("Text in red")

    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Color.set(Color.MAGENTA)
    print("Text in magenta")

    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Color.set(Color.WHITE)
    print("Text in white")

    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Color.set(Color.GRAY)
    print("Text in gray")

    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Color.set(Color.LIGHTBLUE)
    print("Text in lightblue")
