def parse_input(input_data: str) -> list[int]:
    """Parse the input data for day 1."""
    return [int(n) for n in input_data.split()]


def part1(input_data: str) -> int:
    """Solve part 1 of day 1."""
    parsed_data = parse_input(input_data)
    expected_sum = 2020
    seen = set()

    for value in parsed_data:
        complement = expected_sum - value
        print(complement)
        if complement in seen:
            return value * complement
        seen.add(value)
    return -1


def part2(input_data: str) -> int:
    """Solve part 2 of day 1."""
    # Example implementation: find the maximum number in the input
    return 2
