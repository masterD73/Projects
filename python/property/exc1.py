# Reviewer: Ran
class Point:
    """Calculates the distance from origin (0,0).
     evaluates to a float with maximal precision.
     Coordinates are to be set separately.
     You may use ints or floats only.
     Coordinates are not deletable."""

    def __init__(self, x=0.0, y=0.0):
        """
        Create a Point object of two coordinates.
        :param x: x coordinate.
        :param y: y coordinate.
        """
        self.coordinate_x = x
        self.coordinate_y = y

    def distance_from_origin(self) -> float:
        return (self.__x * self.__x + self.__y * self.__y) ** 0.5

    @property
    def coordinate_x(self) -> float:
        """
        Returns the x coordinate of Point object.
        :return: float
        """
        return self.__x

    @coordinate_x.setter
    def coordinate_x(self, x) -> None:
        """
        Change value of x.
        :param x: Data to insert.
        :return: None
        """
        if not isinstance(x, (int, float)):
            raise TypeError("Point accepts numbers only.")
        self.__x = x

    @coordinate_x.deleter
    def coordinate_x(self) -> None:
        """
        Throw exception to user.
        Deletion not allowed.
        :return: None
        """
        raise Exception("Coordinates are not deletable.")

    @property
    def coordinate_y(self) -> float:
        """
        Returns the y coordinate of Point object.
        :return: float
        """
        return self.__y

    @coordinate_y.setter
    def coordinate_y(self, y) -> None:
        """
        Change value of y.
        :param y: Data to insert.
        :return: None
        """
        if not isinstance(y, (int, float)):
            raise TypeError("Point accepts numbers only.")
        self.__y = y

    @coordinate_y.deleter
    def coordinate_y(self) -> None:
        """
        Throw exception to user.
        Deletion not allowed.
        :return: None
        """
        raise Exception("Coordinates are not deletable.")


help(Point)
p = Point(1, 2.5)
print(f"({p.coordinate_x}, {p.coordinate_y})")
p.coordinate_x = 5
p.coordinate_y = 5
# del p.coordinate_x
print(f"x: {p.coordinate_x}\n"
      f"y: {p.coordinate_y}\n"
      f"Distance from origin: {round(p.distance_from_origin(), 2)}")
assert p.coordinate_x == p.coordinate_y == 5
print("Test passed.")
print("Done.")
