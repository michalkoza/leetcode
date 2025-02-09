from collections import defaultdict


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        positions = defaultdict(list)
        t_consume_iterator = 0
        len_t = len(t)

        prefix_counter = defaultdict(int)
        prefix_counter[""] = 1

        for ch in s:
            if t_consume_iterator < len_t and ch == t[t_consume_iterator]:
                positions[t[t_consume_iterator]].append(t_consume_iterator)
                t_consume_iterator += 1
            for position in positions[ch][::-1]:
                prefix_counter[t[:position + 1]] += prefix_counter[t[:position]]

        return prefix_counter[t]
