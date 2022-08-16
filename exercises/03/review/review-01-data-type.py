print("Hex:", "\x48\x65\x6c\x6c\x6f\x20\x69\x6e\x20\x48\x65\x78")
print("Oct:", "\110\145\154\154\157\40\151\156\40\117\143\164\141\154")


# x48  = H
ch = 0 * (16**2) + 4 * (16**1) + 8 * (16**0)
print(" 48:hex = {}:decimal = {}:char ".format(ch, chr(ch)))
# o110 = H
ch = 1 * (8**2) + 1 * (8**1) + 0 * (8**0)
print("110:oct = {}:decimal = {}:char ".format(ch, chr(ch)))


print("convert 110 oct to decimal:", int("110", 8), chr(int("110", 8)))
print("convert x48 hex to decimal:", int("48", 16), chr(int("48", 16)))


print(ord("a"))
print(ord("A"))
print(ord("H"))
print(bin(ord("H")))
print(oct(ord("H")))
print(hex(ord("H")))


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~