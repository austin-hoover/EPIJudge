from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:

    dummy_head = ListNode(0, L)
    back, front = dummy_head, dummy_head.next
    for _ in range(k):
        front = front.next
    while front:
        back, front = back.next, front.next

    # Now back.next is the node to delete.
    back.next = back.next.next

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
