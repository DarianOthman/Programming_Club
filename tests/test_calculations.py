from calculations import Triangle, Square, Rectangle


def test_triangle_area():
    triangle = Triangle("Triangle", 2, 3, 4, 5)
    assert triangle.what_area() == 3


def test_triangle_perimeter():
    triangle = Triangle("Triangle", 2, 3, 4, 5)
    assert triangle.what_perimeter() == 11


def test_square_area():
    square = Square("Square", 4)
    assert square.what_area() == 16


def test_square_perimeter():
    square = Square("Square", 4)
    assert square.what_perimeter() == 16


def test_rectangle_area():
    rectangle = Rectangle("Rectangle", 4, 5)
    assert rectangle.what_area() == 20


def test_rectangle_perimeter():
    rectangle = Rectangle("Rectangle", 4, 5)
    assert rectangle.what_perimeter() == 18
