# Reviewer: Anan
import sys


def cmd_in_out():
    print(*sys.argv[:0:-1], sep="\n")


def main():
    cmd_in_out()


if __name__ == '__main__':
    main()
