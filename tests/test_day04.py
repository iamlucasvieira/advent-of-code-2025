"""Tests for day 4."""

from helpers import load_file

from advent_of_code_2025 import day04


def test_parse_input():
    """Test parsing the input data."""
    input_data = load_file(day=4)
    parsed = day04.parse_input(input_data)
    assert parsed == [
        [".", "@", "."],
        ["@", ".", "."],
        [".", "@", "@"],
    ]


def test_part1_example():
    """Test part 1 with example input."""
    input_data = load_file(day=4)
    result = day04.part1(input_data)
    # TODO: Update with expected result from puzzle
    assert result == 4


def test_part2_example():
    """Test part 2 with example input."""
    input_data = load_file(day=4)
    result = day04.part2(input_data)
    # TODO: Update with expected result from puzzle
    assert result == 0
