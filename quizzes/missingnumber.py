# -------------------------
# title: Missive Integers
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: 
# AI2 InfinityLabs.
# ----------------------------

def missing_int_naive(ls: list) -> int:
    length = len(ls)
    if length == 0:
        return 0
    for i in range(length):
        if i != ls[i]:
            return i
    return ls[-1] + 1


def missing_int_binary_search(ls: list) -> int:
    high = len(ls) - 1
    low = 0
    while low <= high:
        mid = (low + high) // 2
        if ls[mid] == mid:
            low = mid + 1
        else:
            high = mid - 1
    return low


def main():
    ls = list(range(10000))
    ls.remove(5000)
    lists = [[0, 1, 3, 4, 6, 1984], [1, 2, 3, 4, 6, 1984], [], [0, 1, 2], list(range(100)), ls, [0]]
    results = [2, 0, 0, 3, 100, 5000, 1]
    tests = zip(lists, results)
    for t, r in tests:
        assert missing_int_binary_search(t) == r
    print("Done.")


if __name__ == '__main__':
    main()
