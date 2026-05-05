# Reviewer: Alexander.
from errno import ECHILD


class Point:
    def __init__(self, x=0.0, y=0.0) -> None:
        if (not isinstance(x, (int, float))
                or not isinstance(y, (int, float))):
            raise TypeError("Point accepts numbers only.")
        self.x = x
        self.y = y

    def distance_from_origin(self) -> float:
        return (self.x * self.x + self.y * self.y) ** 0.5


p = Point(1, 2.5)
print(f"x: {p.x}\n"
      f"y: {p.y}\n"
      f"Distance from origin: {round(p.distance_from_origin(), 2)}")
