from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        # board = [[False] * n] * n

        colum_attacks = [False] * n
        slash_diagonals_attacks = [False] * (2 * n - 1)
        backslash_diagonals_attacks = [False] * (2 * n - 1)
        rows = [-1] * n

        def generate_solution():
            return ["." * col + "Q" + "." * (n - col - 1) for col in rows]

        def update(col, row, attack: bool):
            colum_attacks[col] = attack
            slash_diagonals_attacks[row - col] = attack
            backslash_diagonals_attacks[row + col] = attack

        def is_free(col, row):
            return colum_attacks[col] == False and slash_diagonals_attacks[row - col] == False and \
                backslash_diagonals_attacks[row + col] == False

        def put(col, row):
            update(col, row, True)
            rows[row] = col

        def remove(col, row):
            update(col, row, False)

        def process_row(row):
            for col in range(n):
                if is_free(col, row):
                    put(col, row)
                    if row == n - 1:
                        results.append(generate_solution())
                    process_row(row + 1)
                    remove(col, row)

        process_row(0)

        return results
