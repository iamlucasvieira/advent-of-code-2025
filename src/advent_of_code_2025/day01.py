def parse_input(input_data: str) -> list[int]:
    """Parse the input data for day 1."""
    direction_mapping = {"L": -1, "R": 1}
    numbers = []
    for line in input_data.splitlines():
        direction, value = line[0], line[1:]
        numbers.append(direction_mapping[direction] * int(value))
    return numbers


def part1(input_data: str, start: int = 50) -> int:
    """Solve part 1 of day 1."""
    numbers = parse_input(input_data)
    total, counter = start, 0
    for n in numbers:
        total += n
        if total % 100 == 0:
            counter += 1
    return counter


def part2(input_data: str) -> int:
    """Solve part 2 of day 1."""
    # Example implementation: find the maximum number in the input
    return 2
