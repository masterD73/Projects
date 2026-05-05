# -------------------------
# title: 
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ------------------------------
# Author: Daniel Merchav.
# Reviewer: Alexander Volkovich.
# AI2 InfinityLabs.
# ------------------------------
import math


def find_square_root(function: tuple) -> tuple | int | float:
    a, b, c = function
    if a == 0:
        if b != 0:
            return -c / b
        else:
            return 0
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return ()
    elif delta == 0:
        return (-b / (2 * a),)
    first = (-b + delta ** 0.5) / (2 * a)
    second = (-b - delta ** 0.5) / (2 * a)
    return first, second


def find_root(f, precision):
    high = 1
    low = -1
    while high - low > precision:
        mid = (high + low) / 2
        if abs(f(mid)) < precision:
            return mid
        elif f(mid) > 0:
            high = mid
        else:
            low = mid
    return (high + low) / 2


def function(x):
    return (x - 0.5) * (x + 3) * (x + 8)


def main():
    f = (2, 1, 0)
    # Updated after uncommenting and fixing find_square_root function
    print(find_square_root(f))
    print(find_root(function, 1e-8))


if __name__ == '__main__':
    main()
