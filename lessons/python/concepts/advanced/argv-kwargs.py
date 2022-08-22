def my_function(*argv, **kwargs):
    for v in argv:
        print("argument:", v)
    for kw in kwargs:
        print("keyword arguments:", kw, kwargs[kw])


my_function("Hello", "Workd", 1, name="Test", size=12)
"""
argument: Hello
argument: Workd
argument: 1
keyword arguments: name Test
keyword arguments: size 12
"""
