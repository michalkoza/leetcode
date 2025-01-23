from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustCounters = defaultdict(int)
        for trusting, trusted in trust:
            trustCounters[trusted] += 1
            trustCounters[trusting] -= 1
        for i in range(1, n + 1):
            if trustCounters[i] == n - 1:
                return i
        return -1
