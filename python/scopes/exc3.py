# Reviewer: Anan
import os
import sys


def main():
    information()


def information():
    print(f'OS name: {sys.platform}.\n\
            Logger user: {os.getlogin()}. \n\
            Current WD: {os.getcwd()}.')


if __name__ == '__main__':
    main()
