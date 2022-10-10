import numpy as np


my_array = np.array(["A", "B", "Hello"], dtype="S")
print(my_array, type(my_array), my_array.dtype)  # S5


my_array = np.array(["A", "B", "Hello"], dtype="U")
print(my_array, type(my_array), my_array.dtype)  # U5


my_array = np.array([3 + 4j, 1 + 2j, 1])
print(my_array, type(my_array), my_array.dtype)  # complex128


my_array = np.array([1.1, 2, 3])
print(my_array, type(my_array), my_array.dtype)  # float64


my_array = np.array(["2020-12-02", "2022-11-03"], dtype="M")
print(my_array, type(my_array), my_array.dtype)  # datetime64


my_array = np.array([100000, 200000], dtype="m")
print(my_array, type(my_array), my_array.dtype)  # timedelta64


my_array = np.array([True, False])
print(my_array, type(my_array), my_array.dtype)  # bool


my_array = np.array([1, 2], "i1")
print(my_array, type(my_array), my_array.dtype)  # int8 -> 8 bits -> 0 - 255


my_array = np.array([1, 2], "i2")
print(my_array, type(my_array), my_array.dtype)  # int16


my_array = np.array([1, 2], "i4")
print(my_array, type(my_array), my_array.dtype)  # int32


my_array = np.array([1, 2], "i8")
print(my_array, type(my_array), my_array.dtype)  # int64


my_array = np.array([1, 2], "b")
print(my_array, type(my_array), my_array.dtype)  # int8


my_array = np.array([1, 2], "f2")
print(my_array, type(my_array), my_array.dtype)  # float16


my_array = np.array([1, 2], "f")  # == f4
print(my_array, type(my_array), my_array.dtype)  # float32


my_array = np.array([1, 2], "f8")
print(my_array, type(my_array), my_array.dtype)  # float64


class MyClass:
    pass


my_array = np.array([MyClass(), MyClass()], "O")
print(my_array, type(my_array), my_array.dtype)  # object


my_array = np.array([b'A', b'B'], "V")
print(my_array, type(my_array), my_array.dtype)  # V1
