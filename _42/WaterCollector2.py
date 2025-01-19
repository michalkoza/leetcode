from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        possible_levels = [0] * n

        highest = 0
        for i in range(n):
            highest = max(highest, height[i])
            possible_levels[i] = highest

        highest = 0
        for i in range(n - 1, -1, -1):
            highest = max(highest, height[i])
            possible_levels[i] = min(possible_levels[i], highest) - height[i]

        return sum(possible_levels)
