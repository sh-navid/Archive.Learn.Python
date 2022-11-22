# encode, decode
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

s = "Hello World"
print(s, type(s))
# Hello World       <class 'str'>


e = s.encode()
print(e, type(e))
# b'Hello World'    <class 'bytes'>


d = e.decode()
print(d, type(d))
# Hello World       <class 'str'>