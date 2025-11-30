"""Command to run a day's solution."""

import importlib
import time
from collections.abc import Callable
from pathlib import Path

import typer
from rich.console import Console

console = Console()


def run_day(
    day: int = typer.Argument(..., help="Day number (1-25)", min=1, max=25),
    part: int | None = typer.Option(None, "--part", "-p", help="Run only specific part (1 or 2)", min=1, max=2),
    example: bool = typer.Option(False, "--example", "-e", help="Use example input instead of puzzle input"),
) -> None:
    """Run solution for a specific day."""
    day_padded = f"{day:02d}"

    # Import the day's module
    try:
        module = importlib.import_module(f"advent_of_code_2025.day{day_padded}")
    except ModuleNotFoundError as e:
        console.print(f"[red]❌ Day {day} not found. Run 'aoc new {day}' to create it.[/red]")
        raise typer.Exit(1) from e

    # Load input data
    project_root = Path(__file__).parent.parent.parent.parent
    if example:
        input_file = project_root / "inputs" / f"day{day_padded}_example.txt"
    else:
        input_file = project_root / "inputs" / f"day{day_padded}.txt"

    if not input_file.exists():
        console.print(f"[red]❌ Input file not found: {input_file}[/red]")
        raise typer.Exit(1)

    input_data = input_file.read_text()

    if not input_data.strip():
        console.print("[yellow]⚠️  Warning: Input file is empty[/yellow]")

    # Determine which parts to run
    parts_to_run = [part] if part else [1, 2]

    # Run the solutions
    console.print(f"\n[bold cyan]🎄 Day {day}[/bold cyan]" + (" [dim](example)[/dim]" if example else ""))

    for part_num in parts_to_run:
        func_name = f"part{part_num}"
        if not hasattr(module, func_name):
            console.print(f"[yellow]⚠️  Part {part_num} not implemented[/yellow]")
            continue

        func: Callable = getattr(module, func_name)

        try:
            start_time = time.perf_counter()
            result = func(input_data)
            elapsed = time.perf_counter() - start_time

            console.print(f"[green]   Part {part_num}: [bold]{result}[/bold] ⭐[/green] [dim]({elapsed:.4f}s)[/dim]")
        except Exception as e:
            console.print(f"[red]   Part {part_num}: ❌ Error: {e}[/red]")

    console.print()
