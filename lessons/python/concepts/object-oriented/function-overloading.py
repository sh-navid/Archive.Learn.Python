class Shape:
    area = None

    @classmethod
    def calc_area(cls, x, y=None, is_triangle=False):
        if y is None:
            cls.area = x * x
        else:
            cls.area = x * y

        if is_triangle:
            cls.area /= 2

        return cls.area


print(Shape.calc_area(10))
print(Shape.calc_area(10, 12))
print(Shape.calc_area(10, 12, True))