import pytest

from _828.SubstringCharCounter import Solution

test_cases = [
    ("ABC", 10),
    ("ABA", 8),
    ("LEETCODE", 92),
    ("D", 1),
    ("AAAAAAAAAA", 10),
    ("ABABA", 16),
]


@pytest.mark.parametrize("s, expectation", test_cases)
def test_find_judges(s, expectation):
    assert Solution().uniqueLetterString(s) == expectation
