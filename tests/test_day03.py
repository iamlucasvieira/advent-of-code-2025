"""Tests for day 3."""

import pytest
from helpers import load_file

from advent_of_code_2025 import day03


def test_parse_input():
    """Test parsing the input data."""
    input_data = load_file(day=3)
    parsed = day03.parse_input(input_data)
    assert parsed == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


@pytest.mark.parametrize(
    ("numbers", "expected"),
    [
        ([1, 3, 2, 5, 4], (5, 4)),
        ([1, 2, 3, 9], (3, 9)),
        ([5, 1, 5, 2], (5, 5)),
    ],
    ids=[
        "largest in middle",
        "largest at end",
        "duplicate largest",
    ],
)
def test_two_largest_in_sequence(numbers: list[int], expected: tuple[int, int]):
    """Test finding the two largest numbers in a sequence."""
    result = day03.two_largest_in_sequence(numbers)
    assert result == expected


def test_part1_example():
    """Test part 1 with example input."""
    input_data = load_file(day=3)
    result = day03.part1(input_data)
    assert result == 168


def test_part2_example():
    """Test part 2 with example input."""
    input_data = load_file(day=3)
    result = day03.part2(input_data)
    # TODO: Update with expected result from puzzle
    assert result == 0
