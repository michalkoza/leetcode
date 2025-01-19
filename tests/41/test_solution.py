import pytest

from _41.SmallestMissingIntFinder import Solution

test_cases = [
    ([2,1], 3),
    ([1], 2),
    ([1, 2, 0], 3),
    ([3, 4, -1, 1], 2),
    ([7, 8, 9, 11, 12], 1),

]


@pytest.mark.parametrize("input, expectation", test_cases)
def test_solution(input, expectation):
    assert Solution().firstMissingPositive(input) == expectation
