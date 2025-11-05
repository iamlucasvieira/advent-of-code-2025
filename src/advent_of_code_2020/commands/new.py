"""Command to scaffold a new day's solution."""

from pathlib import Path

import typer
from rich.console import Console

console = Console()


def new_day(
    day: int = typer.Argument(..., help="Day number (1-25)", min=1, max=25),
    title: str = typer.Option("", help="Optional puzzle title"),
) -> None:
    """Scaffold a new day's solution files."""
    day_padded = f"{day:02d}"

    # Define paths
    project_root = Path(__file__).parent.parent.parent.parent
    solution_file = project_root / "src" / "advent_of_code_2020" / f"day{day_padded}.py"
    test_file = project_root / "tests" / f"test_day{day_padded}.py"
    input_file = project_root / "inputs" / f"day{day_padded}.txt"
    example_file = project_root / "inputs" / f"day{day_padded}_example.txt"

    # Check if files already exist
    if solution_file.exists():
        console.print(f"[yellow]⚠️  Solution file already exists: {solution_file}[/yellow]")
        if not typer.confirm("Overwrite?", default=False):
            raise typer.Abort()

    # Load templates
    template_dir = Path(__file__).parent.parent / "templates"
    solution_template = (template_dir / "solution.py.template").read_text()
    test_template = (template_dir / "test.py.template").read_text()

    # Replace placeholders
    solution_content = solution_template.format(day=day, day_padded=day_padded, title=title)
    test_content = test_template.format(day=day, day_padded=day_padded)

    # Create files
    solution_file.write_text(solution_content)
    console.print(f"[green]✨ Created {solution_file.relative_to(project_root)}[/green]")

    test_file.write_text(test_content)
    console.print(f"[green]✨ Created {test_file.relative_to(project_root)}[/green]")

    # Create empty input files if they don't exist
    if not input_file.exists():
        input_file.write_text("")
        console.print(f"[green]✨ Created {input_file.relative_to(project_root)}[/green]")

    if not example_file.exists():
        example_file.write_text("")
        console.print(f"[green]✨ Created {example_file.relative_to(project_root)}[/green]")

    console.print(f"\n[bold green]🎄 Day {day} ready! Good luck![/bold green]")
    console.print(f"[dim]Edit your solution in {solution_file.relative_to(project_root)}[/dim]")
