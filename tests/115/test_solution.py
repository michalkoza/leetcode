import pytest

from _115_DistinctSubstrings.Finder import Solution

test_cases = [
    ("rabbbit", "rabbit", 3),
    ("babgbag", "bag", 5),
    ("a", "b", 0),
    ("a", "a", 1),
    ("aaa", "aa", 3),
    ("ababab", "ab", 6)
    ]


@pytest.mark.parametrize("s ,t, expectation", test_cases)
def test_solution(s, t, expectation):
    assert Solution().numDistinct(s, t) == expectation, f"{s} {t} {expectation}"
