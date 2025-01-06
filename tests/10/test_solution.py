import random

import pytest

from _10_failed.RegexMatcher import Solution

test_cases = [

    ([0, 1, 2], [0, 1, 2, 3, 4, 5], 2),
    ([0, 1, 2, 3], [0, 1, 2, 3, 4], 2),
    ([0, 1, 2], [0, 1, 2, 3, 4], 1.5),
    ([0, 1, 2, 3], [0, 1, 2, 3, 4, 5], 2),

    ([-93, -83, -52, -35, -19, -19, 8, 11, 21, 32, 58, 65, 72, 100],
     [-98, -97, -91, -81, -74, -67, -61, -48, -24, -7, 2, 4, 9, 19, 33, 44, 90, 93, 93], 2),

    ([], [1, 2, 3], 2),
    ([], [1, 2, 3, 4], 2.5),
    ([], [10], 10),

    ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3], 3.5),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2], 4),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3], 4),
    ([1, 2, 3, 10], [9, 21, 22, 23], 9.5),
    ([1, 2, 3, 10], [10, 21, 22, 23], 10),
    ([1, 2, 3, 10], [11, 21, 22, 23], 10.5),
    ([1, 2, 3, 10], [9, 21, 22], 9),
    ([1, 2, 3, 10], [10, 21, 22], 10),
    ([1, 2, 3, 10], [11, 21, 22], 10),
    ([1, 3], [2], 2),
    ([1, 2], [3, 4], 2.5),
    ([1, 2, 3], [4, 5], 3),
    ([1, 2, 3], [3, 4], 3),
    ([1, 2], [3, 4, 5], 3),
    ([1, 3], [3, 4, 5], 3),
    ([1, 2, 3], [5, 6, 7], 4),
    ([1, 2, 3, 4], [1, 2, 3, 4], 2.5),
    ([1, 2, 3, 4], [2, 3, 4], 3),
    ([2, 3, 4], [1, 2, 3, 4], 3),
    ([2, 3, 4], [2, 3, 4], 3),

    ([1, 2, 3, 4, 5, 6, 7, 8, 9], [8, 9], 6),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2], 4.5),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [8, 9], 6.5),
    ([-73, -38, -34, -18, -11, -3, -1, 3, 6, 12, 14, 18, 26, 48, 62, 62, 69, 77, 84, 88],
     [-99, -96, -77, -46, -19, -16, -14, -7, 36, 49, 49, 51, 70, 79, 84], 12),
]


def merge_tables(nums1, nums2):
    return sorted(nums1 + nums2)


@pytest.mark.parametrize("array1, array2, expectation", test_cases)
def test_solution(array1, array2, expectation):
    assert Solution().findMedianSortedArrays(array1, array2) == expectation


def generate_sorted_random_list():
    # Generate a random size for the list between 1 and 20
    size = random.randint(1, 20)

    # Generate `size` random values (e.g., between 0 and 100)
    random_values = [random.randint(-100, 100) for _ in range(size)]

    # Sort the list in ascending order
    sorted_values = sorted(random_values)

    return sorted_values


def generate():
    ret = []
    for _ in range(100):
        arr1 = generate_sorted_random_list()
        arr2 = generate_sorted_random_list()
        merged = merge_tables(arr1, arr2)
        n = len(merged)
        madian = merged[n // 2] if len(merged) % 2 == 1 else (merged[n // 2 - 1] + merged[n // 2]) / 2
        ret.append((arr1, arr2, madian))
    return ret


generated = generate()


@pytest.mark.parametrize("array1, array2, expectation", generated)
def test_generated(array1, array2, expectation):
    print(f"\narr1: {array1}, arr2: {array2}, expected median: {expectation} ({array1}, {array2}, {expectation})")
    median = Solution().findMedianSortedArrays(array1, array2)
    assert median == expectation, f"arr1: {array1}, arr2: {array2}, median: {median}, expected median: {expectation}"
