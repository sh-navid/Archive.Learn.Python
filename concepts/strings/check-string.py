# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
s1 = "HEllo"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(s1.istitle())
# False

print(s1.islower())
# False

print(s1.isupper())
# False

print(s1.isspace())
# False


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TAB = 14
print(
    "\n\n\n\tisalnum\tisnumeric\tisdigit\tisdecimal\tisalpha\tisascii".expandtabs(
        TAB)
)


def check_numeric(inp: str):
    print(
        "{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
            inp,
            inp.isalnum(),
            inp.isnumeric(),
            inp.isdigit(),
            inp.isdecimal(),
            inp.isalpha(),
            inp.isascii(),
        ).expandtabs(TAB)
    )


check_numeric("2")
check_numeric("2.1")
check_numeric("2e10")
check_numeric("ↁ")  # Roman Number
check_numeric("⅔")  # Fraction
check_numeric("2²")  # Superscript
check_numeric("\u00B2")
check_numeric("A")
check_numeric("ب")

print(s1.isprintable())
print(s1.isidentifier())


print(s1.isascii())
print(s1.isalpha())
