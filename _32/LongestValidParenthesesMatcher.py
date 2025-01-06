class Solution:
    def longestValidParentheses(self, s: str) -> int:
        furthest_back_difference = [-1]
        longest = 0
        for i in range(len(s)):
            if s[i] == "(":
                furthest_back_difference.append(i)
            else:
                furthest_back_difference.pop()
                if len(furthest_back_difference) == 0:
                    furthest_back_difference.append(i)
                else:
                    longest = max(longest, i - furthest_back_difference[-1])
        return longest
