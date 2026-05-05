# -------------------------
# title: Island Counter
# -------------------------
# -------------------------
# Description:
# TC: O(n)
# SC: O(n)
# -------------------------
# -------------------------
# Author: Daniel Merchav.
# Reviewer: None.
# AI2 InfinityLabs.
# -------------------------


def main():
    islands0 = [[0]]
    islands1 = [[1]]
    islands2 = [[0, 1],
                [1, 0]]
    islands3 = [[1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 1, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0]]
    assert island_number(islands0) == 0
    assert island_number(islands1) == 1
    assert island_number(islands2) == 2
    assert island_number(islands3) == 3
    print("Test Done.")


def change_land_to_water(ls: list, row: int, col: int) -> None:
    if row < 0 or col < 0 or row >= len(ls) or col >= len(ls[row]) or ls[row][col] == 0:
        return
    ls[row][col] = 0

    change_land_to_water(ls, row - 1, col)
    change_land_to_water(ls, row + 1, col)
    change_land_to_water(ls, row, col - 1)
    change_land_to_water(ls, row, col + 1)


def island_number(ls: list) -> int:
    counter = 0
    ls_copy = [row[:] for row in ls]

    for row in range(len(ls)):
        for col in range(len(ls[row])):
            if ls_copy[row][col] == 1:
                counter += 1
                change_land_to_water(ls_copy, row, col)
    return counter


if __name__ == '__main__':
    main()
