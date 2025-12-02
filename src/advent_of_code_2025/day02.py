"""Day 2:

https://adventofcode.com/2025/day/2
"""

from collections.abc import Generator
from math import ceil


def parse_input(input_data: str) -> list[tuple[int, int]]:
    """Parse comma-separated ranges into list of (start, end) tuples."""
    ranges = []
    for range_str in input_data.strip().split(","):
        range_start, range_end = range_str.split("-")
        ranges.append((int(range_start), int(range_end)))
    return ranges


def generate_pattern_repeated_numbers(
    range_start: int, range_end: int, repetition_count: int
) -> Generator[int, None, None]:
    """Generate numbers formed by repeating a pattern a specified number of times within a range."""
    if range_end < range_start or repetition_count < 2:
        return

    pattern_length = ceil(len(str(range_start)) / repetition_count)
    min_pattern = 10 ** (pattern_length - 1)

    current_pattern = min_pattern
    while True:
        repeated_number = int(str(current_pattern) * repetition_count)

        if repeated_number > range_end:
            break

        if repeated_number >= range_start:
            yield repeated_number

        current_pattern += 1


def part1(input_data: str) -> int:
    """Sum all numbers that are a pattern repeated exactly twice."""
    ranges = parse_input(input_data)
    total = 0
    for range_start, range_end in ranges:
        total += sum(generate_pattern_repeated_numbers(range_start, range_end, repetition_count=2))
    return total


def part2(input_data: str) -> int:
    """Sum all numbers that are a pattern repeated two or more times."""
    ranges = parse_input(input_data)
    total = 0

    for range_start, range_end in ranges:
        unique_numbers = set()
        max_repetitions = len(str(range_end))

        for repetition_count in range(2, max_repetitions + 1):
            unique_numbers.update(generate_pattern_repeated_numbers(range_start, range_end, repetition_count))

        total += sum(unique_numbers)

    return total
