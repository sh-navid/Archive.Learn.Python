class MyClass:
    name = "PUBLIC"
    _family = "PROTECTED"
    __middle = "PRIVATE"

    def get_private_variable(self):
        return self.__middle

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, value):
        self._family = value


# ------------------------------------------------------------
# Public member

print(MyClass.name)

# ------------------------------------------------------------
# Protected member - Property

print(MyClass._family)  # Accessible - but do not use it like this

cls = MyClass()
print(cls.family)
cls.family += "-Changed"
print(cls.family)
print(cls._family)  # Accessible - but do not use it like this

# ------------------------------------------------------------
# Private member

# print(MyClass.__middle) # AttributeError: type object 'MyClass' has no attribute '__middle'
print(MyClass().get_private_variable())


# ------------------------------------------------------------
class DerivedClass(MyClass):
    name="PUBLIC2"
    _family="PROTECTED2"
    __middle = "New Private Middle Name"


cls = MyClass()
dcls = DerivedClass()

print(cls.name," --- ", dcls.name)
print(cls._family," --- ", dcls._family)
print(cls.get_private_variable()," --- ", dcls.get_private_variable()) # __middle in new class is not shadowed the original one
"""
PUBLIC  ---  PUBLIC2
PROTECTED  ---  PROTECTED2
PRIVATE  ---  PRIVATE
"""
