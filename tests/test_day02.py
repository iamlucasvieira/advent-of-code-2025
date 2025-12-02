"""Tests for day 2."""

import pytest
from helpers import load_file

from advent_of_code_2025 import day02


def test_parse_input():
    """Test parsing the input data."""
    input_data = load_file(day=2)
    parsed = day02.parse_input(input_data)
    assert parsed == [(10, 99), (100, 999)]


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
    result = list(day02.generate_pattern_repeated_numbers(start, end, repetition_count=2))
    assert result == expected


@pytest.mark.parametrize(
    ("start", "end", "n_times", "expected"),
    [
        (1000, 2000, 0, []),
        (1000, 2000, 1, []),
        (1000, 2000, 2, [1010, 1111, 1212, 1313, 1414, 1515, 1616, 1717, 1818, 1919]),
        (1000, 2000, 3, []),
        (1000, 2000, 4, [1111]),
        (1000, 2000, 5, []),
    ],
    ids=[
        "zero_parts",
        "single_repeats",
        "double_repeats",
        "triple_repeats",
        "quadruple_repeats",
        "quintuple_repeats",
    ],
)
def test_repeated_numbers_varied_n(start, end, n_times, expected):
    """Test generating repeated numbers in a range with varied n_times."""
    result = list(day02.generate_pattern_repeated_numbers(start, end, repetition_count=n_times))
    assert result == expected
