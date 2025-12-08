"""Tests for day 8."""

from helpers import load_file

from advent_of_code_2025 import day08


def test_parse_input():
    """Test parsing the input data."""
    input_data = load_file(day=8)
    parsed = day08.parse_input(input_data)
    assert parsed[0] == (1, 2, 3)


def test_part1_example():
    """Test part 1 with example input."""
    input_data = load_file(day=8)
    result = day08.part1(input_data, num_connections=10)
    assert result == 4


def test_part2_example():
    """Test part 2 with example input."""
    input_data = load_file(day=8)
    result = day08.part2(input_data)
    # TODO: Update with expected result from puzzle
    assert result == 44
