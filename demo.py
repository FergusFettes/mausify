import typer
from typing import Optional

app = typer.Typer()


@app.command()
def run_demos(verbose: Optional[bool] = typer.Option(False, "--verbose", "-v", help="Show verbose output")):
    """Run a series of demos to showcase the command-line system function runner."""
    
    demos = [
        ("List files in the current directory", "python main.py ls -o l"),
        ("Search for a pattern in a file", "echo 'Hello, World!' | python main.py grep World"),
        ("Count lines in a file", "python main.py wc -o l main.py"),
        ("Show available options for a command", "python main.py ls --print-args"),
        ("Use multiple options", "python main.py ls -o l -o a -o h /"),
        ("Pipe input to a command", "python main.py sort -p 'banana\\napple\\ncherry'"),
    ]

    for i, (description, command) in enumerate(demos, 1):
        typer.echo(f"\nDemo {i}: {description}")
        typer.echo(f"Command: {command}")
        if verbose:
            typer.echo("Running command...")
        result = subprocess.run(command, shell=True, capture_output=True, text=True).stdout
        if verbose:
            typer.echo("Command output:")
        typer.echo(result)
        typer.echo("-" * 40)


if __name__ == "__main__":
    app()
