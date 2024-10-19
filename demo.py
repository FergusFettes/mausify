from mausify.main import create_system_function


def main():
    print("Command Line System Function Runner Demo")
    print("----------------------------------------")

    # Example 1: List available options for a command
    print("\n1. Listing available options for 'ls' command:")
    ls_func = create_system_function('ls')
    print("Available options for 'ls':")
    for opt, desc in ls_func.options.items():
        print(f"  {opt}: {desc}")

    # Example 2: Run a command with options
    print("\n2. Running 'ls' with options:")
    result = ls_func('-l', '-a', '/home')
    print(f"Result of 'ls -l -a /home':\n{result}")

    # Example 3: Pipe input to a command
    print("\n3. Piping input to 'grep' command:")
    grep_func = create_system_function('grep')
    result = grep_func('World', pipe="Hello, World!")
    print(f"Result of piping 'Hello, World!' to 'grep World':\n{result}")

    # Example 4: Using options with values
    print("\n4. Using 'grep' with options and values:")
    result = grep_func('pattern', i=True, C=2, pipe="Line 1\nPattern\nLine 3\nPATTERN\nLine 5")
    print(f"Result of 'grep -i -C 2 pattern' with piped input:\n{result}")


if __name__ == "__main__":
    main()
