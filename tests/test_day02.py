"""Tests for day 2."""

import pytest
from helpers import load_file

from advent_of_code_2025 import day02


def test_parse_input():
    """Test parsing the input data."""
    input_data = load_file(day=2, part=None, is_example=True)
    parsed = day02.parse_input(input_data)
    for start, end in parsed:
        assert isinstance(start, int)
        assert isinstance(end, int)


@pytest.mark.parametrize(
    ("start", "end", "expected"),
    [
        (10, 99, [11, 22, 33, 44, 55, 66, 77, 88, 99]),
        (100, 110, []),
        (100, 1010, [1010]),
        (1010, 1020, [1010]),
        (1000, 2000, [1010, 1111, 1212, 1313, 1414, 1515, 1616, 1717, 1818, 1919]),
        (1030, 2000, [1111, 1212, 1313, 1414, 1515, 1616, 1717, 1818, 1919]),
    ],
    ids=[
        "two_digit_repeats",
        "no_repeats_in_range",
        "single_repeat_at_end",
        "single_repeat_at_start",
        "thousand_to_two_thousand",
        "thousand_to_two_thousand_exclude_start",
    ],
)
def test_repeated_numbers(start, end, expected):
    """Test generating repeated numbers in a range."""
    result = list(day02.repeated_numbers(start, end))
    assert result == expected
