"""Tests for day 9."""

from helpers import load_file

from advent_of_code_2025 import day09


def test_parse_input():
    """Test parsing the input data."""
    input_data = load_file(day=9)
    parsed = day09.parse_input(input_data)
    assert len(parsed) == 5
    assert parsed[0] == day09.Point(0, 0)


def test_part1_example():
    """Test part 1 with example input."""
    input_data = load_file(day=9)
    result = day09.part1(input_data)
    assert result == 12


def test_part2_example():
    """Test part 2 with example input."""
    input_data = load_file(day=9)
    result = day09.part2(input_data)
    # TODO: Update with expected result from puzzle
    assert result == 0
