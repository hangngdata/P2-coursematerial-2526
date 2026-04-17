import pytest
from parentheses import matching_parentheses


@pytest.mark.parametrize('string', [
    ("(This is a remarks)"),
    ("Every test should not affect each other's output (isolation)"),
    ("Today (17 April) is a Friday (Third Friday of the month)"),
    ("return max(sum(1, 2), min(10, 3))")
])
def test_matching_parentheses(string):
    assert matching_parentheses(string), f"All parentheses are matched"


@pytest.mark.parametrize('string', [
    ("This ( is not closed"),
    ("Close ) but not open."),
    ("Two openings (( but only one closing )"),
    ("There are two closings )) but only one open ("),
    ("Close ) before open ("),
])
def test_nonmatching_parentheses(string):
    assert not matching_parentheses(string), f"Parentheses are not matched"