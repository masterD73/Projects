# -------------------------
# title: Range Class
# -------------------------
# -------------------------
# Description: None.
# -------------------------
# -------------------------.
# Author: Daniel Merchav.
# Reviewer: Anan Yablonko.
# AI2 InfinityLabs.
# -------------------------.
from random import randint


class MyRange:
    def __init__(self, end: int = 10, start: int = 0, step: int = 1) -> None:
        if not isinstance(end, int) or not isinstance(start, int):
            raise TypeError("MyRange accepts integers only.")
        if step <= 0:
            ValueError("Step must be a positive integer.")
        if start >= end:
            raise ValueError("Start of iteration must be lower than the end.")
        self.__end = end
        self.__num = start
        self.__start = start
        self.__step = step

    def __len__(self):
        abs_step = abs(self.__step)
        return (self.__end - self.__start + 1) // abs_step

    def __iter__(self):
        while self.__num < self.__end:
            yield self.__num
            self.__num += self.__step

    def __getitem__(self, index: int) -> int:
        if not isinstance(index, int):
            raise TypeError("MyRange accepts integers only.")
        if index < -len(self) or index >= len(self):
            raise IndexError("Index is out of range.")
        if index < 0:
            return self.__start + self.__step * (len(self) + index)
        return self.__start + index * self.__step

    @property
    def elements(self):
        return self.__end, self.__num, self.__step

    @elements.setter
    def elements(self, end: int, start: int = 0, step: int = 1):
        if (not isinstance(end, int) or
                not isinstance(start, int) or
                not isinstance(step, int) or step < 0):
            raise TypeError("MyRange accepts integers only.")
        if step <= 0:
            ValueError("Step must be a positive integer.")
        if start >= end:
            raise ValueError("Start of iteration must be lower than the end.")
        self.__end = end
        self.__num = start
        self.__step = step


def main():

    end, start, step = randint(21, 40), randint(0, 20), randint(1, 4)
    range_11 = MyRange(end, start, step)
    length = (end - start + 1) // step
    assert len(range_11) == length
    assert range_11[0] == start == range_11[-len(range_11)]
    assert (list(range_11) == list(range(start, end, step)))
    assert range_11[-1] == range_11[len(range_11) - 1]
    print("tests Done.")


if __name__ == '__main__':
    main()
