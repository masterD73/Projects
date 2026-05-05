def num_exists(num: int | float, ls: list) -> bool:
    high = len(ls) - 1
    low = 0
    mid = high // 2
    if ls[low] > ls[high]:
        low = high
        high = 0
    while high != low:
        if ls[mid] > num:
            high = mid
            mid = (high + low) // 2
        elif ls[mid] < num:
            low = mid
            mid = (high + low) // 2
        else:
            return True
    return False


ls = [3, 1, -5, -10, -11, -12, -13]
print(num_exists(-11, ls))
