import ctypes

l = [3, 4, 5]
i = id(l)
print(l, type(l), i)

ref = ctypes.cast(i, ctypes.py_object).value
ref[0] = 12
ref[1] = 15

print(l, ref)
print(i, id(ref))