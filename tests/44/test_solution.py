import pytest

from _44.WildcardMatcher import Solution

test_cases = [
    ("aaabaabababbabbaa", "*b??", True),
    ("adceb", "*a*b", True),
    ("abc", "abc*defghijk", False),
    ("a", "aa", False),
    ("aa", "a*", True),
    ("aa", "aa", True),
    ("a", "", False),
    ("a", "***********", True),
    ("adceb", "*a*b", True),
    ("abbaabbbbababaababababbabbbaaaabbbbaaabbbabaabbbbbabbbbabbabbaaabaaaabbbbbbaaabbabbbbababbbaaabbabbabb",
     "***b**a*a*b***b*a*b*bbb**baa*bba**b**bb***b*a*aab*a**", True),

    ("", "*", True),
    ("a", "***********", True),
    ("aa", "a", False),
    ("aa", "*", True),
    ("cb", "?a", False),
    ("aaabaabababbabbaa", "*b?", False),

    ("", "", True),
    ("", "?", False),

]


@pytest.mark.parametrize("s, p, expectation", test_cases)
def test_solution(s, p, expectation):
    assert Solution().isMatch(s, p) == expectation
