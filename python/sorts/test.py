# -------------------------
# title: Sorting Test
# -------------------------
# -----------------------------
# Description:
# Testing sorting algorithms:
# bubble, selection, insertion,
# merge, count, quick
# -----------------------------
# ------------------------------
# Author: Daniel Merchav.
# Reviewer: Alexander Volkovich.
# AI2 InfinityLabs.
# ------------------------------
from pytest import fixture
from sorts.quick import quick_sort
from sorts.merge import merge_sort
from sorts.bubble import bubble_sort
from sorts.count import counting_sort
from sorts.selection import selection_sort
from sorts.insertion import insertion_sort


@fixture()
def data():
    ls = [4, 2, 61, 3, 5, 1, 2, -4, 0]
    expected = [-4, 0, 1, 2, 2, 3, 4, 5, 61]
    counting_test_ls = [4, 2, 61, 3, 5, 1, 2, 0]
    counting_test_expected = [0, 1, 2, 2, 3, 4, 5, 61]
    return ls, expected, counting_test_ls, counting_test_expected


def test_bubble_sort(data):
    assert bubble_sort(data[0]) == data[1]


def test_selection_sort(data):
    assert selection_sort(data[0]) == data[1]


def test_insertion_sort(data):
    assert insertion_sort(data[0]) == data[1]


def test_merge_sort(data):
    assert merge_sort(data[0]) == data[1]


def test_counting_sort(data):
    assert counting_sort(data[2]) == data[3]


def test_quick_sort(data):
    high = len(data[0]) - 1
    assert quick_sort(data[0], 0, high) == data[1]
