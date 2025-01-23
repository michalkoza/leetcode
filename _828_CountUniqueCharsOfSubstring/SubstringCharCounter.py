from collections import defaultdict


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        occurrences = defaultdict(lambda: (-1, -1))
        sum = 0
        for i, ch in enumerate(s):
            second_last, last = occurrences[ch]
            if last == -1:
                occurrences[ch] = (-1, i)
            else:
                sum += (last - second_last) * (i - last)
                occurrences[ch] = (last, i)
        for ch in occurrences:
            second_last, last = occurrences[ch]
            sum += (last - second_last) * (len(s) - last)
        return sum
