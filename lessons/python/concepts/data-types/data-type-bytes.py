def ttype(a):
    print(a, "\t", type(a))


ttype(b"XYZ")
# Output:
# b'XYZ'   <class 'bytes'>


# Immutable
ttype(bytes(4))
ttype(bytes(b"XYZ"))
# Output:
# b'\x00\x00\x00\x00'               <class 'bytes'>
# b'XYZ'                            <class 'bytes'>


# Mutable
ttype(bytearray(4))
ttype(bytearray(b"XYZ"))
# Output:
# bytearray(b'\x00\x00\x00\x00')    <class 'bytearray'>
# bytearray(b'XYZ')                 <class 'bytearray'>


ba = bytearray(b"XYZ")
ba[1] = int(65)
ttype(ba)
# Output:
# bytearray(b'XAZ')        <class 'bytearray'>


ttype(memoryview(b"XYZ"))
ttype(memoryview(bytes(8)))
# Output:
# <memory at 0x00000207B0D0DB40>   <class 'memoryview'>
# <memory at 0x00000207B0D0DB40>   <class 'memoryview'>


for x in memoryview(b"XYZA"):
    print(x, chr(x))
# Output:
"""
88 X
89 Y
90 Z
65 A
"""


# External Link
# To read more about concept of MemoryView
# https://www.programiz.com/python-programming/methods/built-in/memoryview
