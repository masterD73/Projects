# -------------------------
# title: 
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ------------------------
# Author: Daniel Merchav.
# Reviewer: Anan Yablonko.
# AI2 InfinityLabs.
# ------------------------
import re


def acceptor(numbers: str) -> bool:
    return re.match("0[01]*0$", numbers) is not None


def main():
    number1 = "0101100"
    number2 = "010111"
    assert acceptor(number1)
    assert acceptor(number2) is False
    print("Tests done.")


if __name__ == '__main__':
    main()
