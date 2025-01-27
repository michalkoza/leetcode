from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        biggest_so_far = 0
        increasing_height_indexes = []
        for idx in range(len(heights)):
            while increasing_height_indexes and heights[increasing_height_indexes[-1]] > heights[idx]:
                height = heights[increasing_height_indexes.pop()]
                previous = increasing_height_indexes[-1] if increasing_height_indexes else -1
                width = idx - previous - 1
                biggest_so_far = max(biggest_so_far, height * width)
            increasing_height_indexes.append(idx)

        while increasing_height_indexes:
            height = heights[increasing_height_indexes.pop()]
            previous = increasing_height_indexes[-1] if increasing_height_indexes else -1
            width = n - previous - 1
            biggest_so_far = max(biggest_so_far, height * width)

        return biggest_so_far
