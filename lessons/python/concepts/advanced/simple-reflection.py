# [Functions for Reflection]

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# dir() -> show list of attributes
# type()
# getattr()
# callable()
# isinstance()


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MyClass:
    value = 1000

    def test():
        return "hello"


obj = MyClass()


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# dir()
###--------------------------------------------------------------
print(obj.__dir__())  # -> dir(obj)
# ['__module__', 'value', 'test', '__dict__', '__weakref__',
# '__doc__', '__new__', '__repr__', '__hash__', '__str__',
# '__getattribute__', '__setattr__', '__delattr__', '__lt__',
# '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__',
# '__reduce_ex__', '__reduce__', '__subclasshook__',
# '__init_subclass__', '__format__', '__sizeof__',
# '__dir__', '__class__']

for attr in dir(obj):
    x = None
    exec(f"x = obj.{attr}")
    print(f"obj.{attr}\t\tIs Callable: {callable(x)},\ttype: {type(x)}".expandtabs(20))
"""
obj.__class__                           Is Callable: True,  type: <class 'type'>
obj.__delattr__                         Is Callable: True,  type: <class 'method-wrapper'>
obj.__dict__                            Is Callable: False, type: <class 'dict'>
obj.__dir__                             Is Callable: True,  type: <class 'builtin_function_or_method'>
obj.__doc__                             Is Callable: False, type: <class 'NoneType'>
obj.__eq__                              Is Callable: True,  type: <class 'method-wrapper'>
obj.__format__                          Is Callable: True,  type: <class 'builtin_function_or_method'>
obj.__ge__                              Is Callable: True,  type: <class 'method-wrapper'>
obj.__getattribute__                    Is Callable: True,  type: <class 'method-wrapper'>
obj.__gt__                              Is Callable: True,  type: <class 'method-wrapper'>
obj.__hash__                            Is Callable: True,  type: <class 'method-wrapper'>
obj.__init__                            Is Callable: True,  type: <class 'method-wrapper'>
obj.__init_subclass__                   Is Callable: True,  type: <class 'builtin_function_or_method'>
obj.__le__                              Is Callable: True,  type: <class 'method-wrapper'>
obj.__lt__                              Is Callable: True,  type: <class 'method-wrapper'>
obj.__module__                          Is Callable: False, type: <class 'str'>
obj.__ne__                              Is Callable: True,  type: <class 'method-wrapper'>
obj.__new__                             Is Callable: True,  type: <class 'builtin_function_or_method'>
obj.__reduce__                          Is Callable: True,  type: <class 'builtin_function_or_method'>
obj.__reduce_ex__                       Is Callable: True,  type: <class 'builtin_function_or_method'>
obj.__repr__                            Is Callable: True,  type: <class 'method-wrapper'>
obj.__setattr__                         Is Callable: True,  type: <class 'method-wrapper'>
obj.__sizeof__                          Is Callable: True,  type: <class 'builtin_function_or_method'>
obj.__str__                             Is Callable: True,  type: <class 'method-wrapper'>
obj.__subclasshook__                    Is Callable: True,  type: <class 'builtin_function_or_method'>
obj.__weakref__                         Is Callable: False, type: <class 'NoneType'>
obj.test                                Is Callable: True,  type: <class 'method'>
obj.value                               Is Callable: False, type: <class 'int'>
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# type()
###--------------------------------------------------------------
print(f"Check type: ", type(obj))
# Type:  <class '__main__.MyClass'>

print(f"Is [obj] type of: {MyClass.__name__} -> ", type(obj) is MyClass)
# Is [obj] type of: MyClass ->  True

print(f"Is [obj] type of: {SystemError.__name__} -> ", type(obj) is SystemError)
# Is [obj] type of: SystemError ->  False


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# getattr()
###--------------------------------------------------------------
print(obj.__getattribute__("value"))  # -> getattr(obj, "value")
# 1000

# AttributeError: 'MyClass' object has no attribute 'value2'
# print(obj.__getattribute__("value2"))


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# callable()
###--------------------------------------------------------------
print(callable(obj))  # False
print(callable(obj.test))  # True
print(callable(obj.value))  # False

# AttributeError: 'MyClass' object has no attribute 'test2'.
# print(callable(obj.test2))


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# isinstance()
###--------------------------------------------------------------
print(f"Is [obj] instance of: {MyClass.__name__} -> ", isinstance(obj, MyClass))
# Is [obj] instance of: MyClass ->  True

print(f"Is [obj] instance of: {BufferError.__name__} -> ", isinstance(obj, BufferError))
# Is [obj] instance of: BufferError ->  False
