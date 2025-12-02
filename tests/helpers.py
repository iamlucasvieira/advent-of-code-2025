from pathlib import Path

import pytest
from pydantic import BaseModel, field_validator


class TestFile(BaseModel):
    """Represents an Advent of Code input file.

    Args:
        day: Day number (1-25)
        part: Part number (1 or 2) or None
        is_example: Whether this is example input
        version_controlled: If True (default), loads from inputs/ directory (committed files).
                          If False, loads from inputs/private/ directory (gitignored AoC puzzle inputs).
    """

    model_config = {"frozen": True}

    day: int
    part: int | None = None
    is_example: bool = False
    version_controlled: bool = True

    @field_validator("day")
    @classmethod
    def validate_day(cls, v: int) -> int:
        """Ensure day is 1-25."""
        if not 1 <= v <= 25:
            raise ValueError
        return v

    @field_validator("part")
    @classmethod
    def validate_part(cls, v: int | None) -> int | None:
        """Ensure part is 1, 2, or None."""
        if v is not None and v not in (1, 2):
            raise ValueError
        return v

    @property
    def file_identifier(self) -> str:
        """Generate file identifier based on naming convention (without extension).

        Returns:
            File identifier like 'day01_example', 'day01', or 'day01_part1_example'
        """
        suffix = "_example" if self.is_example else ""
        part_suffix = f"_part{self.part}" if self.part is not None else ""
        return f"day{self.day:02d}{part_suffix}{suffix}"

    @property
    def filename(self) -> str:
        """Generate the filename with .txt extension.

        Returns:
            Filename like 'day01_example.txt', 'day01.txt', or 'day01_part1_example.txt'
        """
        return f"{self.file_identifier}.txt"

    @property
    def file_path(self) -> Path:
        """Generate the full file path based on version_controlled setting.

        Returns:
            Path to the input file
        """
        if self.version_controlled:
            return Path(f"./inputs/{self.filename}")
        return Path(f"./inputs/private/{self.filename}")

    def load(self) -> str:
        """Load and return the input file contents.

        Returns:
            File contents as a string, stripped of trailing whitespace.

        Raises:
            FileNotFoundError: If version_controlled is True and file doesn't exist.
            pytest.skip: If version_controlled is False and file doesn't exist.
        """
        try:
            return self.file_path.read_text().strip()
        except FileNotFoundError:
            if self.version_controlled:
                raise
            pytest.skip(f"Input file for day {self.day} not found")


def load_file(day: int, part: int | None = None, is_example: bool = False, version_controlled: bool = True) -> str:
    """Load the input file for the given day, part, and example status.

    This is a convenience function that creates a TestFile and calls load() on it.

    Args:
        day: Day number (1-25)
        part: Part number (1 or 2) or None
        is_example: Whether this is example input
        version_controlled: If True (default), loads from inputs/ directory (committed files).
                          If False, loads from inputs/private/ directory (gitignored AoC puzzle inputs).

    Returns:
        File contents as a string, stripped of trailing whitespace.
    """
    test_file = TestFile(
        day=day,
        part=part,
        is_example=is_example,
        version_controlled=version_controlled,
    )
    return test_file.load()
