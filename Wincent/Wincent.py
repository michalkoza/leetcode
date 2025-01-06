import bisect
from collections import defaultdict
from typing import Tuple, Optional


class Solver:
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]


    def __init__(self):
        self.verticals = defaultdict(list)
        self.horizontals = defaultdict(list)
        self.slashes = defaultdict(list)
        self.backslashes = defaultdict(list)

    @classmethod
    def get_next_player(cls, current_player, players_on_direction, step):
        current_idx = bisect.bisect_left(players_on_direction, current_player)
        if 0 <= current_idx + step < len(players_on_direction):
            return players_on_direction[current_idx + step]
        else:
            return None

    def check_direction(self, direction, x, y) -> Optional[Tuple[int, int]]:
        if direction == "N":
            new_y = self.get_next_player(y, self.verticals[x], 0) # step is 0 because current player is already gone and bisect will return index of the next
            if new_y is not None:
                return x, new_y
        elif direction == "NE":
            new_x = self.get_next_player(x, self.slashes[y - x], 0)
            if new_x is not None:
                return new_x, new_x + (y - x)
        elif direction == "E":
            new_x = self.get_next_player(x, self.horizontals[y], 0)
            if new_x is not None:
                return new_x, y
        elif direction == "SE":
            new_x = self.get_next_player(x, self.backslashes[x + y], 0)
            if new_x is not None:
                return new_x, (x + y) - new_x
        elif direction == "S":
            new_y = self.get_next_player(y, self.verticals[x], -1)
            if new_y is not None:
                return x, new_y
        elif direction == "SW":
            new_x = self.get_next_player(x, self.slashes[y - x], -1)
            if new_x is not None:
                return new_x, new_x + (y - x)
        elif direction == "W":
            new_x = self.get_next_player(x, self.horizontals[y], -1)
            if new_x is not None:
                return new_x, y
        elif direction == "NW":
            new_x = self.get_next_player(x, self.backslashes[x + y], -1)
            if new_x is not None:
                return new_x, (x + y) - new_x
        return None

    def look_around(self, x, y, receive_direction) -> Optional[Tuple[int, int, str]]:
        for throw_direction in [self.directions[(self.directions.index(receive_direction) + 1 + i) % 8] for i in range(8)]:
            if (find := self.check_direction(throw_direction, x, y)) is not None:
                new_x, new_y = find
                new_receive_direction = self.directions[(self.directions.index(throw_direction) + 4) % 8]
                return new_x, new_y, new_receive_direction
        return None

    def remove_player(self, x, y):
        index = bisect.bisect_left(self.horizontals[y], x)
        self.horizontals[y].pop(index)
        index = bisect.bisect_left(self.verticals[x], y)
        self.verticals[x].pop(index)
        index = bisect.bisect_left(self.slashes[y - x], x)
        self.slashes[y - x].pop(index)
        index = bisect.bisect_left(self.backslashes[x + y], x)
        self.backslashes[x + y].pop(index)

    def solve_test_case(self, N, player_coordinates, initial_direction, starting_player_number) -> list[int]:
        for x, y in player_coordinates:
            bisect.insort(self.horizontals[y], x)
            bisect.insort(self.verticals[x], y)
            bisect.insort(self.slashes[y - x], x)
            bisect.insort(self.backslashes[x + y], x)

        x, y = player_coordinates[starting_player_number - 1]
        self.remove_player(x, y)

        remaining_players = N - 1
        throws = 0
        direction = initial_direction

        while remaining_players > 0:
            if (find := self.look_around(x, y, direction)) is None:  # noone to throw to
                break
            else:
                x, y, direction = find
                throws += 1
                remaining_players -= 1
                self.remove_player(x, y)

        last_player_number = player_coordinates.index([x, y]) + 1
        return [throws, last_player_number]


def main():
    with open("example.in", "r", encoding="utf-8") as in_file:
        test_cases = int(in_file.readline().strip())
        with open("example.out", "w+", encoding="utf-8") as out_file:
            for _ in range(test_cases):
                N = int(in_file.readline())
                player_coordinates = []
                for _ in range(N):
                    player_coordinates.append(list(map(int, in_file.readline().strip().split(" "))))
                initial_direction = in_file.readline().strip()
                starting_player_idx = int(in_file.readline())

                result = Solver().solve_test_case(N, player_coordinates, initial_direction, starting_player_idx)

                out_file.write(f"{" ".join(map(str, result))}\n")


if __name__ == "__main__":
    main()
