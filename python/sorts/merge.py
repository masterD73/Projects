# ---------------------------
# title: Merge Sort Algorithm
# ---------------------------
# ----------------------------
# Description:
# Stable comparison algorithm.
# Time complexity: O(n*log(n))
# Space complexity: O(n)
# ----------------------------
# ------------------------------
# Author: Daniel Merchav.
# Reviewer: Alexander Volkovich.
# AI2 InfinityLabs.
# ------------------------------
def merge_sort(arr: list) -> list:
    """
    Merge sort algorithm.
    :param arr: List to be sorted.
    :return: list.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_side = arr[:mid]
    right_side = arr[mid:]

    sorted_left = merge_sort(left_side)
    sorted_right = merge_sort(right_side)

    result = []
    i = j = 0
    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] < sorted_right[j]:
            result.append(sorted_left[i])
            i += 1
        else:
            result.append(sorted_right[j])
            j += 1
    result.extend(sorted_left[i:])
    result.extend(sorted_right[j:])
    arr[:] = result
    return result
