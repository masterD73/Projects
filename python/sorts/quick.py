# ---------------------------
# title: Quick Sort Algorithm
# ---------------------------
# ------------------------------------
# Description:
# Unstable comparison algorithm.
# Average time complexity: O(n*log(n))
# Average space complexity: O(log(n))
# ------------------------------------
# ------------------------------
# Author: Daniel Merchav.
# Reviewer: Alexander Volkovich.
# AI2 InfinityLabs.
# ------------------------------
def partition(arr: list, low: int, high: int) -> int:
    """
    Helper function to put pivot in place.
    :param arr: List to be sorted.
    :param low: Beginning of list.
    :param high: End of list.
    :return: list.
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[high], arr[i + 1] = arr[i + 1], arr[high]

    return i + 1


def quick_sort(arr: list, low: int, high: int) -> list:
    """
    Counting sort algorithm.
    :param arr: List to be sorted.
    :param low: Beginning of list.
    :param high: End of array.
    :return: list.
    """
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
        return arr


ls = [40, 10, 1, 202]
quick_sort(ls, 0, len(ls) - 1)
