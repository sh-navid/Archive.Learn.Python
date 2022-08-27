import base64

LJUST = 10
RJUST = 10

def clear(byte_arr):
    txt = byte_arr.decode()  # convert to string from bytes
    txt = txt.replace("=", "")
    return txt


def calc(number):
    ch = chr(number)
    txt = chr(number) if ch.isprintable() and ch.isascii() else " "
    print(
        str(number).ljust(8),
        txt.ljust(6),
        str(ch.isascii()).ljust(7),
        ((bin(number).rjust(RJUST)).ljust(LJUST)).replace("0b", ""),
        ((oct(number).rjust(7)).ljust(LJUST)).replace("0o", ""),
        ((hex(number).rjust(RJUST // 3)).ljust(LJUST)).replace("0x", ""),
        clear(base64.b16encode(str(number).encode())).ljust(LJUST),
        clear(base64.b32encode(str(number).encode())).ljust(LJUST),
        clear(base64.b64encode(str(number).encode())).ljust(LJUST),
        clear(base64.b85encode(str(number).encode())).ljust(LJUST),
    )


for i in range(256):
    calc(i)

# Decimal: system of numbers based on the number "ten"
"""
Decimal  Char   isASCII?       Bin   Oct  Hex      Base16     Base32     Base64     Base85
0               True           0     0    0        30         GA         MA         Fa        
1               True           1     1    1        31         GE         MQ         F#        
2               True          10     2    2        32         GI         Mg         G5        
3               True          11     3    3        33         GM         Mw         GX        
4               True         100     4    4        34         GQ         NA         Gy        
5               True         101     5    5        35         GU         NQ         H2        
6               True         110     6    6        36         GY         Ng         HU        
7               True         111     7    7        37         G4         Nw         Hv        
8               True        1000    10    8        38         HA         OA         H~        
9               True        1001    11    9        39         HE         OQ         IR        
10              True        1010    12    a        3130       GEYA       MTA        F)#       
11              True        1011    13    b        3131       GEYQ       MTE        F);       
12              True        1100    14    c        3132       GEZA       MTI        F){       
13              True        1101    15    d        3133       GEZQ       MTM        F*5       
14              True        1110    16    e        3134       GE2A       MTQ        F*E       
15              True        1111    17    f        3135       GE2Q       MTU        F*N       
16              True       10000    20    10       3136       GE3A       MTY        F*X       
17              True       10001    21    11       3137       GE3Q       MTc        F*g       
18              True       10010    22    12       3138       GE4A       MTg        F*p       
19              True       10011    23    13       3139       GE4Q       MTk        F*y       
20              True       10100    24    14       3230       GIYA       MjA        GB5       
21              True       10101    25    15       3231       GIYQ       MjE        GBE       
22              True       10110    26    16       3232       GIZA       MjI        GBN       
23              True       10111    27    17       3233       GIZQ       MjM        GBW       
24              True       11000    30    18       3234       GI2A       MjQ        GBf       
25              True       11001    31    19       3235       GI2Q       MjU        GBp       
26              True       11010    32    1a       3236       GI3A       MjY        GBy       
27              True       11011    33    1b       3237       GI3Q       Mjc        GB*       
28              True       11100    34    1c       3238       GI4A       Mjg        GB^       
29              True       11101    35    1d       3239       GI4Q       Mjk        GC2       
30              True       11110    36    1e       3330       GMYA       MzA        GcW       
31              True       11111    37    1f       3331       GMYQ       MzE        Gcf       
32              True      100000    40    20       3332       GMZA       MzI        Gco       
33       !      True      100001    41    21       3333       GMZQ       MzM        Gcy       
34       "      True      100010    42    22       3334       GM2A       MzQ        Gc*       
35       #      True      100011    43    23       3335       GM2Q       MzU        Gc^       
36       $      True      100100    44    24       3336       GM3A       MzY        Gd2       
37       %      True      100101    45    25       3337       GM3Q       Mzc        GdB       
38       &      True      100110    46    26       3338       GM4A       Mzg        GdK       
39       '      True      100111    47    27       3339       GM4Q       Mzk        GdT       
40       (      True      101000    50    28       3430       GQYA       NDA        G%x       
41       )      True      101001    51    29       3431       GQYQ       NDE        G%)       
42       *      True      101010    52    2a       3432       GQZA       NDI        G%^       
43       +      True      101011    53    2b       3433       GQZQ       NDM        G&2       
44       ,      True      101100    54    2c       3434       GQ2A       NDQ        G&B       
45       -      True      101101    55    2d       3435       GQ2Q       NDU        G&K       
46       .      True      101110    56    2e       3436       GQ3A       NDY        G&T       
47       /      True      101111    57    2f       3437       GQ3Q       NDc        G&c       
48       0      True      110000    60    30       3438       GQ4A       NDg        G&l       
49       1      True      110001    61    31       3439       GQ4Q       NDk        G&u       
50       2      True      110010    62    32       3530       GUYA       NTA        H82       
51       3      True      110011    63    33       3531       GUYQ       NTE        H8B       
52       4      True      110100    64    34       3532       GUZA       NTI        H8K       
53       5      True      110101    65    35       3533       GUZQ       NTM        H8T       
54       6      True      110110    66    36       3534       GU2A       NTQ        H8c       
55       7      True      110111    67    37       3535       GU2Q       NTU        H8l       
56       8      True      111000    70    38       3536       GU3A       NTY        H8u       
57       9      True      111001    71    39       3537       GU3Q       NTc        H8%       
58       :      True      111010    72    3a       3538       GU4A       NTg        H8        
59       ;      True      111011    73    3b       3539       GU4Q       NTk        H8}       
60       <      True      111100    74    3c       3630       GYYA       NjA        HZT       
61       =      True      111101    75    3d       3631       GYYQ       NjE        HZc       
62       >      True      111110    76    3e       3632       GYZA       NjI        HZl       
63       ?      True      111111    77    3f       3633       GYZQ       NjM        HZu       
64       @      True     1000000   100    40       3634       GY2A       NjQ        HZ%       
65       A      True     1000001   101    41       3635       GY2Q       NjU        HZ        
66       B      True     1000010   102    42       3636       GY3A       NjY        HZ}       
67       C      True     1000011   103    43       3637       GY3Q       Njc        Ha7       
68       D      True     1000100   104    44       3638       GY4A       Njg        HaG       
69       E      True     1000101   105    45       3639       GY4Q       Njk        HaP       
70       F      True     1000110   106    46       3730       G4YA       NzA        H!u       
71       G      True     1000111   107    47       3731       G4YQ       NzE        H!%       
72       H      True     1001000   110    48       3732       G4ZA       NzI        H!        
73       I      True     1001001   111    49       3733       G4ZQ       NzM        H!}       
74       J      True     1001010   112    4a       3734       G42A       NzQ        H#7       
75       K      True     1001011   113    4b       3735       G42Q       NzU        H#G       
76       L      True     1001100   114    4c       3736       G43A       NzY        H#P       
77       M      True     1001101   115    4d       3737       G43Q       Nzc        H#Y       
78       N      True     1001110   116    4e       3738       G44A       Nzg        H#h       
79       O      True     1001111   117    4f       3739       G44Q       Nzk        H#q       
80       P      True     1010000   120    50       3830       HAYA       ODA        I4}       
81       Q      True     1010001   121    51       3831       HAYQ       ODE        I57       
82       R      True     1010010   122    52       3832       HAZA       ODI        I5G       
83       S      True     1010011   123    53       3833       HAZQ       ODM        I5P       
84       T      True     1010100   124    54       3834       HA2A       ODQ        I5Y       
85       U      True     1010101   125    55       3835       HA2Q       ODU        I5h       
86       V      True     1010110   126    56       3836       HA3A       ODY        I5q       
87       W      True     1010111   127    57       3837       HA3Q       ODc        I5z       
88       X      True     1011000   130    58       3838       HA4A       ODg        I5+       
89       Y      True     1011001   131    59       3839       HA4Q       ODk        I5_       
90       Z      True     1011010   132    5a       3930       HEYA       OTA        IWP       
91       [      True     1011011   133    5b       3931       HEYQ       OTE        IWY       
92       \      True     1011100   134    5c       3932       HEZA       OTI        IWh       
93       ]      True     1011101   135    5d       3933       HEZQ       OTM        IWq       
94       ^      True     1011110   136    5e       3934       HE2A       OTQ        IWz       
95       _      True     1011111   137    5f       3935       HE2Q       OTU        IW+       
96       `      True     1100000   140    60       3936       HE3A       OTY        IW_       
97       a      True     1100001   141    61       3937       HE3Q       OTc        IX3       
98       b      True     1100010   142    62       3938       HE4A       OTg        IXD       
99       c      True     1100011   143    63       3939       HE4Q       OTk        IXM       
100      d      True     1100100   144    64       313030     GEYDA      MTAw       F)%O      
101      e      True     1100101   145    65       313031     GEYDC      MTAx       F)%R      
102      f      True     1100110   146    66       313032     GEYDE      MTAy       F)%U      
103      g      True     1100111   147    67       313033     GEYDG      MTAz       F)%X      
104      h      True     1101000   150    68       313034     GEYDI      MTA0       F)%a      
105      i      True     1101001   151    69       313035     GEYDK      MTA1       F)%d      
106      j      True     1101010   152    6a       313036     GEYDM      MTA2       F)%g      
107      k      True     1101011   153    6b       313037     GEYDO      MTA3       F)%j      
108      l      True     1101100   154    6c       313038     GEYDQ      MTA4       F)%m      
109      m      True     1101101   155    6d       313039     GEYDS      MTA5       F)%p      
110      n      True     1101110   156    6e       313130     GEYTA      MTEw       F)U       
111      o      True     1101111   157    6f       313131     GEYTC      MTEx       F)X       
112      p      True     1110000   160    70       313132     GEYTE      MTEy       F)a       
113      q      True     1110001   161    71       313133     GEYTG      MTEz       F)d       
114      r      True     1110010   162    72       313134     GEYTI      MTE0       F)g       
115      s      True     1110011   163    73       313135     GEYTK      MTE1       F)j       
116      t      True     1110100   164    74       313136     GEYTM      MTE2       F)m       
117      u      True     1110101   165    75       313137     GEYTO      MTE3       F)p       
118      v      True     1110110   166    76       313138     GEYTQ      MTE4       F)s       
119      w      True     1110111   167    77       313139     GEYTS      MTE5       F)v       
120      x      True     1111000   170    78       313230     GEZDA      MTIw       F)}a      
121      y      True     1111001   171    79       313231     GEZDC      MTIx       F)}d      
122      z      True     1111010   172    7a       313232     GEZDE      MTIy       F)}g      
123      {      True     1111011   173    7b       313233     GEZDG      MTIz       F)}j      
124      |      True     1111100   174    7c       313234     GEZDI      MTI0       F)}m      
125      }      True     1111101   175    7d       313235     GEZDK      MTI1       F)}p      
126      ~      True     1111110   176    7e       313236     GEZDM      MTI2       F)}s      
127             True     1111111   177    7f       313237     GEZDO      MTI3       F)}v      
128             False   10000000   200    80       313238     GEZDQ      MTI4       F)}y      
129             False   10000001   201    81       313239     GEZDS      MTI5       F)}#      
130             False   10000010   202    82       313330     GEZTA      MTMw       F*7g      
131             False   10000011   203    83       313331     GEZTC      MTMx       F*7j      
132             False   10000100   204    84       313332     GEZTE      MTMy       F*7m      
133             False   10000101   205    85       313333     GEZTG      MTMz       F*7p      
134             False   10000110   206    86       313334     GEZTI      MTM0       F*7s      
135             False   10000111   207    87       313335     GEZTK      MTM1       F*7v      
136             False   10001000   210    88       313336     GEZTM      MTM2       F*7y      
137             False   10001001   211    89       313337     GEZTO      MTM3       F*7#      
138             False   10001010   212    8a       313338     GEZTQ      MTM4       F*7&      
139             False   10001011   213    8b       313339     GEZTS      MTM5       F*7*      
140             False   10001100   214    8c       313430     GE2DA      MTQw       F*Gm      
141             False   10001101   215    8d       313431     GE2DC      MTQx       F*Gp      
142             False   10001110   216    8e       313432     GE2DE      MTQy       F*Gs      
143             False   10001111   217    8f       313433     GE2DG      MTQz       F*Gv      
144             False   10010000   220    90       313434     GE2DI      MTQ0       F*Gy      
145             False   10010001   221    91       313435     GE2DK      MTQ1       F*G#      
146             False   10010010   222    92       313436     GE2DM      MTQ2       F*G&      
147             False   10010011   223    93       313437     GE2DO      MTQ3       F*G*      
148             False   10010100   224    94       313438     GE2DQ      MTQ4       F*G;      
149             False   10010101   225    95       313439     GE2DS      MTQ5       F*G>      
150             False   10010110   226    96       313530     GE2TA      MTUw       F*Ps      
151             False   10010111   227    97       313531     GE2TC      MTUx       F*Pv      
152             False   10011000   230    98       313532     GE2TE      MTUy       F*Py      
153             False   10011001   231    99       313533     GE2TG      MTUz       F*P#      
154             False   10011010   232    9a       313534     GE2TI      MTU0       F*P&      
155             False   10011011   233    9b       313535     GE2TK      MTU1       F*P*      
156             False   10011100   234    9c       313536     GE2TM      MTU2       F*P;      
157             False   10011101   235    9d       313537     GE2TO      MTU3       F*P>      
158             False   10011110   236    9e       313538     GE2TQ      MTU4       F*P^      
159             False   10011111   237    9f       313539     GE2TS      MTU5       F*P{      
160             False   10100000   240    a0       313630     GE3DA      MTYw       F*Yy      
161             False   10100001   241    a1       313631     GE3DC      MTYx       F*Y#      
162             False   10100010   242    a2       313632     GE3DE      MTYy       F*Y&      
163             False   10100011   243    a3       313633     GE3DG      MTYz       F*Y*      
164             False   10100100   244    a4       313634     GE3DI      MTY0       F*Y;      
165             False   10100101   245    a5       313635     GE3DK      MTY1       F*Y>      
166             False   10100110   246    a6       313636     GE3DM      MTY2       F*Y^      
167             False   10100111   247    a7       313637     GE3DO      MTY3       F*Y{      
168             False   10101000   250    a8       313638     GE3DQ      MTY4       F*Y~      
169             False   10101001   251    a9       313639     GE3DS      MTY5       F*Z2      
170             False   10101010   252    aa       313730     GE3TA      MTcw       F*h&      
171             False   10101011   253    ab       313731     GE3TC      MTcx       F*h*      
172             False   10101100   254    ac       313732     GE3TE      MTcy       F*h;      
173             False   10101101   255    ad       313733     GE3TG      MTcz       F*h>      
174             False   10101110   256    ae       313734     GE3TI      MTc0       F*h^      
175             False   10101111   257    af       313735     GE3TK      MTc1       F*h{      
176             False   10110000   260    b0       313736     GE3TM      MTc2       F*h~      
177             False   10110001   261    b1       313737     GE3TO      MTc3       F*i2      
178             False   10110010   262    b2       313738     GE3TQ      MTc4       F*i5      
179             False   10110011   263    b3       313739     GE3TS      MTc5       F*i8      
180             False   10110100   264    b4       313830     GE4DA      MTgw       F*q;      
181             False   10110101   265    b5       313831     GE4DC      MTgx       F*q>      
182             False   10110110   266    b6       313832     GE4DE      MTgy       F*q^      
183             False   10110111   267    b7       313833     GE4DG      MTgz       F*q{      
184             False   10111000   270    b8       313834     GE4DI      MTg0       F*q~      
185             False   10111001   271    b9       313835     GE4DK      MTg1       F*r2      
186             False   10111010   272    ba       313836     GE4DM      MTg2       F*r5      
187             False   10111011   273    bb       313837     GE4DO      MTg3       F*r8      
188             False   10111100   274    bc       313838     GE4DQ      MTg4       F*rB      
189             False   10111101   275    bd       313839     GE4DS      MTg5       F*rE      
190             False   10111110   276    be       313930     GE4TA      MTkw       F*z^      
191             False   10111111   277    bf       313931     GE4TC      MTkx       F*z{      
192             False   11000000   300    c0       313932     GE4TE      MTky       F*z~      
193             False   11000001   301    c1       313933     GE4TG      MTkz       F*!2      
194             False   11000010   302    c2       313934     GE4TI      MTk0       F*!5      
195             False   11000011   303    c3       313935     GE4TK      MTk1       F*!8      
196             False   11000100   304    c4       313936     GE4TM      MTk2       F*!B      
197             False   11000101   305    c5       313937     GE4TO      MTk3       F*!E      
198             False   11000110   306    c6       313938     GE4TQ      MTk4       F*!H      
199             False   11000111   307    c7       313939     GE4TS      MTk5       F*!K      
200             False   11001000   310    c8       323030     GIYDA      MjAw       GB7X      
201             False   11001001   311    c9       323031     GIYDC      MjAx       GB7a      
202             False   11001010   312    ca       323032     GIYDE      MjAy       GB7d      
203             False   11001011   313    cb       323033     GIYDG      MjAz       GB7g      
204             False   11001100   314    cc       323034     GIYDI      MjA0       GB7j      
205             False   11001101   315    cd       323035     GIYDK      MjA1       GB7m      
206             False   11001110   316    ce       323036     GIYDM      MjA2       GB7p      
207             False   11001111   317    cf       323037     GIYDO      MjA3       GB7s      
208             False   11010000   320    d0       323038     GIYDQ      MjA4       GB7v      
209             False   11010001   321    d1       323039     GIYDS      MjA5       GB7y      
210             False   11010010   322    d2       323130     GIYTA      MjEw       GBGd      
211             False   11010011   323    d3       323131     GIYTC      MjEx       GBGg      
212             False   11010100   324    d4       323132     GIYTE      MjEy       GBGj      
213             False   11010101   325    d5       323133     GIYTG      MjEz       GBGm      
214             False   11010110   326    d6       323134     GIYTI      MjE0       GBGp      
215             False   11010111   327    d7       323135     GIYTK      MjE1       GBGs      
216             False   11011000   330    d8       323136     GIYTM      MjE2       GBGv      
217             False   11011001   331    d9       323137     GIYTO      MjE3       GBGy      
218             False   11011010   332    da       323138     GIYTQ      MjE4       GBG#      
219             False   11011011   333    db       323139     GIYTS      MjE5       GBG&      
220             False   11011100   334    dc       323230     GIZDA      MjIw       GBPj      
221             False   11011101   335    dd       323231     GIZDC      MjIx       GBPm      
222             False   11011110   336    de       323232     GIZDE      MjIy       GBPp      
223             False   11011111   337    df       323233     GIZDG      MjIz       GBPs      
224             False   11100000   340    e0       323234     GIZDI      MjI0       GBPv      
225             False   11100001   341    e1       323235     GIZDK      MjI1       GBPy      
226             False   11100010   342    e2       323236     GIZDM      MjI2       GBP#      
227             False   11100011   343    e3       323237     GIZDO      MjI3       GBP&      
228             False   11100100   344    e4       323238     GIZDQ      MjI4       GBP*      
229             False   11100101   345    e5       323239     GIZDS      MjI5       GBP;      
230             False   11100110   346    e6       323330     GIZTA      MjMw       GBYp      
231             False   11100111   347    e7       323331     GIZTC      MjMx       GBYs      
232             False   11101000   350    e8       323332     GIZTE      MjMy       GBYv      
233             False   11101001   351    e9       323333     GIZTG      MjMz       GBYy      
234             False   11101010   352    ea       323334     GIZTI      MjM0       GBY#      
235             False   11101011   353    eb       323335     GIZTK      MjM1       GBY&      
236             False   11101100   354    ec       323336     GIZTM      MjM2       GBY*      
237             False   11101101   355    ed       323337     GIZTO      MjM3       GBY;      
238             False   11101110   356    ee       323338     GIZTQ      MjM4       GBY>      
239             False   11101111   357    ef       323339     GIZTS      MjM5       GBY^      
240             False   11110000   360    f0       323430     GI2DA      MjQw       GBhv      
241             False   11110001   361    f1       323431     GI2DC      MjQx       GBhy      
242             False   11110010   362    f2       323432     GI2DE      MjQy       GBh#      
243             False   11110011   363    f3       323433     GI2DG      MjQz       GBh&      
244             False   11110100   364    f4       323434     GI2DI      MjQ0       GBh*      
245             False   11110101   365    f5       323435     GI2DK      MjQ1       GBh;      
246             False   11110110   366    f6       323436     GI2DM      MjQ2       GBh>      
247             False   11110111   367    f7       323437     GI2DO      MjQ3       GBh^      
248             False   11111000   370    f8       323438     GI2DQ      MjQ4       GBh{      
249             False   11111001   371    f9       323439     GI2DS      MjQ5       GBh~      
250             False   11111010   372    fa       323530     GI2TA      MjUw       GBq#      
251             False   11111011   373    fb       323531     GI2TC      MjUx       GBq&      
252             False   11111100   374    fc       323532     GI2TE      MjUy       GBq*      
253             False   11111101   375    fd       323533     GI2TG      MjUz       GBq;      
254             False   11111110   376    fe       323534     GI2TI      MjU0       GBq>      
255             False   11111111   377    ff       323535     GI2TK      MjU1       GBq^      
"""
