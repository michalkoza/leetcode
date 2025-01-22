import pytest

from _60_kthPermutation.Perms import Solution

test_cases = [
    (3, 3, "213"),
    (4, 9, "2314"),
    (3, 1, "123"),
]


@pytest.mark.parametrize("n, k,expectation", test_cases)
def test_solution(n, k, expectation):
    assert Solution().getPermutation(n, k) == expectation
