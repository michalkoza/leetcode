class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        monster_index = -1
        first_not_swallowed_index = -1
        n = len(s)
        k = len(p)
        i = 0
        j = 0

        while i < n:
            if p[j] == "*":
                monster_index = j
                first_not_swallowed_index = i
                j += 1
                if j >= k:
                    return True
            elif (p[j] == "?" or p[j] == s[i]) and not (j == k - 1 and i < n - 1):
                i += 1
                j += 1
            elif monster_index >= 0:
                j = monster_index + 1
                first_not_swallowed_index += 1
                i = first_not_swallowed_index
            else:
                return False
        while j < k:
            if p[j] != "*":
                return False
            j += 1
        return True
