# Definition for singly-linked list.

import heapq
from typing import List, Optional


class MyHeapq:
    def __init__(self, initial=None, key=lambda x: x):
        self.key = key
        self.index = 0
        if initial:
            self._data = [(key(item), i, item) for i, item in enumerate(initial)]
            self.index = len(self._data)
            heapq.heapify(self._data)
        else:
            self._data = []

    def push(self, item):
        heapq.heappush(self._data, (self.key(item), self.index, item))
        self.index += 1

    def pop(self):
        if len(self._data) == 0:
            return None
        val = heapq.heappop(self._data)
        return val[2]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, input_lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = MyHeapq(key=lambda node: node.val)
        for head in input_lists:
            if head is not None:
                lists.push(head)
        dummy_root = ListNode(42, None)
        result = dummy_root
        last = dummy_root
        while (smallest := lists.pop()) is not None:
            if smallest.next is not None:
                lists.push(smallest.next)
            last.next = smallest
            last = smallest

        return result.next
