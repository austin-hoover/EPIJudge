import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:

    def num_nodes(head):
        x, count = head, 0
        while x:
            x = x.next
            count += 1
        return count

    # Remove offset
    len0, len1 = num_nodes(l0), num_nodes(l1)
    C = len0 - len1
    if C < 0:
        l0, l1, = l1, l0
    for _ in range(abs(C)):
        l0 = l0.next

    # Check for overlap
    for _ in range(len0):
        if l0 is l1:
            return l0
        l0, l1 = l0.next, l1.next
    return None


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
