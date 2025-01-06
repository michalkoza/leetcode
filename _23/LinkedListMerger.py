# Definition for singly-linked list.
import bisect
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, input_lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists: List[ListNode] = []
        for head in input_lists:
            if head is not None:
                bisect.insort(lists, head, key=lambda node: -node.val)
        dummy_root = ListNode(42, None)
        result = dummy_root
        last = dummy_root
        while len(lists) > 0:
            smallest = lists.pop()
            if smallest.next is not None:
                bisect.insort(lists, smallest.next, key=lambda node: -node.val)

            last.next = smallest
            last = smallest

        return result.next
