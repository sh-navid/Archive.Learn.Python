# encode, decode

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
s = "Hello World"
e = s.encode()
d = e.decode()

print(s, type(s))
print(e, type(e))
print(d, type(d))

# Hello World       <class 'str'>
# b'Hello World'    <class 'bytes'>
# Hello World       <class 'str'>
