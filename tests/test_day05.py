"""Tests for day 5."""

import pytest
from helpers import load_file

from advent_of_code_2025 import day05


def test_parse_input():
    """Test parsing the input data."""
    input_data = load_file(day=5)
    ranges, numbers = day05.parse_input(input_data)
    assert ranges == [(1, 3), (20, 30), (4, 5), (100, 200), (15, 25)]
    assert numbers == [1, 5, 150, 200, 75]


@pytest.mark.parametrize(
    ("ranges", "expected"),
    [
        ([(1, 3), (5, 7), (2, 4)], [(1, 4), (5, 7)]),
        ([(10, 20), (1, 15), (18, 25)], [(1, 25)]),
        ([(1, 5), (6, 10), (11, 15)], [(1, 5), (6, 10), (11, 15)]),
    ],
    ids=[
        "1_overlapping_ranges",
        "all_overlapping_ranges",
        "no_overlapping_ranges",
    ],
)
def test_merge_ranges(ranges: list[tuple[int, int]], expected: list[tuple[int, int]]):
    """Test merging overlapping ranges."""
    corrected_ranges = [day05.Range(start, end) for start, end in ranges]
    merged = day05.merge_ranges(corrected_ranges)
    assert merged == expected


@pytest.mark.parametrize(
    ("number", "ranges", "expected"),
    [
        (1, [(1, 2), (5, 6)], True),
        (1, [(2, 3), (5, 9), (10, 20)], False),
        (20, [(10, 15), (9, 30), (0, 8)], True),
        (20, [(2, 3), (5, 9), (10, 20)], True),
    ],
    ids=[
        "equal_start",
        "outside",
        "inside",
        "equal_end",
    ],
)
def test_is_number_in_ranges(number: int, ranges: list[tuple[int, int]], expected: bool) -> None:
    corrected_ranges = [day05.Range(start, end) for start, end in ranges]
    sorted_ranges = day05.merge_ranges(corrected_ranges)
    assert day05.is_number_in_ranges(number, sorted_ranges) == expected


def test_part1_example():
    """Test part 1 with example input."""
    input_data = load_file(day=5)
    result = day05.part1(input_data)
    # TODO: Update with expected result from puzzle
    assert result == 4


def test_part2_example():
    """Test part 2 with example input."""
    input_data = load_file(day=5)
    result = day05.part2(input_data)
    # TODO: Update with expected result from puzzle
    assert result == 0
