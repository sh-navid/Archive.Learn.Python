# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# String format with .format()

print("Format: ", "{} - {}".format("Hello", "World"))
# Format:  Hello - World

print("Format: ", "{1} - {0}".format("Hello", "World"))
# Format:  World - Hello


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# String format with f""

x = "Goodbye"
print("Format: ", f"{x} my world")
# Format:  Goodbye my world

print("Format: ", f"I am {5+5} years old")
# Format:  I am 10 years old