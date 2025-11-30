"""CLI for Advent of Code 2025."""

import typer
from rich.console import Console

from advent_of_code_2025.commands import new, run, status

app = typer.Typer(
    name="aoc",
    help="🎄 Advent of Code 2025 CLI",
    add_completion=False,
    rich_markup_mode="rich",
)

console = Console()

# Register commands
app.command(name="new", help="📝 Scaffold a new day's solution")(new.new_day)
app.command(name="run", help="🚀 Run solution for a specific day")(run.run_day)
app.command(name="status", help="📊 Show completion progress")(status.show_status)


if __name__ == "__main__":
    app()
