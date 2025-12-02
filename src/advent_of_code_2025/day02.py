"""Day 2:

https://adventofcode.com/2025/day/2
"""

from collections.abc import Generator


def parse_input(input_data: str) -> list[tuple[int, int]]:
    """Parse the input data for day 2."""
    data = []
    ranges = input_data.strip().split(",")
    for r in ranges:
        start, end = r.split("-")
        data.append((int(start), int(end)))
    return data


def repeated_numbers(start: int, end: int) -> Generator[int, None, None]:
    """Generate numbers with repeated digits in the given range."""
    if end < start:
        return

    start_len = len(str(start))
    if start_len % 2 != 0:
        start = 10**start_len

    half = int(str(start)[: len(str(start)) // 2])

    while True:
        repeated = int(f"{half}{half}")

        if repeated > end:
            break

        if repeated >= start:
            yield repeated

        half += 1


def part1(input_data: str) -> int:
    """Solve part 1 of day 2."""
    data = parse_input(input_data)
    total = 0
    for start, end in data:
        total += sum(repeated_numbers(start, end))
    return total


def part2(input_data: str) -> int:
    """Solve part 2 of day 2."""
    _data = parse_input(input_data)
    # TODO: Implement solution
    return 0
