# Scape Chars

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# \'    Single Quote
# \\    Backslash

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# \t    Tab
print("Tab")
print("\tTab")
print("\t\tTab")
print("\t\t\tTab")
"""
Tab
	Tab
		Tab
			Tab
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# \r    Carriage Return
# TODO: important to run this example with terminal (CMD)
print("Hello World\rGoodbye World")

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# \n    New Line
print("Hello\nWorld")

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# \b    Back Space
# TODO: important to run this example with terminal (CMD)
print("Hello\b\b\b is a good cat")

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# \f    Form Feed: Go to next page for printers

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# \ooo  Octal: ooo is 3 numbers
# \xhh  Hexadecimal
s = "ABCDEFG"
for ch in s:
    o = ord(ch)
    print(ch, o, hex(o), oct(o), bin(o))
"""
BASE    10      16          8           2
A       65      0x41        0o101       0b1000001
B       66      0x42        0o102       0b1000010
C       67      0x43        0o103       0b1000011
D       68      0x44        0o104       0b1000100
E       69      0x45        0o105       0b1000101
F       70      0x46        0o106       0b1000110
G       71      0x47        0o107       0b1000111
"""
print("\101\101\101\103")
print("\x43\x43\x43\x42")
"""
AAAC
CCCB
"""

# hex -> base 16
# 41 hex = ? decimal
# 4 * (16 ** 1) + 1 * (16 ** 0) => 4 * 16 + 1 * 1 => 64 + 1 => 65
