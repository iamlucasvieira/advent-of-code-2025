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


def part2(input_data: str) -> int:
    """Solve part 2 of day 7."""
    _data = parse_input(input_data)
    # TODO: Implement solution
    return 0
