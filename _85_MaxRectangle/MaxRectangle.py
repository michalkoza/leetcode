from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        biggest_so_far = 0
        height = len(matrix)
        width = len(matrix[0])
        m = [[0] * width for _ in range(height)]

        def largestRectangleArea(heights: List[int]) -> None:
            n = len(heights)
            nonlocal biggest_so_far
            increasing_height_indexes = []
            for idx in range(len(heights)):
                while increasing_height_indexes and heights[increasing_height_indexes[-1]] > heights[idx]:
                    height = heights[increasing_height_indexes.pop()]
                    previous = increasing_height_indexes[-1] if increasing_height_indexes else -1
                    width = idx - previous - 1
                    biggest_so_far = max(biggest_so_far, height * width)
                if increasing_height_indexes and heights[idx] == heights[increasing_height_indexes[-1]]:
                    increasing_height_indexes.pop()
                increasing_height_indexes.append(idx)

            while increasing_height_indexes:
                height = heights[increasing_height_indexes.pop()]
                previous = increasing_height_indexes[-1] if increasing_height_indexes else -1
                width = n - previous - 1
                biggest_so_far = max(biggest_so_far, height * width)

        for x in range(width):
            cum = 0
            for y in range(height - 1, -1, -1):
                if matrix[y][x] == "1":
                    cum += 1
                else:
                    cum = 0
                m[y][x] = cum

        for y in range(height):
            largestRectangleArea(m[y])

        return biggest_so_far

