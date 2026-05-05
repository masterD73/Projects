# -------------------------
# title: Binary Search Tree
# -------------------------
# --------------------------------
# Description: BST & Node classes.
# --------------------------------
# -------------------------------
# Author: Daniel Merchav.
# Reviewer #1: Daniel Braunstein.
# Reviewer #2: Anan Yablonko.
# AI2 InfinityLabs.
# -------------------------------
from dataclasses import dataclass
from typing import Any, Self, Callable


@dataclass
class Node:
    value: Any = None
    left: Self | None = None
    right: Self | None = None


class BST:
    """A class representation of a Binary Search Tree"""

    IN_ORDER = "in"
    PRE_ORDER = "pre"
    POST_ORDER = "post"

    def __init__(self, comp: Callable[[Any, Any], int | float] = lambda x, y: x - y) -> None:
        """
        Initializing a Binary search tree instance.
        :param comp: function that returns the value of arg1 - arg2
        """
        self.root = None
        self.compare = comp
        self.len = 0

    def __iter__(self):
        return BSTIterator(self.root)

    def is_empty(self) -> bool:
        """
        Check whether a tree is empty.
        :return: True or False
        """
        return self.root is None

    def insert(self, value: int | float) -> None:
        """
        insert a given element into the tree.
        :param value: The number to be inserted.
        :return: None
        """
        curr = self.root
        new_node = Node(value)
        if self.is_empty():
            self.len += 1
            self.root = new_node
            return

        while True:
            comp = self.compare(curr.value, value)
            if comp <= 0:
                if curr.right is None:
                    curr.right = new_node
                    self.len += 1
                    break
                else:
                    curr = curr.right
            else:
                if curr.left is None:
                    curr.left = new_node
                    self.len += 1
                    break
                else:
                    curr = curr.left

    def _in_order(self, curr: Node, action_func: Callable[[Node], None]) -> None:
        """
        Transverse over tree in an in-order order.
        :param curr: The root where transversing starts.
        :param action_func: Function to act on every tree element.
        :return: None
        """
        if curr:
            self._in_order(curr.left, action_func)
            action_func(curr)
            self._in_order(curr.right, action_func)

    def _pre_order(self, curr, action_func: Callable[[Node], None]) -> None:
        """
        Transverse over tree in a pre-order order.
        :param curr: The root where transversing starts.
        :param action_func: Function to act on every tree element.
        :return: None
        """
        if curr:
            action_func(curr)
            self._pre_order(curr.left, action_func)
            self._pre_order(curr.right, action_func)

    def _post_order(self, curr: Node, action_func: Callable[[Node], None]) -> None:
        """
        Transverse over tree in a post-order order.
        :param curr: The root where transversing starts.
        :param action_func: Function to act on every tree element.
        :return: None
        """
        if curr:
            self._post_order(curr.left, action_func)
            self._post_order(curr.right, action_func)
            action_func(curr)

    def for_each(self, traversal_type: str, action_func: Callable[[Node], None]) -> None:
        """
        Applies 'action_func' to each node in the tree in a 'traversal_type' fashion.
        :param traversal_type: One of: IN_ORDER = "in", PRE_ORDER = "pre", POST_ORDER = "post"
        :param action_func: A function to be applied to each node of the tree.
        :return: None
        """
        match traversal_type:
            case BST.PRE_ORDER:
                self._pre_order(self.root, action_func)
            case BST.IN_ORDER:
                self._in_order(self.root, action_func)
            case BST.POST_ORDER:
                self._post_order(self.root, action_func)

    def __len__(self) -> int:
        """
        Refers to the number of tree elements.
        :return: The number of elements of in the tree.
        """
        return self.len

    @staticmethod
    def _get_successor(curr: Node) -> Node | None:
        """
        Helper function to get the successor element of a given node in tree.
        :param curr: Root to start the current recursion.
        :return: Either a Node or a None object.
        """
        curr = curr.right
        if curr is None:
            return curr
        while curr.left is not None:
            curr = curr.left
        return curr

    def _del_node(self, curr: Node, value: int | float) -> (Node, bool):
        """
        Helper function to remove a given element from the tree.
        :param curr: Root to start the current recursion.
        :param value: Value to be deleted from tree.
        :return: Tuple of Node and bool.
        """
        if curr is None:
            return curr, False

        if curr.value > value:
            curr.left, is_removed = self._del_node(curr.left, value)
        elif curr.value < value:
            curr.right, is_removed = self._del_node(curr.right, value)

        else:
            if curr.left is None:
                return curr.right, True

            if curr.right is None:
                return curr.left, True

            successor = self._get_successor(curr)
            curr.value = successor.value
            curr.right, is_removed = self._del_node(curr.right, successor.value)

        return curr, is_removed

    def remove(self, value: int | float) -> bool:
        """
        Removes a given element from the tree.
        :param value: The element to be removed.
        :return: True if the element was removed, False if it wasn't found.
        """
        curr = self.root
        is_removed = self._del_node(curr, value)[1]
        if is_removed:
            self.len -= 1

        return is_removed

    def __contains__(self, value: int | float) -> bool:
        """
        Check if a value is contained in a given tree.
        :param value: The value to be searched.
        :return: True if the element is in the tree, False otherwise.
        """
        curr = self.root
        while curr:
            comp = self.compare(curr.value, value)
            if comp == 0:
                return True
            elif comp < 0:
                curr = curr.right
            else:
                curr = curr.left
        return False

    def __str__(self) -> str:
        """
        :return: a string representation of the tree in-order.
        """
        curr = self.root
        nodes = []
        if curr:
            self.for_each(BST.IN_ORDER, lambda node: nodes.append(str(node.value)))
        return ', '.join(nodes).rstrip()


class BSTIterator:
    def __init__(self, curr: Node):
        self.stack = []
        self._leftmost_inorder(curr)

    def _leftmost_inorder(self, curr: Node):
        while curr:
            self.stack.append(curr)
            curr = curr.left

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration

        top_node = self.stack.pop()
        if top_node.right:
            self._leftmost_inorder(top_node.right)

        return top_node


def main():
    ls = [10, 20, 50, 0, 20, 1, 100]
    tree = BST()
    for element in ls:
        tree.insert(element)
    tree.for_each(tree.IN_ORDER, lambda node: print(node.value, end=" "))
    list(tree)
    len(tree)
    print("")
    for elem in tree:
        print(elem.value)
    for element in ls:
        print(f"element {element} - {tree.__contains__(element)}")
    print(f"element {666} - {tree.__contains__(666)}")
    print(tree.__str__())


if __name__ == '__main__':
    main()
