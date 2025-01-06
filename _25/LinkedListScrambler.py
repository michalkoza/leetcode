from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1:
            return head

        def find_reversion_end(head: ListNode):
            potential_end = head
            for _ in range(k):
                potential_end = potential_end.next
                if potential_end is None:
                    return None
            return potential_end

        root = ListNode(-1, head)
        last_reversed = root

        while (end := find_reversion_end(last_reversed)) is not None:
            new_last_reversed = last_reversed.next
            for _ in range(k - 1):
                current = last_reversed.next
                last_reversed.next = current.next
                current.next = end.next
                end.next = current
            last_reversed = new_last_reversed

        return root.next
