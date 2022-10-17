def rectangle_area(x,y=None):
    if y is None:
        return x*x
    else:
        return x*y

print(rectangle_area(12))
print(rectangle_area(12,13))