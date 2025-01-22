class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        digits = [i + 1 for i in range(n)]
        factorials = [1] * n
        result = []

        for i in range(1, n):
            factorials[i] = factorials[i - 1] * i

        for digit_idx in range(n):
            digit = k // factorials[n - digit_idx - 1]
            k -= digit * factorials[n - digit_idx - 1]
            result.append(str(digits.pop(digit)))

        return "".join(result)
