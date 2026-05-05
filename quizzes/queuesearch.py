# -------------------------
# title: 
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: 
# AI2 InfinityLabs.
# ----------------------------
from queue import Queue
from binarytree import Node


def print_tree(root):
    que = Queue()
    que.put(root)
    while not que.empty():
        node = que.get()
        print(node)
        if node.left:
            que.put(node.left)
        if node.right:
            que.put(node.right)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(6)
    print_tree(root)


if __name__ == '__main__':
    main()
