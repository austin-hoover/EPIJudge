from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity: int) -> None:
        self._entries = [0] * capacity
        self._head = self._tail = 0

    def enqueue(self, x: int) -> None:
        self._entries[self._tail] = x
        self._tail += 1
        if self._tail == len(self._entries):
            self._entries += [0] * len(self._entries)

    def dequeue(self) -> int:
        if self.size() == 0:
            return
        x = self._entries[self._head]
        for i in range(self._tail):
            self._entries[i] = self._entries[i + 1]
        self._entries[self._tail] = 0
        self._tail -= 1
        return x

    def size(self) -> int:
        return self._tail - self._head


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
