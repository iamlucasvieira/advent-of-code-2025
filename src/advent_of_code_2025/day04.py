"""Day 4:

https://adventofcode.com/2025/day/4
"""

from collections import deque
from collections.abc import Generator

from pydantic.dataclasses import dataclass


@dataclass
class Grid:
    data: list[list[str]]
    n_rows: int
    n_cols: int

    def get(self, pos: tuple[int, int]) -> str:
        """Get cell value at position (col, row)."""
        col, row = pos
        return self.data[row][col]

    def set(self, pos: tuple[int, int], value: str) -> None:
        """Set cell value at position (col, row)."""
        col, row = pos
        self.data[row][col] = value

    def is_roll(self, pos: tuple[int, int]) -> bool:
        """Check if position contains a roll."""
        return self.get(pos) == "@"

    def __iter__(self) -> Generator[tuple[int, int], None, None]:
        """Iterate over all positions in the grid."""
        for row in range(self.n_rows):
            for col in range(self.n_cols):
                yield (col, row)


def parse_input(input_data: str) -> Grid:
    """Parse the input data for day 4."""
    data = [list(line) for line in input_data.strip().splitlines()]
    n_rows = len(data)
    n_cols = len(data[0]) if n_rows > 0 else 0
    return Grid(data=data, n_rows=n_rows, n_cols=n_cols)


def neighbours(position: tuple[int, int], max_x: int, max_y: int) -> Generator[tuple[int, int], None, None]:
    x, y = position
    directions = {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < max_x and 0 <= ny < max_y:
            yield (nx, ny)


def count_adjacent_rolls(grid: Grid, position: tuple[int, int]) -> int:
    return sum(
        1 for neighbour_position in neighbours(position, grid.n_cols, grid.n_rows) if grid.is_roll(neighbour_position)
    )


def is_accessible(grid: Grid, pos: tuple[int, int]) -> bool:
    """Check if a roll at position is accessible (< 4 adjacent rolls)."""
    return grid.is_roll(pos) and count_adjacent_rolls(grid, pos) < 4


def part1(input_data: str) -> int:
    """Solve part 1 of day 4."""
    grid = parse_input(input_data)
    return sum(1 for position in grid if is_accessible(grid, position))


def part2(input_data: str) -> int:
    """Solve part 2 of day 4."""
    grid = parse_input(input_data)
    queue = deque(position for position in grid if is_accessible(grid, position))
    removed = 0

    while queue:
        position = queue.popleft()

        if not is_accessible(grid, position):
            continue

        grid.set(position, ".")
        removed += 1

        for neighbour_position in neighbours(position, grid.n_cols, grid.n_rows):
            if is_accessible(grid, neighbour_position):
                queue.append(neighbour_position)

    return removed
