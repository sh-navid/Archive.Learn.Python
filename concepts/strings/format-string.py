# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# String format with .format()
print("Format: ", "{} - {}".format("Hello", "World"))
print("Format: ", "{1} - {0}".format("Hello", "World"))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# String format with f""
x = "Goodbye"
print("Format: ", f"{x} my world")
print("Format: ", f"I am {5+5} years old")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Translate and Make Trans
a = "old"
b = "0!&"
s = "Hello World"
print("Translate + MakeTrans: ", s.translate(s.maketrans(a, b)))
