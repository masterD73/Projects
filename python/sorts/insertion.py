# -------------------------
# title: Insertion Sort
# -------------------------
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
def insertion_sort(arr: list) -> list:
    """
    Insertion sort algorithm.
    :param arr: List to be sorted.
    :return: list.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
