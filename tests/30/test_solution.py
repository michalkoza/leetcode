import pytest

from _30.SubstringWithConcatenationOfAllWordsFinder import Solution

test_cases = [

    ("ababababababababaabab", ["abab", "baba"], [13]),
    ("ababababababababaababxy", ["xy"], [21]),
    ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
    ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
    ("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12]),
]


@pytest.mark.parametrize("s, words, expectation", test_cases)
def test_solution(s, words, expectation):
    assert Solution().findSubstring(s, words) == expectation
