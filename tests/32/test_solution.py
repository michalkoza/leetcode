import pytest

from _32.LongestValidParenthesesMatcher import Solution

test_cases = [

    (")()())", 4),
    ("()(()", 2),
    ("(()", 2),
    ("", 0),
    ("(()()()()()()()()()()", 20),
    ("(()()()()()()()()()())", 22),
    ("()()())(((((((((((()()()()()))))))()))))))())()()()()()()()()()()()()()()()()", 34),
    ("()()())(((((((((((()()()()()))))))()))))))())()()()()()()()()()()()()()()()()()", 34),
    ("()()())(((((((((((()()()()()))))))()))))))())()()()()()()()()()()()()()()()()()()", 36),

]


@pytest.mark.parametrize("s, expectation", test_cases)
def test_solution(s, expectation):
    assert Solution().longestValidParentheses(s) == expectation
