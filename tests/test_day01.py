from helpers import TestFile

from advent_of_code_2025 import day01


def test_parse_input():
    test_file = TestFile(day=1)
    input_data = test_file.load()
    parsed = day01.parse_input(input_data)
    assert parsed == [-10, 20, -1, 5]
