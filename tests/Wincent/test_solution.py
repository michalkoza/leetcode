import pytest

from Wincent.Wincent import Solution

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

    Solution().longestValidParentheses()
    with open("output.txt", "r") as result_file:
        res = [int(line.strip()) for line in result_file]

    assert res == list(range(10))
