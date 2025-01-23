import math


class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        possibilities = 1

        for i in range(2, round(math.sqrt(2 * n)) + 1):
            x = (2 * n + i - i ** 2) / (2 * i)
            if x > 0 and x.is_integer():
                possibilities += 1
                print(" + ".join([f"{i}" for i in range(round(x), round(x + i))]))

        return possibilities
