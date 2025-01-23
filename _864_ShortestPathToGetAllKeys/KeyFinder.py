from typing import List, Set, Optional, FrozenSet


class Tail:
    def __init__(self, char: str):
        self.is_wall = char == "#"
        self.key = char if char.islower() else None
        self.lock = char.lower() if char.isupper() else None
        self.is_start = char == "@"
        self.visited_with_keys: Set[FrozenSet[str]] = set()

    def not_wall(self) -> bool:
        return not self.is_wall

    def not_locked(self, key_set: FrozenSet[str]) -> bool:
        return self.lock is None or self.lock in key_set

    def not_visited(self, key_set: FrozenSet[str]) -> bool:
        return key_set not in self.visited_with_keys

    def try_visit(self, key_set: FrozenSet[str]) -> Optional[FrozenSet[str]]:
        if self.not_wall() and self.not_locked(key_set) and self.not_visited(key_set):
            self.visited_with_keys.add(key_set)
            if self.key is not None:
                key_set = key_set.union(frozenset(self.key))
            return key_set
        return None


class Solution:
    def shortestPathAllKeys(self, input: List[str]) -> int:
        self.grid: List[List[Tail]] = [[Tail(char) for char in line] for line in input]

        steps = 0
        height = len(self.grid)
        width = len(self.grid[0])
        desired_key_set = set()
        bsf = None

        def scout():
            nonlocal bsf
            for i in range(height):
                for j in range(width):
                    if self.grid[i][j].is_start:
                        bsf = [(i, j, frozenset())]
                    elif (key := self.grid[i][j].key) is not None:
                        desired_key_set.add(key)

        scout()

        while bsf:
            new = []
            steps += 1
            for i, j, key_set in bsf:
                for x, y in {(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)}:
                    if 0 <= x < height and 0 <= y < width:
                        new_key_set = self.grid[x][y].try_visit(key_set)
                        if new_key_set is not None:
                            if new_key_set == desired_key_set:
                                return steps
                            new.append((x, y, new_key_set))
            bsf = new
        return -1
