from abc import ABC, abstractmethod


class Calculations(ABC):
    def what_area(self):
        pass

    def what_perimeter(self):
        pass

    def __str__(self):
        return f"Area: {self.what_area()}, Perimeter: {self.what_perimeter()}"


class Shape:
    def __init__(self, name):
        self.name = name


class Triangle(Shape, Calculations):
    def __init__(self, name, base, height, second_side, third_side):
        self.base = base
        self.height = height
        self.second_side = second_side
        self.third_side = third_side
        super().__init__(name)

    @abstractmethod
    def what_area(self):
        return 0.5 * (self.base * self.height)

    @abstractmethod
    def what_perimeter(self):
        return self.base + self.second_side + self.third_side


class Square(Shape, Calculations):
    def __init__(self, name, side):
        self.side = side
        super().__init__(name)

    @abstractmethod
    def what_area(self):
        return self.side * self.side

    @abstractmethod
    def what_perimeter(self):
        return self.side * 4


class Rectangle(Shape, Calculations):
    def __init__(self, name, large, long):
        self.large = large
        self.long = long
        super().__init__(name)

    @abstractmethod
    def what_area(self):
        return self.large * self.long

    @abstractmethod
    def what_perimeter(self):
        return 2 * (self.large + self.long)
