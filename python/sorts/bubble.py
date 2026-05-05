# ----------------------------
# title: Bubble Sort Algorithm
# ----------------------------
# ----------------------------
# Description:
# Stable comparison algorithm.
# Time complexity: O(n^2)
# Space complexity: O(1)
# ----------------------------
# ------------------------------
# Author: Daniel Merchav.
# Reviewer: Alexander Volkovich.
# AI2 InfinityLabs.
# ------------------------------
def bubble_sort(arr: list) -> list:
    """
    Bubble sort algorithm.
    :param arr: List to be sorted.
    :return: list.
    """
    length = len(arr)

    for i in range(length):
        swapped = False
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped is False:
            break
    return arr
