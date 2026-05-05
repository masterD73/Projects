# -------------------------
# title: Infinite Range
# -------------------------
# -------------------------
# Description: None.
# -------------------------
# --------------------------
# Author: Daniel Merchav.
# Reviewer: Anan Yablonko.
# AI2 InfinityLabs.
# --------------------------
from time import sleep


def InfiniteRange(num: int = 0) -> iter:
    """
    Range generator from num to infinity.
    :param num: Starting range number.
    :return: generator object
    """
    while True:
        yield num
        num += 1


def main():
    for i in InfiniteRange():
        print(i + 1)
        sleep(0.5)


if __name__ == '__main__':
    main()
