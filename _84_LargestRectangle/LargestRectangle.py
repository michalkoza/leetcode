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
            if i >= len(relevant_heights):
                bisect.insort(relevant_heights, height)
            elif relevant_heights[i] != height:
                rectangles_tracker[height] = rectangles_tracker[relevant_heights[i]]
                bisect.insort(relevant_heights, height)
            for h in relevant_heights[:i + 1]:
                    rectangles_tracker[h] += 1
                    biggest_so_far = max(biggest_so_far, h * rectangles_tracker[h])
            for h in relevant_heights[i + 1:]:
                rectangles_tracker[h] = 0
            relevant_heights = relevant_heights[:i + 1]
            relevant_heights = [h for h in relevant_heights if (rectangles_tracker[h] + n - idx) * h > biggest_so_far]

        return biggest_so_far
