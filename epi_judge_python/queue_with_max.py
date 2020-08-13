from test_framework import generic_test
from test_framework.test_failure import TestFailure
import collections


class QueueWithMax:
    def __init__(self):
        self._entries = collections.deque()
        self._max_candidates = collections.deque()

    def enqueue(self, x: int) -> None:
        self._entries.append(x)
        while self._max_candidates and x > self._max_candidates[-1]:
            self._max_candidates.pop()
        self._max_candidates.append(x)

    def dequeue(self) -> int:
        item = self._entries.popleft()
        if item == self._max_candidates[0]:
            self._max_candidates.popleft()
        return item

    def max(self) -> int:
        if self._max_candidates:
            return self._max_candidates[0]
        raise IndexError('empty queue')


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_with_max.py',
                                       'queue_with_max.tsv', queue_tester))
