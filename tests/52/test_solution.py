import pytest

from _52_NQueens2.NQueens2 import Solution

test_cases = [
    (4, 2),
    (1, 1),
]


@pytest.mark.parametrize("n,expectation", test_cases)
def test_solution(n, expectation):
    assert Solution().totalNQueens(n) == expectation
