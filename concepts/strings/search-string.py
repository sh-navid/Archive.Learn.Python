# Search

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
s = "Hello World"
print("StartsWith:", s.startswith("hello"))
print("StartsWith:", s.startswith("Hello"))

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
s = "Hello World"
print("EndsWith:", s.endswith("rld"))
print("EndsWith:", s.endswith("bye"))

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
s = "Hello World"
print("Find:", s.find("World"))
print("Find:", s.find("apple"))
print('L Find "o":', s.find("o"))
print('R Find "o":', s.rfind("o"))

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Find vs Index
s = "Hello World"
print("Index:", s.index("World"))
# print("Index:", s.index("apple")) # ValueError: substring not found

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
s = "hi hello hi hi bye"
search = "hello"
print("L Index:", f' Text:"{s}", Search for "{search}" -> ', s.index(search))
# last founded substring ->
print("R Index:", f' Text:"{s}", Search for "{search}" -> ', s.rindex(search))

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
s = "hi hello hi hi bye"
search = "hi"
print("L Index:", f' Text:"{s}", Search for "{search}" -> ', s.index(search))
# last founded substring ->
print("R Index:", f' Text:"{s}", Search for "{search}" -> ', s.rindex(search))
