"""Day 8:

https://adventofcode.com/2025/day/8
"""

from collections import defaultdict
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

        # DFS to explore the entire component
        component: set[Coord3d] = set()
        stack: list[Coord3d] = [node]

        while stack:
            current = stack.pop()

            if current in visited:
                continue

            visited.add(current)
            component.add(current)

            # Add all unvisited neighbors
            stack.extend(neighbor for neighbor in graph[current] if neighbor not in visited)

        components.append(component)

    return components


def group_coodinates(connected_coords: dict[Coord3d, set[Coord3d]]) -> list[set[Coord3d]]:
    """Group coordinates into connected components."""
    visited: set[Coord3d] = set()
    groups: list[set[Coord3d]] = []

    for coord in connected_coords.copy():
        if coord in visited:
            continue

        group: set[Coord3d] = set()
        stack: list[Coord3d] = [coord]

        while stack:
            current = stack.pop()
            if current in visited:
                continue

            visited.add(current)
            group.add(current)

            stack.extend(connected_coords[current])
        groups.append(group)

    return groups


def part1(input_data: str, num_connections: int) -> int:
    """Solve part 1 of day 8."""
    distances: list[tuple[float, Coord3d, Coord3d]] = []
    data = parse_input(input_data)
    n_numbers = len(data)

    for i in range(n_numbers):
        for j in range(i + 1, n_numbers):
            dist = euclidean_distance(data[i], data[j])
            distances.append((dist, data[i], data[j]))

    sorted_distances = sorted(distances)

    closest_points: dict[Coord3d, set[Coord3d]] = defaultdict(set)
    for total_connections, (_, point_a, point_b) in enumerate(sorted_distances):
        closest_points[point_b].add(point_a)
        closest_points[point_a].add(point_b)
        if total_connections == num_connections - 1:
            break

    groups = group_coodinates(closest_points)
    return prod(sorted(set(map(len, groups)))[-3:])


def part2(input_data: str) -> int:
    """Solve part 2 of day 8."""
    _data = parse_input(input_data)
    # TODO: Implement solution
    return 0
