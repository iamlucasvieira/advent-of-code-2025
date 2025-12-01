from helpers import load_file

from advent_of_code_2025 import day01


def test_parse_input():
    input_data = load_file(day=1, part=None, is_example=True)
    parsed = day01.parse_input(input_data)
    assert parsed == [-68, -30, 48, -5, 60, -55, -1, -99, 14, -82]
