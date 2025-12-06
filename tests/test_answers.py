"""Test framework for Advent of Code solutions."""

from collections.abc import Callable
from typing import Any

import pytest
from helpers import InputFile
from pydantic import BaseModel, computed_field

from advent_of_code_2025 import day01, day02, day03, day04, day05, day06


class AocTest(BaseModel):
    """Test case for an Advent of Code solution.

    Args:
        test_file: InputFile instance specifying which input file to load
        function: Function to test (e.g., day01.part1)
        expected: Expected result
        id: Optional custom test ID for pytest output
    """

    model_config = {"frozen": True}

    test_file: InputFile
    function: Callable[[str], Any]
    expected: int | str
    id: str | None = None

    @computed_field
    @property
    def test_id(self) -> str:
        """Generate readable test ID for pytest output.

        Format: {file_identifier}-{function_name}
        Example: day01_example-part1
        """
        if self.id:
            return self.id
        # Extract function name (e.g., 'part1' from 'day01.part1')
        func_name = getattr(self.function, "__name__", "unknown")
        return f"{self.test_file.file_identifier}-{func_name}"

    def read_input(self) -> str:
        """Read and return the input file contents."""
        return self.test_file.load()


# Example usage - define your test cases here
TEST_CASES: list[AocTest] = [
    AocTest(
        test_file=InputFile(day=1, is_example=True, version_controlled=False),
        function=day01.part1,
        expected=3,
    ),
    AocTest(
        test_file=InputFile(day=1, is_example=False, version_controlled=False),
        function=day01.part1,
        expected=1102,
    ),
    AocTest(
        test_file=InputFile(day=1, is_example=True, version_controlled=False),
        function=day01.part2,
        expected=6,
    ),
    AocTest(
        test_file=InputFile(day=1, is_example=False, version_controlled=False),
        function=day01.part2,
        expected=6175,
    ),
    AocTest(
        test_file=InputFile(day=2, is_example=True, version_controlled=False),
        function=day02.part1,
        expected=1227775554,
    ),
    AocTest(
        test_file=InputFile(day=2, is_example=False, version_controlled=False),
        function=day02.part1,
        expected=41294979841,
    ),
    AocTest(
        test_file=InputFile(day=2, is_example=True, version_controlled=False),
        function=day02.part2,
        expected=4174379265,
    ),
    AocTest(
        test_file=InputFile(day=2, is_example=False, version_controlled=False),
        function=day02.part2,
        expected=66500947346,
    ),
    AocTest(
        test_file=InputFile(day=3, is_example=True, version_controlled=False),
        function=day03.part1,
        expected=357,
    ),
    AocTest(
        test_file=InputFile(day=3, is_example=False, version_controlled=False),
        function=day03.part1,
        expected=17100,
    ),
    AocTest(
        test_file=InputFile(day=3, is_example=True, version_controlled=False),
        function=day03.part2,
        expected=3121910778619,
    ),
    AocTest(
        test_file=InputFile(day=3, is_example=False, version_controlled=False),
        function=day03.part2,
        expected=170418192256861,
    ),
    AocTest(
        test_file=InputFile(day=4, is_example=True, version_controlled=False),
        function=day04.part1,
        expected=13,
    ),
    AocTest(
        test_file=InputFile(day=4, is_example=False, version_controlled=False),
        function=day04.part1,
        expected=1537,
    ),
    AocTest(
        test_file=InputFile(day=4, is_example=True, version_controlled=False),
        function=day04.part2,
        expected=43,
    ),
    AocTest(
        test_file=InputFile(day=4, is_example=False, version_controlled=False),
        function=day04.part2,
        expected=8707,
    ),
    AocTest(
        test_file=InputFile(day=5, is_example=True, version_controlled=False),
        function=day05.part1,
        expected=3,
    ),
    AocTest(
        test_file=InputFile(day=5, is_example=False, version_controlled=False),
        function=day05.part1,
        expected=638,
    ),
    AocTest(
        test_file=InputFile(day=5, is_example=True, version_controlled=False),
        function=day05.part2,
        expected=14,
    ),
    AocTest(
        test_file=InputFile(day=5, is_example=False, version_controlled=False),
        function=day05.part2,
        expected=352946349407338,
    ),
    AocTest(
        test_file=InputFile(day=6, is_example=True, version_controlled=False),
        function=day06.part1,
        expected=4277556,
    ),
    AocTest(
        test_file=InputFile(day=6, is_example=False, version_controlled=False),
        function=day06.part1,
        expected=4693419406682,
    ),
]


@pytest.mark.parametrize(
    "test_case",
    TEST_CASES,
    ids=lambda tc: tc.test_id,
)
def test_aoc_solutions(test_case: AocTest):
    """Test Advent of Code solutions."""
    input_data = test_case.read_input()
    result = test_case.function(input_data)
    assert result == test_case.expected
