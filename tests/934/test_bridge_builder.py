import pytest

from _934_ShortestBridge.BridgeBuilder import Solution

test_cases = [
    ([[0, 1], [1, 0]], 1),
    ([[0, 1, 0], [0, 0, 0], [0, 0, 1]], 2),
    ([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]], 1),
    ([[0, 1, 0, 0, 0], [0, 1, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 1)
]


@pytest.mark.parametrize("grid, expectation", test_cases)
def test_find_judges(grid, expectation):
    assert Solution().shortestBridge(grid) == expectation
