import unittest


class Shape:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w*self.h


class TestShape(unittest.TestCase):
    def test_area_calculation(self):
        s = Shape(12, 10)
        print(s.area())
        self.assetTrue(s.area(), 120, "Area with 10 and 12 should be 120")
        self.assertGreaterEqual(s.area(), 0, "Area should be 0 or greater")


if __name__ == "__main__":
    unittest.main()
