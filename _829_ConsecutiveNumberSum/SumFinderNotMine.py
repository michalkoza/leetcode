import math

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 1

        # Continue while k * (k - 1) / 2 < n
        for k in range(2, round(math.sqrt(2 * n)) + 1):
            # Calculate the remaining part after subtracting the sum of first (k-1) numbers
            remaining = n - k * (k - 1) / 2

            # Check if remaining is divisible by k
            if remaining % k == 0:
                count += 1

        return count
