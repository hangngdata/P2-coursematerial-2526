from mystatistics import average
import pytest
from pytest import approx

@pytest.mark.parametrize('ns, expected', [
    ([1], 1.0),
    ([1, 2], 1.5),
    ([1, 2, 3, 4], 2.5),
    ([0.1, 0.1, 0.1], 0.1)
])
def test_matching_parentheses(ns, expected):
    assert approx(average(ns), abs=0.01) == expected, f"Expected {expected} but get {average(ns)}"