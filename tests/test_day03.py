"""Tests for day 3."""

from helpers import load_file

from advent_of_code_2025 import day03


def test_parse_input():
    """Test parsing the input data."""
    input_data = load_file(day=3, part=None, is_example=True)
    parsed = day03.parse_input(input_data)
    assert parsed is not None


def test_part1_example():
    """Test part 1 with example input."""
    input_data = load_file(day=3, part=None, is_example=True)
    result = day03.part1(input_data)
    # TODO: Update with expected result from puzzle
    assert result == 0


def test_part2_example():
    """Test part 2 with example input."""
    input_data = load_file(day=3, part=None, is_example=True)
    result = day03.part2(input_data)
    # TODO: Update with expected result from puzzle
    assert result == 0
