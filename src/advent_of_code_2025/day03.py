"""Day 3:

https://adventofcode.com/2025/day/3
"""


def parse_input(input_data: str) -> list[list[int]]:
    """Parse the input data for day 3."""
    lines = input_data.strip().splitlines()
    data = [[int(char) for char in line] for line in lines]
    return data


def two_largest_in_sequence(numbers: list[int]) -> tuple[int, int]:
    """Returns the first largest number and the second largest after it in a sequence."""
    first = second = -1
    len_numbers = len(numbers)
    for current_idx, number in enumerate(numbers):
        if number > first and current_idx < len_numbers - 1:
            first = number
            second = numbers[current_idx + 1]
        elif number > second:
            second = number
    return first, second


def part1(input_data: str) -> int:
    """Solve part 1 of day 3."""
    data = parse_input(input_data)
    total = 0
    for row in data:
        first, second = two_largest_in_sequence(row)
        total += int(f"{first}{second}")
    return total


def part2(input_data: str) -> int:
    """Solve part 2 of day 3."""
    _data = parse_input(input_data)
    # TODO: Implement solution
    return 0
