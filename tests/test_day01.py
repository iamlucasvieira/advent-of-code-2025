from helpers import load_file

from advent_of_code_2020 import day01


def test_parse_input():

    input_data = load_file(day=1, part=None, is_example=True)
    parsed = day01.parse_input(input_data)
    assert parsed == [1721, 979, 366, 299, 675, 1456]
