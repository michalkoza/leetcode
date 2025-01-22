import pytest

from _51_NQueens.NQueens import Solution

test_cases = [
    (4, [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]),
    (1, [["Q"]]),
]


def to_set(solutions):
    return {"|".join(solution) for solution in solutions}


@pytest.mark.parametrize("n,expectation", test_cases)
def test_solution(n, expectation):
    results = to_set(Solution().solveNQueens(n))
    exp = to_set(expectation)
    assert to_set(Solution().solveNQueens(n)) == to_set(expectation)
