# -------------------------
# title: 
# -------------------------
# -------------------------
# Description: None.
# -------------------------
# --------------------------
# Author: Daniel Merchav.
# Reviewer: Anan Yablonko.
# AI2 InfinityLabs.
# --------------------------
from time import sleep
from exc1 import InfiniteRange


def main():
    even = (elem for elem in InfiniteRange() if elem % 2 == 0)
    for i in even:
        print(i)
        sleep(0.5)


if __name__ == '__main__':
    main()
