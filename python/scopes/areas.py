from math import pi


def circle_area(r):
    """Calculates the area of a circle"""
    return pi * r ** 2


def triangle_area(h, w):
    """Calculates the area of a triangle"""
    return h * w / 2


def rectangle_area(h, w):
    """Calculates the area of a rectangle"""
    return h * w


if __name__ == '__main__':
    assert circle_area(1) == pi
    assert triangle_area(2, 4) == 4
    assert rectangle_area(2, 4) == 8
