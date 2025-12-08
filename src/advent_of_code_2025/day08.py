"""Day 8:

https://adventofcode.com/2025/day/8
"""

from collections import defaultdict
from collections.abc import Hashable
from math import prod
from typing import Generic, TypeVar

Coord3d = tuple[int, int, int]
T = TypeVar("T", bound=Hashable)


class UnionFind(Generic[T]):
    def __init__(self, items: list[T]) -> None:
        """Initialize the Union-Find data structure."""
        self.parent: dict[T, T] = {item: item for item in items}
        self.rank: dict[T, int] = dict.fromkeys(items, 0)

    def find(self, item: T) -> T:
        """Find the root of the set containing the item."""
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, item_1: T, item_2: T) -> bool:
        """Union the sets containing item_1 and item_2."""
        root_1 = self.find(item_1)
        root_2 = self.find(item_2)

        if root_1 == root_2:
            return False

        if self.rank[root_1] < self.rank[root_2]:
            self.parent[root_1] = root_2
        elif self.rank[root_1] > self.rank[root_2]:
            self.parent[root_2] = root_1
        else:
            self.parent[root_2] = root_1
            self.rank[root_1] += 1

        return True

    def get_component_sizes(self) -> list[int]:
        """Get the sizes of all connected components."""
        component_sizes: dict[T, int] = defaultdict(int)
        for item in self.parent:
            root = self.find(item)
            component_sizes[root] += 1
        return list(component_sizes.values())


def parse_input(input_data: str) -> list[Coord3d]:
    """Parse the input data for day 8."""
    data = []
    for line in input_data.strip().splitlines():
        x, y, z = map(int, line.split(","))
        data.append((x, y, z))
    return data


def euclidean_distance(a: tuple[int, ...], b: tuple[int, ...]) -> float:
    """Calculate the Euclidean distance between two points."""
    if len(a) != len(b):
        raise ValueError()
    return sum((x - y) ** 2 for x, y in zip(a, b, strict=True)) ** 0.5


def get_distances_sorted(points: list[Coord3d]) -> list[tuple[float, Coord3d, Coord3d]]:
    """Get all pairwise distances between points, sorted in ascending order."""
    edges: list[tuple[float, Coord3d, Coord3d]] = [
        (euclidean_distance(points[i], points[j]), points[i], points[j])
        for i in range(len(points))
        for j in range(i + 1, len(points))
    ]
    edges.sort()
    return edges


def part1(input_data: str, num_connections: int) -> int:
    """Solve part 1 of day 8."""
    points = parse_input(input_data)
    uf = UnionFind(points)
    edges = get_distances_sorted(points)

    for _, point_a, point_b in edges[:num_connections]:
        uf.union(point_a, point_b)

    component_sizes = sorted(uf.get_component_sizes(), reverse=True)
    return prod(component_sizes[:3])


def part2(input_data: str) -> int:
    """Solve part 2 of day 8."""
    points = parse_input(input_data)
    uf = UnionFind(points)
    edges = get_distances_sorted(points)

    n_points = len(points)
    for _, point_a, point_b in edges:
        if uf.union(point_a, point_b):
            n_points -= 1

        if n_points == 1:
            return point_a[0] * point_b[0]

    raise ValueError()
