"""Tests for day 7."""

from helpers import load_file

from advent_of_code_2025 import day07


def test_parse_input():
    """Test parsing the input data."""
    input_data = load_file(day=7)
    grid, start_point = day07.parse_input(input_data)
    assert grid.n_rows == 6
    assert grid.n_cols == 7
    assert start_point == day07.Point(row=0, col=3)
    assert grid.get_cell(start_point) == "S"


def test_part1_example():
    """Test part 1 with example input."""
    input_data = load_file(day=7)
    result = day07.part1(input_data)
    assert result == 3


def test_part2_example():
    """Test part 2 with example input."""
    input_data = load_file(day=7)
    result = day07.part2(input_data)
    assert result == 4
