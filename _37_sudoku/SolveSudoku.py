from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = 9
        used_in_rows = [set() for _ in range(n)]
        used_in_cols = [set() for _ in range(n)]
        used_in_boxes = [[set() for _ in range(n // 3)] for _ in range(n // 3)]
        unsolved = set()

        def get_possibilities(row, col):
            invalid = used_in_rows[row] | used_in_cols[col] | used_in_boxes[row // 3][col // 3]
            valid = {x for x in range(1, n + 1) if x not in invalid}
            return valid

        for row in range(n):
            for col in range(n):
                if (ch := board[row][col]) == ".":
                    unsolved.add((row, col))
                else:
                    used_in_rows[row].add(int(ch))
                    used_in_cols[col].add(int(ch))
                    used_in_boxes[row // 3][col // 3].add(int(ch))

        def solve():
            if len(unsolved) == 0:
                return True
            else:
                cell = min(unsolved, key=lambda cell: len(get_possibilities(cell[0], cell[1])))
                row, col = cell
                for value in get_possibilities(row, col):
                    used_in_rows[row].add(value)
                    used_in_cols[col].add(value)
                    used_in_boxes[row // 3][col // 3].add(value)
                    unsolved.remove(cell)
                    if solve():
                        board[row][col] = str(value)
                        return True
                    else:
                        used_in_rows[row].remove(value)
                        used_in_cols[col].remove(value)
                        used_in_boxes[row // 3][col // 3].remove(value)
                        unsolved.add(cell)
                return False

        solve()
