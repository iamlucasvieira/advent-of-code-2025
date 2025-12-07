"""Day 7:

https://adventofcode.com/2025/day/7
"""

from collections import deque
from typing import NamedTuple

from pydantic.dataclasses import dataclass


class Point(NamedTuple):
    row: int
    col: int


@dataclass
class Grid:
    n_rows: int
    n_cols: int
    _cells: list[list[str]]

    def get_cell(self, point: Point) -> str | None:
        """Get the cell value at the given point."""
        if 0 <= point.row < self.n_rows and 0 <= point.col < self.n_cols:
            return self._cells[point.row][point.col]
        return None


def parse_input(input_data: str) -> tuple[Grid, Point]:
    """Parse the input data for day 7."""
    cells = []
    start_pos: Point = Point(-1, -1)
    for row_idx, line in enumerate(input_data.splitlines()):
        cells.append(list(line))
        if "S" in line:
            start_pos = Point(row=row_idx, col=line.index("S"))
    cells = [list(line) for line in input_data.splitlines()]
    n_rows = len(cells)
    n_cols = len(cells[0]) if n_rows > 0 else 0
    return Grid(n_rows=n_rows, n_cols=n_cols, _cells=cells), start_pos


def part1(input_data: str) -> int:
    """Solve part 1 of day 7."""
    grid, start = parse_input(input_data)

    queue: deque[Point] = deque([start])
    visited: set[Point] = set()
    splits = 0

    while queue:
        current = queue.popleft()

        while (current_value := grid.get_cell(current)) and current not in visited:
            visited.add(current)
            if current_value == "^":
                splits += 1

                left_point = Point(row=current.row, col=current.col - 1)
                right_point = Point(row=current.row, col=current.col + 1)
                queue.appendleft(left_point)
                queue.appendleft(right_point)
                break

            current = Point(row=current.row + 1, col=current.col)
    return splits


def count_timelines(grid: Grid, pos: Point, memo: dict[Point, int]) -> int:
    """Count the number of timelines from the given position."""

    if grid.get_cell(pos) is None:
        return 0

    if pos.row == grid.n_rows - 1:
        return 1

    if pos in memo:
        return memo[pos]

    total_timelines = 0

    if grid.get_cell(pos) == "^":
        left_point = Point(row=pos.row, col=pos.col - 1)
        right_point = Point(row=pos.row, col=pos.col + 1)
        total_timelines += count_timelines(grid, left_point, memo)
        total_timelines += count_timelines(grid, right_point, memo)
    else:
        down_point = Point(row=pos.row + 1, col=pos.col)
        total_timelines += count_timelines(grid, down_point, memo)

    memo[pos] = total_timelines
    return total_timelines


def part2(input_data: str) -> int:
    """Solve part 2 of day 7."""
    grid, start = parse_input(input_data)
    memo: dict[Point, int] = {}
    return count_timelines(grid, start, memo)
