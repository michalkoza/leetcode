class Solution:
    jumps = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [1, 7, 0],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4]
    }

    def knightDialer(self, n: int) -> int:
        current = [1] * 10
        for jump in range(1, n):
            current = list(
                map(lambda i: sum(list(map(lambda x: current[x], self.jumps[i]))) % (10 ** 9 + 7), range(10)))
        return sum(current) % (10 ** 9 + 7)
