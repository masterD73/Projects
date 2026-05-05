# -------------------------
# title: Max Ones Subarray
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: None.
# AI2 InfinityLabs.
# ----------------------------

def max_ones(ls: list, n: int) -> int:
    count_0 = 0
    count_1 = 0
    count_1_max = 0
    index = 0
    for i in range(len(ls)):
        if ls[i] == 1:
            print("before count", count_1)
            count_1 += 1
            print("after count", count_1)
            if count_1 > count_1_max:
                print("before max", count_1_max)
                count_1_max = count_1
                print("after max", count_1_max)
                count_1 = 0
                index = i
                print("index:", i)
    while index < len(ls) - 1 and count_0 <= n:
        if ls[index + 1] == 0:
            count_0 += 1
            ls[index + 1] = 1
        else:
            break
    while index - count_1 >= 0 and count_0 <= n:
        if ls[index - count_1 - 1] == 0:
            count_0 += 1
            ls[index + 1] = 1
        else:
            break
    if count_0 >= n:
        return count_1_max + n
    return count_1_max + count_0


example = [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0]
print(max_ones(example, 2))
