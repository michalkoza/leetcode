import pytest

from _829_ConsecutiveNumberSum.SumFinderNotMine import Solution

test_cases = [
    (6, 2),
    (85, 4),
    (5, 2),
    (9, 3),
    (15, 4),
    (1, 1),
    (2, 1),
]


@pytest.mark.parametrize("n, expectation", test_cases)
def test_find_judges(n, expectation):
    assert Solution().consecutiveNumbersSum(n) == expectation
