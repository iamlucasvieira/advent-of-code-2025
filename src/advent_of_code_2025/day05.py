"""Day 5:

https://adventofcode.com/2025/day/5
"""

from typing import NamedTuple


class Range(NamedTuple):
    start: int
    end: int


def parse_input(input_data: str) -> tuple[list[Range], list[int]]:
    """Parse the input data for day 5."""
    ranges: list[Range] = []
    numbers: list[int] = []
    parsing_ranges = True
    for line in input_data.splitlines():
        line = line.strip()

        if not line:
            parsing_ranges = False
            continue

        if parsing_ranges:
            start, end = line.split("-")
            ranges.append(Range(int(start), int(end)))
        else:
            numbers.append(int(line))
    return ranges, numbers


def merge_ranges(ranges: list[Range]) -> list[Range]:
    """Merge overlapping and contiguous ranges."""
    if not ranges:
        return []
    sorted_ranges = sorted(ranges, key=lambda r: r.start)
    new_ranges: list[Range] = [sorted_ranges[0]]

    for current in sorted_ranges:
        previous = new_ranges[-1]
        if current.start <= previous.end:
            new_ranges[-1] = Range(previous.start, max(previous.end, current.end))
        else:
            new_ranges.append(current)
    return new_ranges


def is_number_in_ranges(number: int, sorted_ranges: list[Range]) -> bool:
    """Check if a number is within any of the given sorted ranges."""
    n_ranges = len(sorted_ranges)
    left, right = 0, n_ranges - 1

    while left <= right:
        mid = (left + right) // 2

        current_range = sorted_ranges[mid]

        if number < current_range.start:
            right = mid - 1
        elif number > current_range.end:
            left = mid + 1
        else:
            return True
    return False


def part1(input_data: str) -> int:
    """Solve part 1 of day 5."""
    ranges, numbers = parse_input(input_data)
    sorted_ranges = merge_ranges(ranges)
    return sum(is_number_in_ranges(n, sorted_ranges) for n in numbers)


def part2(input_data: str) -> int:
    """Solve part 2 of day 5."""
    ranges, _ = parse_input(input_data)
    sorted_ranges = merge_ranges(ranges)
    return sum(r.end - r.start + 1 for r in sorted_ranges)
