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
    ("numbers", "n", "expected"),
    [
        ([1, 3, 2, 5, 4], 2, [5, 4]),
        ([1, 2, 3, 9], 2, [3, 9]),
        ([5, 1, 5, 2], 2, [5, 5]),
        ([2, 3, 5, 1, 2, 6, 9, 2], 5, [5, 2, 6, 9, 2]),
    ],
    ids=[
        "2 largest in middle",
        "2 largest at end",
        "2 duplicate largest",
        "5 largest mixed",
    ],
)
def test_n_largest_in_sequence(numbers: list[int], n: int, expected: tuple[int, int]):
    """Test finding the two largest numbers in a sequence."""
    result = day03.n_largest_in_sequence(numbers, n=n)
    assert result == expected


def test_part1_example():
    """Test part 1 with example input."""
    input_data = load_file(day=3)
    result = day03.part1(input_data)
    assert result == 168
