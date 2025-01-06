class Solution:
    def isMatch(self, string: str, p: str) -> bool:
        matchers = []
        satisfied = []
        matches = []
        earliest_unsatisfied = -1

        def parseRegex():
            nonlocal earliest_unsatisfied
            i = len(string) - 1
            consumed_end = i + 1

            def dump():
                nonlocal earliest_unsatisfied
                if consumed_end>i:
                    matchers.append(string[i + 1:consumed_end])
                    satisfied.append(False)

            while i >= 0:
                if string[i] == "*":
                    dump()
                    matchers.append(string[i - 1:i + 1])
                    satisfied.append(True)
                    consumed_end = i - 1
                    i = - 2
                elif string[i] == ".":
                    dump()
                    matchers.append(string[i])
                    satisfied.append(False)
                    consumed_end = i
                    i -= 1
                else:
                    i -= 1
            if consumed_end > 1:
                matchers.append(string[0:consumed_end])

            earliest_unsatisfied = min([i for i in range(len(satisfied)) if satisfied[i] is False])
            nonlocal matches
            matches = [[] for _ in matchers]

        def attempt_consumption(s: str, matcher_idx: int):
            if matcher_idx > earliest_unsatisfied:
                attempt_consumption(s, matcher_idx-1)
            matcher = matchers[matcher_idx]
            if matcher[:-1] == "*":
                if matcher[0] == ".":
                    matches[matcher_idx].append(s)




        parseRegex()

        return False
