# ------------------------------
# title: Counting Sort Algorithm
# ------------------------------
# --------------------------------
# Description:
# Stable non-comparison algorithm.
# Time complexity: O(n+m)
# Space complexity: O(n+m)
# --------------------------------
# ------------------------------
# Author: Daniel Merchav.
# Reviewer: Alexander Volkovich.
# AI2 InfinityLabs.
# ------------------------------
def counting_sort(arr: list) -> list:
    """
    Counting sort algorithm.
    :param arr: List to be sorted.
    :return: list.
    """
    length = len(arr)
    maximum = max(arr)
    output_arr = [0] * length
    count_arr = [0] * (maximum + 1)

    for elem in arr:
        count_arr[elem] += 1
    for i in range(1, maximum + 1):
        count_arr[i] += count_arr[i - 1]

    for i in range(length - 1, -1, -1):
        output_arr[count_arr[arr[i]] - 1] = arr[i]
        count_arr[arr[i]] -= 1
    arr[:] = output_arr
    return arr
