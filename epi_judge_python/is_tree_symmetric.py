from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:

    def check(left, right):
        if not left and not right:
            return True
        elif left and right:
            return (left.data == right.data
                    and check(left.left, right.right) # branch out
                    and check(left.right, right.left)) # branch in
        return False

    return not tree or check(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
