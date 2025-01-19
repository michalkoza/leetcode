from typing import List


class Solution:

    @classmethod
    def iter_box(cls, row, col, i):
        return 3 * (row // 3) + i // 3, 3 * (col // 3) + i % 3

    def solveSudoku(self, board: List[List[str]]) -> None:
        n = 9

        def is_valid(row, col, ch) -> bool:
            for i in range(n):
                if board[row][i] == ch:
                    return False
                if board[i][col] == ch:
                    return False
                box_x, box_y = self.iter_box(row, col, i)
                if board[box_x][box_y] == ch:
                    return False
            return True

        def solve(row, col):
            if row == n:
                return True
            if col == n:
                return solve(row + 1, 0)

            if board[row][col] == ".":
                for i in range(1, 10):
                    if is_valid(row, col, str(i)):
                        board[row][col] = str(i)
                        if solve(row, col + 1):
                            return True
                        else:
                            board[row][col] = "."
                return False
            else:
                return solve(row, col + 1)

        solve(0, 0)
