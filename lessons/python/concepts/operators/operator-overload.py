class Entity:
    value = 0

    def __init__(self, value) -> None:
        self.value = value

    def __add__(self, obj):
        return Entity(self.value + obj.value)

    def __mul__(self, obj):
        return Entity(self.value * obj.value)


e1 = Entity(2)
e2 = Entity(3)
e3 = e1 + e2
e4 = e1 * e2
# e5 = e1 / e2 -> TypeError: unsupported operand type(s) for /: 'Entity' and 'Entity'
print(e3.value)
print(e4.value)

print(type(e3))
print(type(e3.__add__))
