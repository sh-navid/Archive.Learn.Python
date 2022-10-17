class Shape:
    def area(self):
        return -1

    def __init__(self, *values) -> None:
        self.value = values


class Rectangle(Shape):
    def area(self):
        return self.value[0] * self.value[1]


class Triangle(Shape):
    def area(self):
        return (self.value[0] * self.value[1]) / 2


class Square(Shape):
    def area(self):
        return self.value[0] * self.value[0]


s1 = Rectangle(10, 12)
s2 = Triangle(10, 12)
s3 = Square(10)

for shape in [s1, s2, s3]:
    print(shape.area())
