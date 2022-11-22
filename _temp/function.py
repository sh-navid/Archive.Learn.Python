# -------------------------------------------------------------------
# Make a function with `def`
def c1(a, b):
    return a*b

print(c1(20, 30))
'''
Output:
600
'''

# -------------------------------------------------------------------
# OR make a function with `lambda`
c2 = lambda a, b: a*b

print(c2(20, 30))
'''
Output:
600
'''

# -------------------------------------------------------------------
# A function calls itself

def r1(num):
    print(num)
    if num > 0:
        num //= 2
        r1(num)


r1(8)
'''
Outout:
8
4
2
1
0
'''

# -------------------------------------------------------------------
# A Recursive fucntion
def r2(num):
    if (num < 1000):
        return num
    num //= 2
    return r2(num)


print(r2(2020))
# 505.0

print(r2(600))
# 600

print(r2(10000097263198765721809809435198098087908709872))
# 896
