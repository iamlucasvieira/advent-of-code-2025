"""Day 3:

https://adventofcode.com/2025/day/3
"""


def parse_input(input_data: str) -> list[list[int]]:
    """Parse the input data for day 3."""
    lines = input_data.strip().splitlines()
    data = [[int(char) for char in line] for line in lines]
    return data


def n_largest_in_sequence(numbers: list[int], n: int) -> list[int]:
    """Returns the n largest numbers in a sequence in order of appearance."""
    n_candidates = len(numbers)
    largest_numbers = [-1] * n
    for candidate_idx, candidate in enumerate(numbers):
        for i in range(n):
            candidates_left = n_candidates - (candidate_idx + 1)
            positions_available = n - (i + 1)
            current_largest = largest_numbers[i]
            if candidate > current_largest and candidates_left >= positions_available:
                largest_numbers[i] = candidate
                if i < n - 1:
                    largest_numbers[i + 1 :] = [-1] * (n - (i + 1))
                break
    return largest_numbers


def list_to_int(digits: list[int]) -> int:
    """Transform a list of integers into a single integer by concatenating the digits."""
    print("".join(str(digit) for digit in digits))
    return int("".join(str(digit) for digit in digits))


def part1(input_data: str) -> int:
    """Solve part 1 of day 3."""
    data = parse_input(input_data)
    return sum(list_to_int(n_largest_in_sequence(row, n=2)) for row in data)


def part2(input_data: str) -> int:
    """Solve part 2 of day 3."""
    data = parse_input(input_data)
    return sum(list_to_int(n_largest_in_sequence(row, n=12)) for row in data)
