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
from joblib.externals.loky.backend.queues import Queue


def min_large(arr: list, k: int) -> list:
    max_val = max(arr)
    arr_sum = sum(arr)
    sm, lm = 0, 1
    temp, result = [], []
    for val in range(max_val, arr_sum + 1):
        for element in arr:
            if element + sm <= val:
                temp.append(element)
                sm += element
            else:
                result.append(temp)
                temp = [element]
                sm = element
                lm += 1

        if lm == k:
            result.append(temp)
            return result
        lm = 1
        result = []
        temp = []
    print("No solution found.")


def main():
    k = 3
    test_cases = [2, 1, 5, 1, 2, 2, 2], [1, 3, 2, 1, 2, 4, 5]
    test_results = [[2, 1], [5, 1], [2, 2, 2]], [[1, 3], [2, 1, 2, 4], [5]]
    for case, result in zip(test_cases, test_results):
        assert result == min_large(case, k)


if __name__ == '__main__':
    main()
    print("Done.")
