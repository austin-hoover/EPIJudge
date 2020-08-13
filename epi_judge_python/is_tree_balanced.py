from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import collections


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    Status = collections.namedtuple('Status', ('balanced', 'height'))
    def check(node):
        if not node:
            return Status(True, -1)

        left_status = check(node.left)
        if not left_status.balanced:
            return left_status

        right_status = check(node.right)
        if not right_status.balanced:
            return right_status

        height = max(left_status.height, right_status.height) + 1
        balanced = abs(left_status.height - right_status.height) <= 1
        return Status(balanced, height)

    return check(tree).balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
