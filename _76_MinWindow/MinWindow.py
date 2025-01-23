from collections import deque


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hits = [0]*128
        chars = set()
        looking_for = 0
        positions = deque()
        n=len(s)

        best_l = -1
        best_r = n

        for ch in t:
            hits[ord(ch)] -= 1
            looking_for += 1
            chars.add(ch)

        l = r = 0
        while r < n or looking_for == 0:
            if looking_for == 0:
                l = positions.popleft()
                if best_r - best_l > r - l:
                    best_l, best_r = l, r
                ch = s[l]
                hits[ord(ch)] -= 1
                if hits[ord(ch)] < 0:
                    looking_for += 1
            else:
                ch = s[r]
                if ch in chars:
                    hits[ord(ch)] += 1
                    positions.append(r)
                    if hits[ord(ch)] <= 0:
                        looking_for -= 1
                r += 1

        if best_l >= 0:
            return s[best_l: best_r]
        else:
            return ""
