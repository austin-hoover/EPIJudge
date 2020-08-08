from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order_recursive(tree: BinaryTreeNode) -> List[List[int]]:
    L = []
    if not tree:
        return L

    def update(node, level):
        if len(L) <= level:
            L.append([])
        L[level].append(node.data)
        if node.left:
            update(node.left, level + 1)
        if node.right:
            update(node.right, level + 1)
    update(tree, 0)
    return L

def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    L = []
    if not tree:
        return L

    nodes = [tree]
    while nodes:
        L.append([node.data for node in nodes])
        nodes = [child for node in nodes
                 for child in (node.left, node.right) if child]
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('binary_tree_depth_order_recursive.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
