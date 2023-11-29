from abc import ABC


class Shape(ABC):
    def what_area(self, shapes):
        print(f"Calculating the area")
        print(f"====================")
        for shape in shapes:
            print(f"Area for your {shape.name}")
            print(f"Area: {shape.what_area()}")

    def what_perimeter(self, shapes):
        print(f"Calculating the perimeter")
        print(f"====================")
        for shape in shapes:
            print(f"Perimeter for your {shape.name}")
            print(f"Perimeter: {shape.what_perimeter()}")


class Triangle(Shape):
    def __init__(self, base, height, second_side, third_side):
        self.base = base
        self.height = height
        self.second_side = second_side
        self.third_side = third_side

    def what_area(self):
        return 0.5 * (self.base * self.height)

    def what_perimeter(self):
        return self.base + self.second_side + self.third_side


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def what_area(self):
        return self.side * self.side

    def what_perimeter(self):
        return self.side * 4


class Rectangle(Shape):
    def __init__(self, large, long):
        self.large = large
        self.long = long

    def what_area(self):
        return self.large * self.long

    def what_perimeter(self):
        return 2 * (self.large + self.long)
