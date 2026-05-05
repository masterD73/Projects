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
def main():
    arr1 = [2, 4, 1, 6, 4, 2, 4, 3, 5]
    arr2 = [2, 4, 1, 6, 4, 2, 4, 3, 5]
    assert jump(arr1)
    assert not jump(arr2)

    print("Done.")


def jump(arr: list, index: int = 0, tracker: list = []) -> bool:
    if index == len(arr) - 1:
        return True
    if index >= len(arr) or index < 0 or index in tracker:
        return False
    tracker.append(index)
    return jump(arr, index + arr[index]) or jump(arr, index - arr[index])


if __name__ == '__main__':
    main()
