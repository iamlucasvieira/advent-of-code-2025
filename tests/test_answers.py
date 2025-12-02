"""Test framework for Advent of Code solutions."""

from collections.abc import Callable
from pathlib import Path

import pytest
from helpers import load_file
from pydantic import BaseModel, computed_field, field_validator

from advent_of_code_2025 import day01, day02


class AocTest(BaseModel):
    """Test case for an Advent of Code solution.

    Args:
        day: Day number (1-25)
        part: Part number (1 or 2)
        expected: Expected result
        is_example: Whether this is example input (True) or puzzle input (False)
        input_file: Optional custom input file path. If None, uses convention:
                   - inputs/day{day:02d}_example.txt for examples
                   - inputs/day{day:02d}.txt for puzzle input
        id: Optional custom test ID for pytest output
    """

    model_config = {"frozen": True}

    day: int
    part: int | None = None
    expected: int | str
    is_example: bool = False
    input_file: Path | None = None
    id: str | None = None
    function: Callable

    @field_validator("day")
    @classmethod
    def validate_day(cls, v: int) -> int:
        """Ensure day is 1-25."""
        if not 1 <= v <= 25:
            raise ValueError()
        return v

    @field_validator("part")
    @classmethod
    def validate_part(cls, v: int) -> int:
        """Ensure part is 1 or 2."""
        if v not in (1, 2):
            raise ValueError()
        return v

    @computed_field
    @property
    def test_id(self) -> str:
        """Generate readable test ID for pytest output."""
        if self.id:
            return self.id
        example = "_example" if self.is_example else "_input"
        part = "" if self.part is None else f"_part{self.part}"
        return f"day{self.day:02d}{part}{example}"

    def read_input(self) -> str:
        """Read and return the input file contents."""
        if self.input_file:
            if not self.input_file.exists():
                pytest.skip(f"Input file {self.input_file} not found")
            return self.input_file.read_text().strip()
        try:
            return load_file(self.day, self.part, self.is_example)
        except FileNotFoundError:
            pytest.skip(f"Input file for day {self.day} part {self.part} not found")


# Example usage - define your test cases here
TEST_CASES: list[AocTest] = [
    AocTest(
        day=1,
        expected=3,
        is_example=True,
        function=day01.part1,
    ),
    AocTest(
        day=1,
        expected=1102,
        is_example=False,
        function=day01.part1,
    ),
    AocTest(
        day=1,
        expected=6,
        is_example=True,
        function=day01.part2,
    ),
    AocTest(
        day=1,
        expected=6175,
        is_example=False,
        function=day01.part2,
    ),
    AocTest(
        day=2,
        expected=1227775554,
        is_example=True,
        function=day02.part1,
    ),
    AocTest(
        day=2,
        expected=41294979841,
        is_example=False,
        function=day02.part1,
    ),
    AocTest(
        day=2,
        expected=4174379265,
        is_example=True,
        function=day02.part2,
    ),
    AocTest(
        day=2,
        expected=66500947346,
        is_example=False,
        function=day02.part2,
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
