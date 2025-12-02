from pathlib import Path


def load_file(day: int, part: int | None = None, is_example: bool = False, version_controlled: bool = True) -> str:
    """Load the input file for the given day, part, and example status.

    Args:
        day: Day number (1-25)
        part: Part number (1 or 2) or None
        is_example: Whether this is example input
        version_controlled: If True (default), loads from inputs/ directory (committed files).
                          If False, loads from inputs/private/ directory (gitignored AoC puzzle inputs).

    """
    suffix = "_example" if is_example else ""
    part_suffix = f"_part{part}" if part is not None else ""
    filename = f"day{day:02d}{part_suffix}{suffix}.txt"

    file_path = Path(f"./inputs/{filename}") if version_controlled else Path(f"./inputs/private/{filename}")
    return file_path.read_text().strip()
