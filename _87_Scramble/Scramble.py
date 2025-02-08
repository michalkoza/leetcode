from collections import defaultdict


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        cache = dict()
        def inner(real, scramble):
            if real == scramble:
                return True
            if (cache_check := cache.get((real, scramble))) is not None:
                return cache_check
            l = len(real)
            if l == 1:
                return False
            if l == 2:
                return real == scramble[::-1]
            prefix_collector = defaultdict(int)
            suffix_collector = defaultdict(int)
            real_collector = defaultdict(int)
            for i in range(l - 1):
                is_success = False
                real_collector[real[i]] += 1
                prefix_collector[scramble[i]] += 1
                suffix_collector[scramble[-(i + 1)]] += 1
                if real_collector == prefix_collector:
                    if inner(real[:i + 1], scramble[:i + 1]) and inner(real[i + 1:], scramble[i + 1:]):
                        is_success = True
                if real_collector == suffix_collector:
                    if inner(real[:i + 1], scramble[-(i + 1):]) and inner(real[i + 1:], scramble[:-(i + 1)]):
                        is_success = True
                if is_success:
                    cache[(real, scramble)] = is_success
                    return True
                else:
                    cache[(real, scramble)] = is_success
            return False

        return sorted(s1) == sorted(s2) and inner(s1, s2)
