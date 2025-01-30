import pytest

from _85_MaxRectangle.MaxRectangle import Solution

test_cases = [
    ([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]], 6),
    ([["1", "0", "1", "0", "0"],
      ["1", "0", "1", "0", "1"],
      ["1", "1", "1", "1", "1"],
      ["1", "0", "0", "1", "0"]], 5),
    ([["1"]], 1),
    ([["0"]], 0),
    ([["1", "1"],
      ["1", "1"]], 4),
    ([["0", "1"],
      ["1", "1"]], 2),
    ([["1", "0"],
      ["0", "0"]], 1),
    ([["0", "1", "1", "1", "1"],
      ["1", "1", "1", "1", "1"],
      ["1", "1", "1", "1", "1"],
      ["1", "1", "1", "1", "1"],
      ["1", "1", "1", "1", "0"]], 16),
    ([["0", "1", "1", "1", "0"],
      ["1", "1", "1", "1", "1"],
      ["1", "1", "1", "1", "1"],
      ["1", "1", "1", "1", "1"],
      ["0", "1", "1", "1", "0"]], 15),
    ([["0", "0", "0", "0", "1"],
      ["0", "0", "0", "1", "1"],
      ["0", "0", "1", "1", "1"],
      ["0", "1", "1", "1", "1"],
      ["1", "1", "1", "1", "1"]], 9),
    ([["1", "1", "1", "1", "1"],
      ["1", "0", "1", "1", "1"],
      ["1", "1", "0", "1", "1"],
      ["1", "1", "1", "1", "1"],
      ["1", "0", "1", "0", "1"],
      ["1", "1", "1", "1", "1"],
      ["1", "1", "1", "1", "1"],
      ["1", "1", "0", "1", "0"]], 10),
]


@pytest.mark.parametrize("matrix ,expectation", test_cases)
def test_solution(matrix, expectation):
    rotated = [[row[i] for row in matrix[::-1]] for i in range(len(matrix[0]))]
    mirror_y = [row[::-1] for row in matrix]
    mirror_x = matrix[::-1]
    mirror_xy = [row[::-1] for row in mirror_x]
    rotated_mirror_y = [row[::-1] for row in rotated]
    rotated_mirror_x = rotated[::-1]
    rotated_mirror_xy = [row[::-1] for row in rotated_mirror_x]
    assert Solution().maximalRectangle(matrix) == expectation, f"{matrix}"
    assert Solution().maximalRectangle(mirror_x) == expectation, f"{mirror_x}"
    assert Solution().maximalRectangle(mirror_y) == expectation, f"{mirror_y}"
    assert Solution().maximalRectangle(mirror_xy) == expectation, f"{mirror_xy}"
    assert Solution().maximalRectangle(rotated) == expectation, f"{rotated}"
    assert Solution().maximalRectangle(rotated_mirror_x) == expectation, f"{rotated_mirror_x}"
    assert Solution().maximalRectangle(rotated_mirror_y) == expectation, f"{rotated_mirror_y}"
    assert Solution().maximalRectangle(rotated_mirror_xy) == expectation, f"{rotated_mirror_xy}"
