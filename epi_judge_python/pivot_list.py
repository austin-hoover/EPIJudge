import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def remove_and_insert(insert_after, remove_after):
    # Remove
    node = remove_after.next
    remove_after.next = remove_after.next.next
    # Insert
    node.next = insert_after.next
    insert_after.next = node


def list_pivoting(L: ListNode, x: int) -> Optional[ListNode]:

    if L is None or L.next is None:
        return L

    dummy_head = ListNode(0, L)

    # Find first pivot
    pivot = dummy_head
    while pivot.next and pivot.next.data < x:
        pivot = pivot.next

    # Insert after pivot: all nodes with node.data < x
    node = pivot
    while node.next:
        if node.next.data < x:
            remove_and_insert(pivot, node)
            pivot = pivot.next
        else:
            node = node.next

    # Update pivot
    while pivot.next and pivot.next.data <= x:
        pivot = pivot.next

    # Insert after pivot: all nodes with node.data == x
    node = pivot
    while node.next:
        if node.next.data == x:
            remove_and_insert(pivot, node)
            pivot = pivot.next
        else:
            node = node.next

    return dummy_head.next


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pivot_list.py', 'pivot_list.tsv',
                                       list_pivoting_wrapper))
