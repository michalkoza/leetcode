class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        if not s:
            if not p:
                return True
            else:
                for i in range(len(p)):
                    if p[i] != "*":
                        return False
                return True

        if not p:
            return not s

        def match_here(start, pattern):
            if start + len(pattern) > n or start < 0:
                return False
            for i in range(len(pattern)):
                if s[start + i] != pattern[i] and pattern[i] != "?":
                    return False
            return True

        starts_with_star = p[0] == "*"
        ends_with_star = p[-1] == "*"
        chunks = []

        j = 0
        pattern = []
        while j < len(p):
            if p[j] == "*":
                if pattern:
                    chunks.append(pattern)
                    pattern = []
            else:
                pattern.append(p[j])
            j += 1
        if pattern:
            chunks.append(pattern)

        i = 0
        if not ends_with_star:
            if not match_here(n - len(chunks[-1]), chunks[-1]):
                return False

        if not starts_with_star:
            if not match_here(0, chunks[0]):
                return False

        if not ends_with_star and not starts_with_star and len(chunks) < 2:
            return len(p) == len(s)

        if not chunks:
            return True

        j = 0
        while i < n:
            if s[i] == chunks[0][j] or chunks[0][j] == "?":
                j += 1
                i += 1
                if j == len(chunks[0]):
                    chunks = chunks[1:]
                    j = 0
                    if not chunks:
                        return True
            else:
                i = i + 1 - j
                j = 0

        return False
