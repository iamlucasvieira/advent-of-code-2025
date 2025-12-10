"""Day 9:

https://adventofcode.com/2025/day/9
"""

from collections import defaultdict
from collections.abc import Iterator
from itertools import combinations_with_replacement
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


def in_squared_polygon(p: Point, polygon: list[Point]) -> bool:
    x, y = p.x, p.y
    crossings = 0
    edges = zip(polygon, [*polygon[1:], polygon[0]], strict=True)

    for p1, p2 in edges:
        max_x, min_x = max(p1.x, p2.x), min(p1.x, p2.x)
        max_y, min_y = max(p1.y, p2.y), min(p1.y, p2.y)
        if p1.x == p2.x:
            is_on_edge = (x == p1.x) and (min_y <= y <= max_y)
            if is_on_edge:
                return True
            if min_y < y < max_y and x < max_x:
                crossings += 1
        elif p1.y == p2.y:
            is_on_edge = (y == p1.y) and (min_x <= x <= max_x)
            if is_on_edge:
                return True
            continue
        else:
            raise ValueError()

    return crossings % 2 == 1


def get_areas(grouped_points: dict[int, list[int]]) -> Iterator[tuple[Point, Point, int]]:
    """Generate areas formed by points with the same x-coordinate."""
    for p1_x, p2_x in combinations_with_replacement(grouped_points.keys(), 2):
        p1_y_values = grouped_points[p1_x]
        p2_y_values = grouped_points[p2_x]

        p1_max_y, p1_min_y = max(p1_y_values), min(p1_y_values)
        p2_max_y, p2_min_y = max(p2_y_values), min(p2_y_values)

        if abs(p1_max_y - p2_min_y) > abs(p1_min_y - p2_max_y):
            p1_y, p2_y = p1_max_y, p2_min_y
        else:
            p1_y, p2_y = p1_min_y, p2_max_y

        p1, p2 = Point(p1_x, p1_y), Point(p2_x, p2_y)
        yield p1, p2, get_area(p1, p2)


def fill_polygon(polygon: list[Point]) -> set[Point]:  # noqa: C901
    """Precompute all points inside/on the polygon boundary."""
    if not polygon:
        return set()

    max_x = max(p.x for p in polygon)

    filled = set()
    for p1, p2 in zip(polygon, [*polygon[1:], polygon[0]], strict=True):
        if p1.x == p2.x:
            for y in range(min(p1.y, p2.y), max(p1.y, p2.y) + 1):
                filled.add(Point(p1.x, y))
        elif p1.y == p2.y:
            for x in range(min(p1.x, p2.x), max(p1.x, p2.x) + 1):
                filled.add(Point(x, p1.y))
        else:
            raise ValueError()

    for p in filled.copy():
        horizontal_line = set()
        found_wall = False
        for x in range(p.x + 1, max_x + 1):
            horizontal_line.add(Point(x, p.y))
            if Point(x, p.y) in filled:
                found_wall = True
                break

        if found_wall:
            filled.update(horizontal_line)

    return filled


def rectangle_fully_inside(p1: Point, p2: Point, filled_polygon: set[Point]) -> bool:
    """Check if entire rectangle is inside using precomputed set."""
    min_x, max_x = min(p1.x, p2.x), max(p1.x, p2.x)
    min_y, max_y = min(p1.y, p2.y), max(p1.y, p2.y)

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if Point(x, y) not in filled_polygon:
                return False
    return True


def get_all_rectangle_candidates(points: list[Point]) -> Iterator[tuple[Point, Point, int]]:
    """Generate all possible rectangles using red tiles as diagonal corners."""
    for i, p1 in enumerate(points):
        for p2 in points[i + 1 :]:
            area = get_area(p1, p2)
            yield p1, p2, area


def find_max_area(grouped_points: dict[int, list[int]]) -> int:
    """Find the maximum area formed by points with the same x-coordinate."""
    return max(get_areas(grouped_points), key=lambda item: item[2])[2]


def find_max_area_in_polygon(points: list[Point], polygon: set[Point]) -> int:
    """Find the maximum area formed by points within a polygon."""
    max_area = 0
    for i, p1 in enumerate(points):
        for p2 in points[i + 1 :]:
            p3, p4 = Point(p1.x, p2.y), Point(p2.x, p1.y)
            if p3 not in polygon or p4 not in polygon:
                print(f"Skipping rectangle with corners {p1}, {p2} - not fully inside polygon")
                continue
            area = get_area(p1, p2)
            max_area = max(max_area, area)
    return max_area


def part1(input_data: str) -> int:
    """Solve part 1 of day 9."""
    points = parse_input(input_data)
    grouped_points = group_by_x(points)
    return find_max_area(grouped_points)


def part2(input_data: str) -> int:
    """Solve part 2 of day 9."""
    points = parse_input(input_data)
    polygon = fill_polygon(points)
    return find_max_area_in_polygon(points, polygon)
