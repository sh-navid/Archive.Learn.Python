import numpy as np

# One's Complement
#   1001    ->     0110
#   1100    ->     0011
# Signed Numbers
#   * First bit is sign bit 
#   *  0 (00000000),  127 (01111111)
#   * -1 (11111111), -128 (10000000)
#   * Two's Complement of 4 is -4; It is a method of storing negative numbers. We use the most significant bit.


def complement_repr(n):
    # Binary Representation
    # 00000101
    b = np.binary_repr(n, width=8)

    # One's Complement
    # 11111010
    c1 = np.binary_repr(np.bitwise_not(n), width=8)

    # Two's Complement
    # 11111011
    c2 = np.binary_repr(np.bitwise_not(n) + 1, width=8)

    return {"binary": b, "ones_complement": c1, "twos_complement": c2}


print(complement_repr(5))
print(complement_repr(-5))
"""
{'binary': '00000101', 'ones_complement': '11111010', 'twos_complement': '11111011'}
{'binary': '11111011', 'ones_complement': '00000100', 'twos_complement': '00000101'}
"""

# for i in range(0, 128):
#     print(
#         i, "\t", np.binary_repr(i, width=8), "\t", ~i, "\t", np.binary_repr(~i, width=8)
#     )
"""
0 	     00000000 	 -1 	 11111111
1 	     00000001 	 -2 	 11111110
2 	     00000010 	 -3 	 11111101
3 	     00000011 	 -4 	 11111100
4 	     00000100 	 -5 	 11111011
5 	     00000101 	 -6 	 11111010
6 	     00000110 	 -7 	 11111001
7 	     00000111 	 -8 	 11111000
8 	     00001000 	 -9 	 11110111
9 	     00001001 	 -10 	 11110110
10 	     00001010 	 -11 	 11110101
11 	     00001011 	 -12 	 11110100
12 	     00001100 	 -13 	 11110011
13 	     00001101 	 -14 	 11110010
14 	     00001110 	 -15 	 11110001
15 	     00001111 	 -16 	 11110000
16 	     00010000 	 -17 	 11101111
17 	     00010001 	 -18 	 11101110
18 	     00010010 	 -19 	 11101101
19 	     00010011 	 -20 	 11101100
20 	     00010100 	 -21 	 11101011
21 	     00010101 	 -22 	 11101010
22 	     00010110 	 -23 	 11101001
23 	     00010111 	 -24 	 11101000
24 	     00011000 	 -25 	 11100111
25 	     00011001 	 -26 	 11100110
26 	     00011010 	 -27 	 11100101
27 	     00011011 	 -28 	 11100100
28 	     00011100 	 -29 	 11100011
29 	     00011101 	 -30 	 11100010
30 	     00011110 	 -31 	 11100001
31 	     00011111 	 -32 	 11100000
32 	     00100000 	 -33 	 11011111
33 	     00100001 	 -34 	 11011110
34 	     00100010 	 -35 	 11011101
35 	     00100011 	 -36 	 11011100
36 	     00100100 	 -37 	 11011011
37 	     00100101 	 -38 	 11011010
38 	     00100110 	 -39 	 11011001
39 	     00100111 	 -40 	 11011000
40 	     00101000 	 -41 	 11010111
41 	     00101001 	 -42 	 11010110
42 	     00101010 	 -43 	 11010101
43 	     00101011 	 -44 	 11010100
44 	     00101100 	 -45 	 11010011
45 	     00101101 	 -46 	 11010010
46 	     00101110 	 -47 	 11010001
47 	     00101111 	 -48 	 11010000
48 	     00110000 	 -49 	 11001111
49 	     00110001 	 -50 	 11001110
50 	     00110010 	 -51 	 11001101
51 	     00110011 	 -52 	 11001100
52 	     00110100 	 -53 	 11001011
53 	     00110101 	 -54 	 11001010
54 	     00110110 	 -55 	 11001001
55 	     00110111 	 -56 	 11001000
56 	     00111000 	 -57 	 11000111
57 	     00111001 	 -58 	 11000110
58 	     00111010 	 -59 	 11000101
59 	     00111011 	 -60 	 11000100
60 	     00111100 	 -61 	 11000011
61 	     00111101 	 -62 	 11000010
62 	     00111110 	 -63 	 11000001
63 	     00111111 	 -64 	 11000000
64 	     01000000 	 -65 	 10111111
65 	     01000001 	 -66 	 10111110
66 	     01000010 	 -67 	 10111101
67 	     01000011 	 -68 	 10111100
68 	     01000100 	 -69 	 10111011
69 	     01000101 	 -70 	 10111010
70 	     01000110 	 -71 	 10111001
71 	     01000111 	 -72 	 10111000
72 	     01001000 	 -73 	 10110111
73 	     01001001 	 -74 	 10110110
74 	     01001010 	 -75 	 10110101
75 	     01001011 	 -76 	 10110100
76 	     01001100 	 -77 	 10110011
77 	     01001101 	 -78 	 10110010
78 	     01001110 	 -79 	 10110001
79 	     01001111 	 -80 	 10110000
80 	     01010000 	 -81 	 10101111
81 	     01010001 	 -82 	 10101110
82 	     01010010 	 -83 	 10101101
83 	     01010011 	 -84 	 10101100
84 	     01010100 	 -85 	 10101011
85 	     01010101 	 -86 	 10101010
86 	     01010110 	 -87 	 10101001
87 	     01010111 	 -88 	 10101000
88 	     01011000 	 -89 	 10100111
89 	     01011001 	 -90 	 10100110
90 	     01011010 	 -91 	 10100101
91 	     01011011 	 -92 	 10100100
92 	     01011100 	 -93 	 10100011
93 	     01011101 	 -94 	 10100010
94 	     01011110 	 -95 	 10100001
95 	     01011111 	 -96 	 10100000
96 	     01100000 	 -97 	 10011111
97 	     01100001 	 -98 	 10011110
98 	     01100010 	 -99 	 10011101
99 	     01100011 	 -100 	 10011100
100 	 01100100 	 -101 	 10011011
101 	 01100101 	 -102 	 10011010
102 	 01100110 	 -103 	 10011001
103 	 01100111 	 -104 	 10011000
104 	 01101000 	 -105 	 10010111
105 	 01101001 	 -106 	 10010110
106 	 01101010 	 -107 	 10010101
107 	 01101011 	 -108 	 10010100
108 	 01101100 	 -109 	 10010011
109 	 01101101 	 -110 	 10010010
110 	 01101110 	 -111 	 10010001
111 	 01101111 	 -112 	 10010000
112 	 01110000 	 -113 	 10001111
113 	 01110001 	 -114 	 10001110
114 	 01110010 	 -115 	 10001101
115 	 01110011 	 -116 	 10001100
116 	 01110100 	 -117 	 10001011
117 	 01110101 	 -118 	 10001010
118 	 01110110 	 -119 	 10001001
119 	 01110111 	 -120 	 10001000
120 	 01111000 	 -121 	 10000111
121 	 01111001 	 -122 	 10000110
122 	 01111010 	 -123 	 10000101
123 	 01111011 	 -124 	 10000100
124 	 01111100 	 -125 	 10000011
125 	 01111101 	 -126 	 10000010
126 	 01111110 	 -127 	 10000001
127 	 01111111 	 -128 	 10000000
"""
