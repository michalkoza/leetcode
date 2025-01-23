from collections import defaultdict
from typing import List, Set


class Node:

    def __init__(self):
        self.children: Set['Node'] = set()
        self.distances = 0
        self.descendants = 0
        self.value = None

    def update_distances(self, distances, descendants):
        total_nodes = descendants
        parent_nodes = total_nodes - self.descendants
        parent_distances = distances - (self.distances + self.descendants)
        self.distances += parent_distances + parent_nodes
        for child in self.children:
            child.update_distances(self.distances, total_nodes)

    def collect_distances(self, parent: 'Node' = None):
        if parent is not None:
            self.children.remove(parent)
        if self.children:
            self.distances, self.descendants = map(sum, zip(*[child.collect_distances(self) for child in self.children]))
            self.distances += self.descendants
        self.descendants += 1

        return self.distances, self.descendants


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes = defaultdict(Node)
        for a, b in edges:
            nodes[a].value = a
            nodes[b].value = b
            nodes[a].children.add(nodes[b])
            nodes[b].children.add(nodes[a])
        distances, total_nodes = nodes[0].collect_distances()
        for child in nodes[0].children:
            child.update_distances(distances, total_nodes)

        return [nodes[i].distances for i in range(n)]

