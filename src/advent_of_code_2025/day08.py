"""Day 8:

https://adventofcode.com/2025/day/8
"""

from collections import defaultdict, deque
from math import prod

Coord3d = tuple[int, int, int]


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


def find_connected_components(graph: dict[Coord3d, set[Coord3d]]) -> list[set[Coord3d]]:
    """
    Find all connected components in a graph using depth-first search.

    Args:
        graph: Adjacency list representation of the graph

    Returns:
        List of sets, where each set contains nodes in a connected component
    """
    visited: set[Coord3d] = set()
    components: list[set[Coord3d]] = []

    for node in graph:
        if node in visited:
            continue

        component: set[Coord3d] = set()
        stack = deque([node])

        while stack:
            current = stack.pop()

            if current in visited:
                continue

            visited.add(current)
            component.add(current)

            stack.extend(neighbor for neighbor in graph[current] if neighbor not in visited)

        components.append(component)

    return components


def part1(input_data: str, num_connections: int) -> int:
    """Solve part 1 of day 8."""
    points = parse_input(input_data)

    edges: list[tuple[float, Coord3d, Coord3d]] = [
        (euclidean_distance(points[i], points[j]), points[i], points[j])
        for i in range(len(points))
        for j in range(i + 1, len(points))
    ]

    edges.sort()

    graph: dict[Coord3d, set[Coord3d]] = defaultdict(set)

    for _, point_a, point_b in edges[:num_connections]:
        graph[point_a].add(point_b)
        graph[point_b].add(point_a)

    components = find_connected_components(graph)
    component_sizes = sorted((len(comp) for comp in components), reverse=True)

    return prod(component_sizes[:3])


def part2(input_data: str) -> int:
    """Solve part 2 of day 8."""
    _data = parse_input(input_data)
    # TODO: Implement solution
    return 0
