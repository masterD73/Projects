# -------------------------
# title: Hanoi Tower
# -------------------------
# -------------------------
# Description: Quiz
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: 
# AI2 InfinityLabs.
# ----------------------------

def hanoi_tower(n, frm, to, via):

    if n == 1:
        print(f"Move disk 1 from", frm, "to", to)
    else:
        hanoi_tower(n - 1, frm, via, to)
        print(f"Move disk {n} from", frm, "to", to)
        hanoi_tower(n - 1, via, to, frm)


def main():
    n = 3
    frm = 'A'
    to = 'C'
    via = 'B'
    hanoi_tower(n, frm, to, via)


if __name__ == '__main__':
    main()
    print('Done.')
