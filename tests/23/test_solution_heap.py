import pytest

from _23.LinkedListMergerHeap import ListNode
from _23.LinkedListMergerHeap import Solution

test_cases = [
    ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
    ([], []),
    ([[]], []),
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


@pytest.mark.parametrize("input, expectation", test_cases)
def test_solution(input, expectation):
    lists = [build_list(elements) for elements in input]
    result = Solution().mergeKLists(lists)
    assert list_list(result) == expectation
