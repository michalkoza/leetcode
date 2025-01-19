from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for current in range(n):
            to_insert = nums[current]
            if to_insert != current + 1:
                nums[current] = -1
                while 0 < to_insert <= n and to_insert != nums[to_insert - 1]:
                    new_to_replace = nums[to_insert - 1]
                    nums[to_insert - 1] = to_insert
                    to_insert = new_to_replace

        for current in range(n):
            if nums[current] < 1:
                return current + 1
        return n + 1
