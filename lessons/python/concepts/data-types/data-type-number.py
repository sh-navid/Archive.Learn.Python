def ttype(a):
    print(a,"\t",type(a))

ttype(2)
ttype(2.1)
ttype(2j)
ttype(2j+4)

# Output:
"""
2        <class 'int'>
2.1      <class 'float'>
2j       <class 'complex'>
(4+2j)   <class 'complex'>
"""

x=2j+4
ttype(x)
print(x.real,x.imag)

# Output
"""
(4+2j)   <class 'complex'>
4.0 2.0
"""