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

#               isalnum       isnumeric     isdigit       isdecimal     isalpha       isascii
# 2             True          True          True          True          False         True
# 2.1           False         False         False         False         False         True
# 2e10          True          False         False         False         False         True
# ↁ             True          True          False         False         False         False
# ⅔             True          True          False         False         False         False
# 2²            True          True          True          False         False         False
# ²             True          True          True          False         False         False
# A             True          False         False         False         True          True
# ب             True          False         False         False         True          False


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(s1.isprintable())
# True

print(s1.isidentifier())
# True

print(s1.isascii())
# True

print(s1.isalpha())
# True
