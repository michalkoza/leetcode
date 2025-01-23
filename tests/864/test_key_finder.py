import pytest

from _864_ShortestPathToGetAllKeys.KeyFinder import Solution

test_cases = [
    (["@.a..", "###.#", "b.A.B"], 8),
    (["@..aA", "..B#.", "....b"], 6),
    (["@Aa"], -1),
]


@pytest.mark.parametrize("grid, expectation", test_cases)
def test_find_judges(grid, expectation):
    assert Solution().shortestPathAllKeys(grid) == expectation
