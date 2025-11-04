from pathlib import Path


def load_file(day: int, part: int | None, is_example: bool) -> str:
    """Load the input file for the given day, part, and example status."""
    suffix = "_example" if is_example else ""
    part_suffix = f"_part{part}" if part is not None else ""
    file_path = Path(f"./inputs/day{day:02d}{part_suffix}{suffix}.txt")
    return file_path.read_text().strip()
