from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def lengths_sum_even():
            return (n_1 + n_2) % 2 == 0

        inf = 10 ** 7
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n_1 = len(nums1)
        n_2 = len(nums2)

        first = 0
        outside = n_1

        while True:
            first_not_left_1 = (first + outside) // 2
            first_not_left_2 = (n_2 + n_1) // 2 - first_not_left_1

            max_left_1 = -inf if first_not_left_1 == 0 else nums1[first_not_left_1 - 1]
            potential_median_1 = inf if first_not_left_1 == n_1 else nums1[first_not_left_1]
            max_left_2 = -inf if first_not_left_2 == 0 else nums2[first_not_left_2 - 1]
            potential_median_2 = inf if first_not_left_2 == n_2 else nums2[first_not_left_2]

            if potential_median_1 < max_left_2:
                first = first_not_left_1 + 1
            elif potential_median_2 < max_left_1:
                outside = first_not_left_1 - 1
            else:
                if lengths_sum_even():
                    return (max(max_left_1, max_left_2) + min(potential_median_1, potential_median_2)) / 2
                else:
                    return min(potential_median_1, potential_median_2)
