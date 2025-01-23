from collections import deque, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hits = defaultdict(int)
        looking_for = set()
        positions = deque()

        best_l = -1
        best_r = len(s)

        for ch in t:
            hits[ch] -= 1
            looking_for.add(ch)

        l = -1
        r = 0
        while r < len(s) or looking_for == set():
            if looking_for == set():
                if l < 0:
                    l = positions.popleft()
                if best_r - best_l > r - l:
                    best_l, best_r = l, r
                ch = s[l]
                hits[ch] -= 1
                if hits[ch] < 0:
                    looking_for.add(ch)
                if len(positions) > 0:
                    l = positions.popleft()
            else:
                ch = s[r]
                if ch in hits.keys():
                    hits[ch] += 1
                    positions.append(r)
                    if hits[ch] >= 0:
                        looking_for.discard(ch)
                r += 1

        if best_l >= 0:
            return s[best_l: best_r]
        else:
            return ""
