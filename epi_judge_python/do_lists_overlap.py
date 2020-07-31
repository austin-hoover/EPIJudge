import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from is_list_cyclic import has_cycle
from do_terminated_lists_overlap import overlapping_no_cycle_lists

def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:

    def cycle_length(start):
        x, length = start, 0
        while True:
            length += 1
            x = x.next
            if x is start:
                return length

    x0, x1 = has_cycle(l0), has_cycle(l1)
    n_cyclic = (x0 is not None) + (x1 is not None)

    if n_cyclic == 0:
        return overlapping_no_cycle_lists(l0, l1)
    elif n_cyclic == 1:
        return None

    for _ in range(cycle_length(x0)):
        if x0 is x1:
            return x0
        x0 = x0.next

    return None


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_lists_overlap.py',
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
