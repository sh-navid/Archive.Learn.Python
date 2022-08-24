## این فایل کامل نیست
## صبر کنید تا ورژن بعدی

import numpy as np

# One's Complement مکمل یک یا
#   1001    ->     0110
#   1100    ->     0011
# Two's Complement مکمل‌ دو یا متمم دو یا
#   *  0 (00000000),  127 (01111111)
#   * -1 (11111111), -128 (10000000)


def my_binary_repr(n):
    # u: unsignred, s: signed
    # eg -> n:-5

    # b: '0b101'
    u = bin(n)

    # b: '101'
    u = u.replace("0b", "")

    # b: '00000101'
    b = 9 if u[0] == "-" else 8
    u = u.zfill(b)

    # If number have a sign like -5
    s = None
    if u[0] == "-":
        # Remove - Sign from U
        # -0000101 -> 0000101
        u = u[1:]

        # One's Complement
        # '1111010'
        s = u
        s = "".join(["0" if x == "1" else "1" for x in u])

        # Add 1 to the result
        # *** Not completed yet ***
        # carrier = 0
        # for i in range(7, -1, -1):
        #     bit = int(s[i])
        #     result = 
        #     print(bit, result)

    return (u, s)


print(np.binary_repr(-5, width=8))
print(my_binary_repr(-5))
