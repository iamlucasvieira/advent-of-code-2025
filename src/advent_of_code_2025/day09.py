"""Day 9:

https://adventofcode.com/2025/day/9
"""

from collections import defaultdict
from itertools import combinations
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


def parse_input(input_data: str) -> list[Point]:
    """Parse the input data for day 9."""
    points = []
    for line in input_data.strip().splitlines():
        x_str, y_str = line.split(",")
        points.append(Point(int(x_str), int(y_str)))
    return points


def group_by_x(points: list[Point]) -> dict[int, list[int]]:
    """Group points by their x-coordinate."""
    grouped = defaultdict(list)
    for point in points:
        grouped[point.x].append(point.y)
    return grouped


def get_area(p1: Point, p2: Point) -> int:
    return (abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1)


def find_max_area(grouped_points: dict[int, list[int]]) -> int:
    """Find the maximum area formed by points with the same x-coordinate."""

    max_area = 0

    for p1_x, p2_x in combinations(grouped_points.keys(), 2):
        p1_y_values = grouped_points[p1_x]
        p2_y_values = grouped_points[p2_x]

        p1_max_y, p1_min_y = max(p1_y_values), min(p1_y_values)
        p2_max_y, p2_min_y = max(p2_y_values), min(p2_y_values)

        if abs(p1_max_y - p2_min_y) > abs(p1_min_y - p2_max_y):
            p1_y, p2_y = p1_max_y, p2_min_y
        else:
            p1_y, p2_y = p1_min_y, p2_max_y

        if (area := get_area(Point(p1_x, p1_y), Point(p2_x, p2_y))) > max_area:
            max_area = area
    return max_area


def part1(input_data: str) -> int:
    """Solve part 1 of day 9."""
    points = parse_input(input_data)
    grouped_points = group_by_x(points)
    return find_max_area(grouped_points)


def part2(input_data: str) -> int:
    """Solve part 2 of day 9."""
    _data = parse_input(input_data)
    # TODO: Implement solution
    return 0
