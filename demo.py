Here's a demo script that showcases some features of the package. You can pipe this directly into demo.py:

```python
#!/usr/bin/env python3

import typer

app = typer.Typer()

@app.command()
def main():
    typer.echo("Welcome to the demo of our system command runner!")

    # Example 1: Simple command
    typer.echo("\nExample 1: Running a simple 'ls' command")
    typer.echo("python demo.py run-command ls")
    
    # Example 2: Command with arguments
    typer.echo("\nExample 2: Running 'ls' with arguments")
    typer.echo("python demo.py run-command ls -o l -o a /etc")
    
    # Example 3: Using pipe
    typer.echo("\nExample 3: Using pipe with 'grep'")
    typer.echo("echo 'Hello, World!' | python demo.py run-command grep Hello")
    
    # Example 4: Complex command (find)
    typer.echo("\nExample 4: Complex command (find)")
    typer.echo("python demo.py run-command find /etc -o name='*.conf' -o type=f")
    
    # Example 5: Printing available options
    typer.echo("\nExample 5: Printing available options for a command")
    typer.echo("python demo.py run-command ls --print-args")
    
    # Example 6: Using a different command (ps)
    typer.echo("\nExample 6: Using 'ps' command")
    typer.echo("python demo.py run-command ps -o aux")

    typer.echo("\nTry running these commands to see the results!")

if __name__ == "__main__":
    app()
```

This demo script provides several examples that showcase different features of your system command runner:

1. Running a simple 'ls' command
2. Running 'ls' with arguments and options
3. Using pipe with 'grep'
4. Running a more complex command (find) with multiple options
5. Printing available options for a command
6. Using a different command (ps) with options

To use this demo, you can save it as `demo.py` and run it directly, or you can pipe it into your existing `demo.py` file. The demo will print out the commands that demonstrate the features, which you can then run to see the actual results.
