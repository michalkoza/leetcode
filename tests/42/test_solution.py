import pytest

from _42.WaterCollector2 import Solution

test_cases = [
    ([5, 5, 1, 7, 1, 1, 5, 2, 7, 6], 23),
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ([4, 2, 0, 3, 2, 5], 9),
    ([100, 99], 0),

]


@pytest.mark.parametrize("input, expectation", test_cases)
def test_solution(input, expectation):
    assert Solution().trap(input) == expectation
