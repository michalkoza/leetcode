import pytest

from _997_FindTheTownJudge.JudgeFinder import Solution

test_cases = [
    (2, [[1,2]], 2),
    (3, [[1,3],[2,3]], 3),
    (3, [[1,3],[2,3],[3,1]], -1),
]


@pytest.mark.parametrize("n, trusts, expectation", test_cases)
def test_find_judges(n, trusts, expectation):
    assert Solution().findJudge(n, trusts) == expectation
