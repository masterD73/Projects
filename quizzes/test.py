# -------------------------
# title: 
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: 
# AI2 InfinityLabs.
# ----------------------------

amaze = [[0, 0, 1, 1, 1, 1],
         [1, 0, 0, 1, 1, 1],
         [1, 1, 0, 0, 1, 1],
         [1, 1, 1, 0, 0, 0]]


def change_land_to_water(ls: list, row: int, col: int) -> tuple:
    if row < 0 or col < 0 or row >= len(ls) or col >= len(ls[row]) or ls[row][col] == 1:
        return row, col
    ls[row][col] = 1

    change_land_to_water(ls, row - 1, col)
    change_land_to_water(ls, row + 1, col)
    change_land_to_water(ls, row, col - 1)
    change_land_to_water(ls, row, col + 1)


def maze(ls: list) -> tuple:
    counter = 0
    ls_copy = [row[:] for row in ls]

    for row in range(len(ls)):
        for col in range(len(ls[row])):
            if ls_copy[row][col] == 0:
                index = change_land_to_water(ls_copy, row, col)

    return index


print(maze(amaze))
