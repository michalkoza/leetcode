import pytest

from _850_rectangleArea2.AreaFinder import Solution

test_cases = [
    ([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]], 6),
    ([[0, 0, 1000000000, 1000000000]], 49),
]


@pytest.mark.parametrize("rectangles, expectation", test_cases)
def test_solution(rectangles, expectation):
    assert Solution().rectangleArea(rectangles) == expectation
