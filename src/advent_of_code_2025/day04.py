"""Day 4:

https://adventofcode.com/2025/day/4
"""

from collections.abc import Generator


def parse_input(input_data: str) -> list[list[str]]:
    """Parse the input data for day 4."""
    return [list(row) for row in input_data.splitlines()]


def neighbours(x: int, y: int, max_x: int, max_y: int) -> Generator[tuple[int, int], None, None]:
    directions = {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < max_x and 0 <= ny < max_y:
            yield (nx, ny)


def part1(input_data: str) -> int:
    """Solve part 1 of day 4."""
    data = parse_input(input_data)
    n_rows = len(data)
    n_cols = len(data[0]) if n_rows > 0 else 0

    result = 0

    for row in range(n_rows):
        for col in range(n_cols):
            cell = data[row][col]
            if cell == "@":
                count = sum(1 for nx, ny in neighbours(col, row, n_cols, n_rows) if data[ny][nx] == "@")
                if count < 4:
                    result += 1
    return result


def part2(input_data: str) -> int:
    """Solve part 2 of day 4."""
    _data = parse_input(input_data)
    # TODO: Implement solution
    return 0
