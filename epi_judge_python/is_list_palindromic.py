from list_node import ListNode
from test_framework import generic_test


def reverse_list(head):
    dummy = ListNode()
    while head:
        dummy.next, head.next, head = head, dummy.next, head.next
    return dummy.next


def is_linked_list_a_palindrome(L: ListNode) -> bool:

    # Find midpoint of list
    fast = slow = L
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    node1, node2 = L, reverse_list(slow)
    while node1 and node2:
        if node1.data != node2.data:
            return False
        node1, node2 = node1.next, node2.next
    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
