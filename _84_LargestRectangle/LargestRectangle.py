import bisect
from collections import defaultdict
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        rectangles_tracker = defaultdict(int)
        relevant_heights = []
        biggest_so_far = 0
        for idx in range(len(heights)):
            height = heights[idx]
            i = bisect.bisect_left(relevant_heights, height)
            if i >= len(relevant_heights) or relevant_heights[i] != height:
                bisect.insort(relevant_heights, height)
            rectangles_tracker[relevant_heights[i]] += 1
            for j in range(len(relevant_heights) - 1, i, -1):
                collected = rectangles_tracker[relevant_heights[j]]
                biggest_so_far = max(biggest_so_far, collected * relevant_heights[j])
                rectangles_tracker[relevant_heights[j]] = 0
                rectangles_tracker[relevant_heights[j - 1]] += collected
            relevant_heights = relevant_heights[:i + 1]

        for j in range(len(relevant_heights) - 1, -1, -1):
            collected = rectangles_tracker[relevant_heights[j]]
            biggest_so_far = max(biggest_so_far, collected * relevant_heights[j])
            if j > 0:
                rectangles_tracker[relevant_heights[j - 1]] += collected

        return biggest_so_far
