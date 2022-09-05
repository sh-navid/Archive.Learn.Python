class Entity:
    def set(self, value):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

    calc = lambda num: num**2

    def run():
        pass


obj1 = Entity()
obj1.set(12)

obj2 = Entity()
obj2.set(45)

print(obj1, obj2)

Entity.run()
print(Entity.calc(12))

# --------------------------------------------------
del obj1
try:
    print(obj1)
except Exception as e:
    print(e)

# --------------------------------------------------

import types

x = lambda a, b, c: a * b * c

print(x(1, 2, 3), type(x))
print(types.LambdaType is x.__class__, types.LambdaType, x.__class__)
print(types.FunctionType is x.__class__, types.FunctionType, x.__class__)
print(types.FunctionType is types.LambdaType, types.FunctionType, types.LambdaType)
print(types.FunctionType is types.MethodType, types.FunctionType, types.MethodType)
