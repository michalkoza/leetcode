import pytest

from _25.LinkedListScrambler import Solution
from _25.LinkedListScrambler import ListNode

test_cases = [
    ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),

    ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),

    ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5]),
    ([1], 2, [1]),

    ([1, 2, 3, 4, 5, 6], 3, [3, 2, 1, 6, 5, 4]),
]


def build_list(elements):
    previous = None
    for e in elements[::-1]:
        new = ListNode(e, previous)
        previous = new
    return previous


def list_list(linked_list: ListNode):
    result = []
    while linked_list is not None:
        result.append(linked_list.val)
        linked_list = linked_list.next
    return result


@pytest.mark.parametrize("input,k, expectation", test_cases)
def test_solution(input, k, expectation):
    linked_list = build_list(input)
    result = Solution().reverseKGroup(linked_list, k)
    assert list_list(result) == expectation
