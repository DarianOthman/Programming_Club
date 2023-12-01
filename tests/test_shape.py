# import pytest
from shape import Shape, Rectangle, Square, Triangle


def test_shape():
    shape = Shape("Triangle")
    assert shape.name == "Triangle"


def test_rectangle():
    rectangle = Rectangle("Rectangle", 2, 3)
    assert rectangle.name == "Rectangle"
    assert rectangle.large == 2
    assert rectangle.long == 3
    assert rectangle.what_area() == 6
    assert rectangle.what_perimeter() == 10


def test_square():
    square = Square("Square", 2)
    assert square.name == "Square"
    assert square.side == 2
    assert square.what_area() == 4
    assert square.what_perimeter() == 8


def test_triangle():
    triangle = Triangle("Triangle", 2, 3, 4, 5)
    assert triangle.name == "Triangle"
    assert triangle.base == 2
    assert triangle.height == 3
    assert triangle.second_side == 4
    assert triangle.third_side == 5
    assert triangle.what_area() == 3
    assert triangle.what_perimeter() == 11
