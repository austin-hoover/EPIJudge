from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:

    if L is None:
        return L

    # Create cyclic list
    tail, n_nodes = L, 1
    while tail.next:
        n_nodes += 1
        tail = tail.next
    tail.next = L

    # Find new head node
    new_head = tail.next
    for _ in range(n_nodes - (k % n_nodes)):
        new_head = new_head.next

    # Find new tail node
    new_tail = L
    while new_tail.next is not new_head:
        new_tail = new_tail.next
    new_tail.next = None

    return new_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
