from itertools import permutations

import pytest
from mergesort import *


@pytest.mark.parametrize('ns', [
    [x for x in range(length)] for length in range(100)
])
def test_split_in_two(ns):
    left, right = split_in_two(ns)
    assert ns == left + right
    assert abs(len(left) - len(right)) <= 1


@pytest.mark.parametrize('left', [
    [],
    [1],
    [4, 10, 15],
    [2, 5, 10, 34],
    [2, 6, 6, 31, 54],
    [11, 21, 31, 90, 110]
])
@pytest.mark.parametrize('right', [
    [],
    [1],
    [7, 32, 78],
    [12, 13, 19, 24],
    [22, 23, 64, 65, 69],
    [11, 11, 11, 32, 46]
])

def test_merge_sorted(left, right):
    actual = merge_sorted(left, right)
    expected = sorted(left + right)
    assert expected == actual


@pytest.mark.parametrize('ns, expected', [
    (list(permutation), ns)
    for ns in [[], [1], [1, 2], [3, 4, 4, 6], [2, 2, 4, 6, 9, 15, 19]]
    for permutation in permutations(ns)
])

def test_merge_sort(ns, expected):
    assert merge_sort(ns) == expected