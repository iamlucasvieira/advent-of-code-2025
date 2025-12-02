"""Day 2:

https://adventofcode.com/2025/day/2
"""

from collections.abc import Generator
from math import ceil


def parse_input(input_data: str) -> list[tuple[int, int]]:
    """Parse the input data for day 2."""
    data = []
    ranges = input_data.strip().split(",")
    for r in ranges:
        start, end = r.split("-")
        data.append((int(start), int(end)))
    return data


def repeated_numbers(start: int, end: int, n_times: int) -> Generator[int, None, None]:
    """Generate numbers with repeated digits in the given range."""
    if end < start or n_times < 2:
        return

    part_length = ceil(len(str(start)) / n_times)
    part = 10 ** (part_length - 1)

    while True:
        repeated = int(f"{part}" * n_times)

        if repeated > end:
            break

        if repeated >= start:
            yield repeated

        part += 1


def part1(input_data: str) -> int:
    """Solve part 1 of day 2."""
    data = parse_input(input_data)
    total = 0
    for start, end in data:
        total += sum(repeated_numbers(start, end, n_times=2))
    return total


def part2(input_data: str) -> int:
    """Solve part 2 of day 2."""
    data = parse_input(input_data)
    total = 0

    for start, end in data:
        sub_total = set()
        for n_times in range(2, len(str(end)) + 1):
            sub_total.update(repeated_numbers(start, end, n_times=n_times))
        total += sum(sub_total)
    return total
