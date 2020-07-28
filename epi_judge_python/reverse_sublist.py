from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:

    dummy_head = sublist_head = ListNode(0, L)

    for _ in range(start - 1):
        sublist_head = sublist_head.next

    current = sublist_head.next
    for _ in range(finish - start):
        temp = current.next
        current.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
