"""Tests for day 9."""

import pytest
from helpers import load_file

from advent_of_code_2025 import day09


def test_parse_input():
    """Test parsing the input data."""
    input_data = load_file(day=9)
    parsed = day09.parse_input(input_data)
    assert len(parsed) == 4
    assert parsed[0] == day09.Point(0, 0)


@pytest.mark.parametrize(
    ("point", "expected"),
    [
        (day09.Point(2, 2), True),
        (day09.Point(6, 6), False),
        (day09.Point(0, 0), True),
        (day09.Point(5, 0), True),
        (day09.Point(5, 5), True),
        (day09.Point(0, 5), True),
        (day09.Point(0, 3), True),
    ],
)
def test_in_squared_polygon(point, expected):
    """Test the in_polygon function."""
    input_data = load_file(day=9)
    polygon = day09.parse_input(input_data)
    assert day09.in_squared_polygon(point, polygon) == expected


def test_part1_example():
    """Test part 1 with example input."""
    input_data = load_file(day=9)
    result = day09.part1(input_data)
    assert result == 36


def test_part2_example():
    """Test part 2 with example input."""
    input_data = load_file(day=9)
    result = day09.part2(input_data)
    # TODO: Update with expected result from puzzle
    assert result == 36
