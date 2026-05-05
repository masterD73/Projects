# -------------------------------
# title: Binary Search Tree Tests
# -------------------------------
# ----------------------------------------------------
# Description: Tests all BST functions and edge cases.
# ----------------------------------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: Daniel Braunstein.
# AI2 InfinityLabs.
# ----------------------------

from bst import BST, Node
from pytest import fixture

NOT_IN_TREE = 666
ELEM_LIST = [10, 20, 50, 0, 20, 1, 100]
ELEM_PRE_ORDER = [10, 0, 1, 20, 50, 20, 100]
ELEM_POST_ORDER = [1, 0, 20, 100, 50, 20, 10]
STR_LIST = "0, 1, 10, 20, 20, 50, 100"
STR_LIST_DBL = "0, 2, 20, 40, 40, 100, 200"


def mult_value(node: Node) -> None:
    """
    Multiply node value by two.
    :param node: Node to be doubled.
    :return: None
    """
    node.value *= 2


@fixture
def tree() -> BST:
    tree = BST()
    yield tree
    del tree


def test_bst_create(tree):
    assert tree is not None and tree.len == 0


def test_bst_insert(tree):
    for element in ELEM_LIST:
        tree.insert(element)
    assert tree.__str__() == STR_LIST


def test_bst_len(tree):
    for element in ELEM_LIST:
        tree.insert(element)
    assert tree.len == len(ELEM_LIST)


def test_bst_contains(tree):
    tree.insert(ELEM_LIST[5])
    assert tree.__contains__(ELEM_LIST[5]) and not tree.__contains__(NOT_IN_TREE)


def test_bst_remove_exist(tree):
    for element in ELEM_LIST:
        tree.insert(element)
    tree.remove(ELEM_LIST[0])
    assert tree.len == len(ELEM_LIST) - 1 and not tree.__contains__(ELEM_LIST[0])


def test_bst_remove_doesnt_exist(tree):
    for element in ELEM_LIST:
        tree.insert(element)
    tree.remove(NOT_IN_TREE)
    assert tree.len == len(ELEM_LIST) and not tree.__contains__(NOT_IN_TREE)


def test_bst_remove_empty(tree):
    boolean_result = tree.remove(ELEM_LIST[5])
    assert tree.len == 0 and not boolean_result


def test_bst_remove_exist_no_child(tree):
    for element in ELEM_LIST:
        tree.insert(element)
    tree.remove(ELEM_LIST[-1])
    assert tree.len == len(ELEM_LIST) - 1 and not tree.__contains__(ELEM_LIST[-1])


def test_bst_remove_exist_one_child(tree):
    for element in ELEM_LIST:
        tree.insert(element)
    tree.remove(ELEM_LIST[3])
    assert tree.len == len(ELEM_LIST) - 1 and not tree.__contains__(ELEM_LIST[3])


def test_for_each_in(tree):
    for element in ELEM_LIST:
        tree.insert(element)
    tree.for_each(BST.IN_ORDER, mult_value)

    assert tree.__str__() == STR_LIST_DBL


def test_for_each_pre(tree):
    for element in ELEM_LIST:
        tree.insert(element)
    ls = []
    tree.for_each(BST.PRE_ORDER, lambda x: ls.append(x.value))
    assert ls == ELEM_PRE_ORDER


def test_for_each_post(tree):
    for element in ELEM_LIST:
        tree.insert(element)
    ls = []
    tree.for_each(BST.POST_ORDER, lambda x: ls.append(x.value))
    assert ls == ELEM_POST_ORDER
