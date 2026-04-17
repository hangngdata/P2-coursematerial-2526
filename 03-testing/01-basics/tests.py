from intervals import overlapping_intervals
import pytest


def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (3, 6))
    assert overlapping_intervals((1, 5), (2, 3))
    assert overlapping_intervals((2, 5), (0, 9))
    assert not overlapping_intervals((2, 5), (7, 10))
    assert not overlapping_intervals((2, 5), (7, 5))
    assert not overlapping_intervals((10, 5), (7, 5))