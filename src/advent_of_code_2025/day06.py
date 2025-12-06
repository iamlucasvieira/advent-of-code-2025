"""Day 6:

https://adventofcode.com/2025/day/6
"""

from collections.abc import Callable
from math import prod

from pydantic.dataclasses import dataclass

OPERATIONS: dict[str, Callable[[list[int]], int]] = {
    "+": sum,
    "*": prod,
}


@dataclass
class Problem:
    numbers: list[int]
    operation: Callable[[list[int]], int]

    def solve(self) -> int:
        return self.operation(self.numbers)


def parse_input(input_data: str) -> list[Problem]:
    """Parse the input data for day 6."""
    *number_lines, operations_line = input_data.strip().splitlines()
    operations = operations_line.split()
    problems = [Problem(numbers=[], operation=OPERATIONS[op]) for op in operations]

    for line in number_lines:
        for idx, char in enumerate(line.split()):
            problems[idx].numbers.append(int(char))
    return problems


def parse_input_columns(input_data: str) -> list[Problem]:
    """Parse the input data for day 6 respecting column spaces."""
    *number_lines, operations_line = input_data.strip().splitlines()
    operations = operations_line.split()
    problems = [Problem(numbers=[], operation=OPERATIONS[op]) for op in operations]

    all_numbers = ["" for _ in range(len(number_lines[0]))]
    for line in number_lines:
        for idx, char in enumerate(line):
            all_numbers[idx] += char

    current_probem = 0
    for number in all_numbers:
        stripped_number = number.strip()
        if stripped_number:
            problems[current_probem].numbers.append(int(stripped_number))
        else:
            current_probem += 1
    return problems


def part1(input_data: str) -> int:
    """Solve part 1 of day 6."""
    problems = parse_input(input_data)
    return sum(problem.solve() for problem in problems)


def part2(input_data: str) -> int:
    """Solve part 2 of day 6."""
    problems = parse_input_columns(input_data)
    return sum(problem.solve() for problem in problems)
