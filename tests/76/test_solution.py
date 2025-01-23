import pytest

from _76_MinWindow.MinWindow import Solution

test_cases = [

    ("a", "a", "a"),
    ("ADOBECODEBANC", "ABC", "BANC"),

    ("a", "aa", ""),
]


@pytest.mark.parametrize("s, t ,expectation", test_cases)
def test_solution(s, t, expectation):
    assert Solution().minWindow(s, t) == expectation
