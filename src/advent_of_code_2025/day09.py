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


def get_all_rectangle_candidates(points: list[Point]) -> Iterator[tuple[Point, Point, int]]:
    """Generate all possible rectangles using red tiles as diagonal corners."""
    for i, p1 in enumerate(points):
        for p2 in points[i + 1 :]:
            area = get_area(p1, p2)
            yield p1, p2, area


def find_max_area(grouped_points: dict[int, list[int]]) -> int:
    """Find the maximum area formed by points with the same x-coordinate."""
    return max(get_areas(grouped_points), key=lambda item: item[2])[2]


def get_green_lines(polygon: list[Point]) -> list[tuple[Point, Point]]:
    """Get all green line segments (edges between consecutive red tiles)."""
    lines = []
    for i in range(len(polygon)):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % len(polygon)]
        lines.append((p1, p2))
    return lines


def line_intersects_rectangle(line_start: Point, line_end: Point, rect_p1: Point, rect_p2: Point) -> bool:
    """Check if a line segment intersects the interior of a rectangle."""
    min_x, max_x = min(rect_p1.x, rect_p2.x), max(rect_p1.x, rect_p2.x)
    min_y, max_y = min(rect_p1.y, rect_p2.y), max(rect_p1.y, rect_p2.y)

    line_min_x, line_max_x = min(line_start.x, line_end.x), max(line_start.x, line_end.x)
    line_min_y, line_max_y = min(line_start.y, line_end.y), max(line_start.y, line_end.y)

    return line_min_x < max_x and line_max_x > min_x and line_min_y < max_y and line_max_y > min_y


def find_max_area_in_polygon(polygon: list[Point]) -> int:
    """Find the maximum area using green line intersection check."""

    candidates = sorted(get_all_rectangle_candidates(polygon), key=lambda x: x[2], reverse=True)

    green_lines = get_green_lines(polygon)
    green_lines.sort(key=lambda line: abs(line[1].x - line[0].x) + abs(line[1].y - line[0].y), reverse=True)

    for p1, p2, area in candidates:
        has_intersection = False
        for line_start, line_end in green_lines:
            if line_intersects_rectangle(line_start, line_end, p1, p2):
                has_intersection = True
                break

        if not has_intersection:
            return area

    return 0


def part1(input_data: str) -> int:
    """Solve part 1 of day 9."""
    points = parse_input(input_data)
    grouped_points = group_by_x(points)
    return find_max_area(grouped_points)


def part2(input_data: str) -> int:
    """Solve part 2 of day 9."""
    points = parse_input(input_data)
    return find_max_area_in_polygon(points)
