# -------------------------
# title: Recaman's Sequence
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: 
# AI2 InfinityLabs.
# ----------------------------
def recaman(limit=10):
    visited = {0}
    n = 0
    a = 0

    while n <= limit:
        yield a
        n += 1
        a -= n
        if a < 0 or a in visited:
            a += 2 * n
        visited.add(a)


def main():
    j = 0
    ls = [0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10]

    for i in recaman(len(ls) - 1):
        assert i == ls[j]
        j += 1
    print("Done.")


if __name__ == '__main__':
    main()
