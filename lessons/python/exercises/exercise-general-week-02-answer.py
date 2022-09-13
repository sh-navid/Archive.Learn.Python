import random

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer 1
my_list = ["Hello", "My", "World"]
print("@".join(my_list).upper())
"""
HELLO@MY@WORLD
"""

print("$".join(my_list).lower())
"""
hello$my$world
"""

print("~".join(my_list).swapcase())
"""
hELLO~mY~wORLD
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer 2
FA = "۰۱۲۳۴۵۶۷۸۹"
EN = "0123456789"
s = "4433۶۶"

for x, y in zip(FA, EN):
    s = s.replace(x, y)
print("EN->", s)
"""
EN-> 443366
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer 3
coin = ["Back","Front"]
print(random.choice(coin))

coin = ["Back","Front","Front","Front","Front"]
print(random.choice(coin))

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer 4
s = """Hi:Hello
Bye:GoodBye
"""

s=s.splitlines()
print(s)
# ['Hi:Hello', 'Bye:GoodBye']

for i,item in enumerate(s):
    s[i]=item.split(":")
print(s)
# [['Hi', 'Hello'], ['Bye', 'GoodBye']]