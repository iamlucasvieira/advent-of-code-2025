"""Command to show completion status."""

import importlib
import inspect
from pathlib import Path

from rich.console import Console
from rich.table import Table

console = Console()


def _check_part_implemented(module, part: int) -> bool:
    """Check if a part is implemented (not just a placeholder)."""
    func_name = f"part{part}"
    if not hasattr(module, func_name):
        return False

    func = getattr(module, func_name)
    source = inspect.getsource(func)

    # Check if the function just returns 0 or has TODO
    if "return 0" in source and "TODO" in source:
        return False

    # Check if it's a trivial implementation
    lines = [line.strip() for line in source.split("\n") if line.strip() and not line.strip().startswith("#")]
    # If function only has docstring and "return 0", it's not implemented
    return not (len(lines) <= 3 and "return 0" in source)


def show_status() -> None:
    """Show completion progress for all days."""
    project_root = Path(__file__).parent.parent.parent.parent
    src_dir = project_root / "src" / "advent_of_code_2025"

    # Find all day files
    day_files = sorted(src_dir.glob("day*.py"))

    if not day_files:
        console.print("[yellow]No solution files found. Run 'aoc new 1' to get started![/yellow]")
        return

    # Create table
    table = Table(title="🎄 Advent of Code 2025 Progress", show_header=True, header_style="bold cyan")
    table.add_column("Day", style="cyan", width=8)
    table.add_column("Part 1", justify="center", width=10)
    table.add_column("Part 2", justify="center", width=10)

    total_stars = 0

    for day_file in day_files:
        # Extract day number
        day_num = int(day_file.stem.replace("day", ""))
        day_padded = f"{day_num:02d}"

        try:
            module = importlib.import_module(f"advent_of_code_2025.day{day_padded}")

            part1_done = _check_part_implemented(module, 1)
            part2_done = _check_part_implemented(module, 2)

            part1_symbol = "⭐" if part1_done else "☆"
            part2_symbol = "⭐" if part2_done else "☆"

            total_stars += (1 if part1_done else 0) + (1 if part2_done else 0)

            table.add_row(f"Day {day_num}", part1_symbol, part2_symbol)
        except Exception as e:
            console.print(f"[red]Error loading day {day_num}: {e}[/red]")
            continue

    console.print()
    console.print(table)
    console.print(f"\n[bold]Progress: {total_stars}/50 ⭐[/bold]")
    console.print()
