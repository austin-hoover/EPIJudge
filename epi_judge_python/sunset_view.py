from typing import Iterator, List
import collections
from test_framework import generic_test

def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:

    Building = collections.namedtuple('Building', ('idx', 'height'))

    sunset_views, n = [], len(sequence)
    for idx, height in enumerate(sequence):
        while sunset_views and sunset_views[-1].height <= height:
            sunset_views.pop()
        sunset_views.append(Building(idx, height))
    return [building.idx for building in reversed(sunset_views)]




def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
