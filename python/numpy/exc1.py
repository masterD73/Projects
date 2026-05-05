# -------------------------
# title: Who's Faster?
# -------------------------
# -------------------------
# Description:
# Series of tests to
# determine if lists or
# arrays are faster.
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: Netta Savin.
# AI2 InfinityLabs.
# ----------------------------
import math
from random import randint
from timeit import timeit
import numpy as np


def dot(ls1, ls2):
    if len(ls1) != len(ls2):
        return 0
    return sum(i[0] * i[1] for i in zip(ls1, ls2))


def add_constant_list(ls, constant):
    for i in range(len(ls)):
        ls[i] += constant
    return ls


def add_constant_array(ls, constant):
    return ls + constant


def create_list(n=10):
    return [0] * n


def create_array(n=3):
    return np.zeros(n)


def cat_list(ls1, ls2):
    return ls1 + ls2


def cat_array(arr1, arr2):
    return np.concatenate((arr1, arr2))


def exponentiation_list(ls, n):
    return [2 ** x for x in ls]


def exponentiation_array(array):
    return np.exp(array)


def print_elements_list(ls):
    print(ls)


def print_elements_array(arr):
    print(arr)


def main():
    constant = 5
    runs = 1000
    num_range = 100
    list_add = list(range(num_range))
    array_add = np.array(list(range(num_range)))
    print(array_add)

    time_create_list = timeit(create_list, number=runs)
    time_create_array = timeit(create_array, number=runs)

    time_add_list = timeit(lambda: add_constant_list(list_add, constant), number=runs)
    time_add_array = timeit(lambda: add_constant_array(array_add, constant), number=runs)

    dot_list = timeit(lambda: dot(list_add, list_add), number=runs)
    dot_array = timeit(lambda: np.dot(array_add, array_add), number=runs)

    exponentiation_ls = timeit(lambda: exponentiation_list(list_add, constant), number=runs)
    exponentiation_arr = timeit(lambda: exponentiation_array(array_add), number=runs)

    cat_ls = timeit(lambda: cat_list(list_add, list_add), number=runs)
    cat_arr = timeit(lambda: cat_array(array_add, array_add), number=runs)

    print_ls = timeit(lambda: print_elements_list(list_add), number=runs)
    print_arr = timeit(lambda: print_elements_array(array_add), number=runs)

    if time_create_list < time_create_array:
        print("Creating a list is faster than an array.")
    else:
        print("Creating an array is faster than a list.")

    if time_add_list < time_add_array:
        print("Adding a constant to a list is faster than on an array.")
    else:
        print("Adding a constant to an array is faster than on a list.")

    if dot_list < dot_array:
        print("Dotting a list is faster than on an array.")
    else:
        print("Dotting an array is faster than on a list.")

    if exponentiation_ls < exponentiation_arr:
        print("Exponentiation on a list is faster than on an array.")
    else:
        print("Exponentiation on an array is faster than on a list.")

    if cat_ls < cat_arr:
        print("Merging on a list is faster than on an array.")
    else:
        print("Merging on an array is faster than on a list.")
    if print_ls < print_arr:
        print("Printing elements on a list is faster than on an array.")
    else:
        print("Printing elements on an array is faster than on a list.")


def random_matrix(n: int, m: int) -> np.array:
    np.random.seed(0)
    return np.concatenate((np.random.rand(n, m), np.ones([n, 1])), 1)


if __name__ == '__main__':
    main()


def example():
    my_range = 3
    my_const = 10
    runs = 100
    while True:
        ls = list(range(my_range))
        arr = np.array(range(my_range))
        for i in range(1, my_range):
            exponentiation_ls = timeit(lambda: exponentiation_list(ls, my_const), number=runs)
            exponentiation_arr = timeit(lambda: exponentiation_array(arr), number=runs)
            if exponentiation_arr < exponentiation_ls:
                print(f"At a size of {i}, arrays are more efficient than lists at exponentiation.")
                return
        my_range += 1


example()
