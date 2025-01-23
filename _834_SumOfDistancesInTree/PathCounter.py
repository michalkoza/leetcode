from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        edge_table = [[None] * i + [0] for i in range(n)]

        def set_distance(a, b, value):
            if get_distance(a, b) is None:
                edge_table[max(a, b)][min(a, b)] = value

        def get_distance(a, b):
            return edge_table[max(a, b)][min(a, b)]

        def get_distances(i):
            return [get_distance(i, j) for j in range(i + 1, n)] + edge_table[i]

        def add_edge(a, b, value=1):
            nonlocal edge_table
            smaller = min(a, b)
            bigger = max(a, b)
            set_distance(a, b, value)
            for linked_to_bigger in range(n):
                if (distance2 := get_distance(linked_to_bigger, bigger)) is not None:
                    for linked_to_smaller in range(n):
                        if linked_to_bigger != linked_to_smaller:
                            if (distance1 := get_distance(linked_to_smaller, smaller)) is not None:
                                set_distance(linked_to_smaller, linked_to_bigger, 1 + distance1 + distance2)

        for a, b in edges:
            add_edge(a, b)

        return [sum(get_distances(i)) for i in range(n)]
