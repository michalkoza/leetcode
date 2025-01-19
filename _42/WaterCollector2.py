from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        water = 0

        highest_left = height[left]
        highest_right = height[right]

        while left < right:
            if highest_left < highest_right:
                left += 1
                highest_left = max(highest_left, height[left])
                water += max(0, min(highest_left, highest_right) - height[left])
            else:
                right -= 1
                highest_right = max(highest_right, height[right])
                water += max(0, min(highest_left, highest_right) - height[right])

        return water
