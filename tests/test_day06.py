"""Tests for day 6."""

from helpers import load_file

from advent_of_code_2025 import day06


def test_parse_input():
    """Test parsing the input data."""
    input_data = load_file(day=6)
    parsed = day06.parse_input(input_data)
    assert parsed[0].numbers == [10, 2]
    assert parsed[0].operation == day06.OPERATIONS["+"]
    assert parsed[1].numbers == [20, 5]
    assert parsed[1].operation == day06.OPERATIONS["*"]


def test_part1_example():
    """Test part 1 with example input."""
    input_data = load_file(day=6)
    result = day06.part1(input_data)
    # TODO: Update with expected result from puzzle
    assert result == 112


def test_part2_example():
    """Test part 2 with example input."""
    input_data = load_file(day=6)
    result = day06.part2(input_data)
    # TODO: Update with expected result from puzzle
    assert result == 0
