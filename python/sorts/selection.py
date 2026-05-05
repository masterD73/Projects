# -------------------------------
# title: Selection Sort Algorithm
# -------------------------------
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
def selection_sort(arr: list) -> list:
    """
    Selection sort algorithm.
    :param arr: List to be sorted.
    :return: list.
    """
    length = len(arr)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
