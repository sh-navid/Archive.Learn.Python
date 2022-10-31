import re

s = "Hello to this world 100"
m = re.search("\s", s)
print(m.start(), m.end())


m = re.search("[0-9]", s)
print(m.start(), m.end())


m = re.search("[0-9][0-9]", s)
print(m.start(), m.end())


m = re.search("[0-9]+", s)
print(m.start(), m.end())