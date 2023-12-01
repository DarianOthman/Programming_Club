from calculations import (AreaTriangle, Perimeter_triangle, Area_square, Perimeter_square, Area_rectangle,
                          Perimeter_rectangle)


class Shape:
    def __init__(self, name):
        self.name = name


class Triangle(Shape, AreaTriangle, Perimeter_triangle):
    def __init__(self, name, base, height, second_side, third_side):
        AreaTriangle.__init__(self, base, height, second_side, third_side)
        Perimeter_triangle.__init__(self, base, second_side, third_side)
        super().__init__(name)


class Square(Shape, Area_square, Perimeter_square):
    def __init__(self, name, side):
        Area_square.__init__(self, side)
        Perimeter_square.__init__(self, side)
        super().__init__(name)


class Rectangle(Shape, Area_rectangle, Perimeter_rectangle):
    def __init__(self, name, large, long):
        Area_rectangle.__init__(self, large, long)
        Perimeter_rectangle.__init__(self, large, long)
        super().__init__(name)
