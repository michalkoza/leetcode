class Solution:
    def shortestBridge(self, A):

        def on_grid(i, j) -> bool:
            return 0 <= i < n and 0 <= j < n

        def is_water(i, j) -> bool:
            return A[i][j] == 0

        def is_land(i, j) -> bool:
            return A[i][j] == 1

        def is_shore(i, j) -> bool:
            return any(
                [not on_grid(x, y) or is_water(x, y) for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))]
            )

        def is_island(i, j) -> bool:
            return on_grid(i, j) and is_land(i, j)

        def dfs(i, j):
            A[i][j] = -1
            first_island.append((i, j))
            if is_shore(i, j):
                first_shore.append((i, j))
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if is_island(x, y):
                    dfs(x, y)

        def dfs2(i, j):
            A[i][j] = -1
            if is_shore(i, j):
                second_shore.append((i, j))
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if is_island(x, y):
                    dfs2(x, y)

        def first():
            for i in range(n):
                for j in range(n):
                    if is_land(i, j):
                        return i, j

        n, step, first_island, first_shore, second_shore = len(A), 0, [], [], []
        dfs(*first())

        def second():
            for i in range(n):
                for j in range(n):
                    if is_land(i, j) and (i, j) not in first_island:
                        return i, j

        dfs2(*second())

        shortest = n

        for x1, y1 in first_shore:
            for x2, y2 in second_shore:
                shortest = min(shortest, abs(x2 - x1) + abs(y2 - y1) - 1)

        return shortest
