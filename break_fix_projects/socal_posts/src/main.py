import subprocess
import sys
import os


def run_command(cmd: list[str], description: str) -> None:
    """
    Runs a shell command and prints output. Exits on failure.

    Args:
        cmd (list[str]): Command and arguments to run.
        description (str): Description shown in the log.
    """
    print(f"\n=== Running: {description} ===")
    try:
        result = subprocess.run(cmd,
                                check=True,
                                text=True,
                                capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error during: {description}\n{e.stderr}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    """
    Main runner script to execute Python and Go scripts in order.
    """
    # Step 1: Run import_data.py
    run_command([sys.executable, "import_data.py"], "Import Data")

    # Step 2: Run database_setup.py
    run_command([sys.executable, "database_setup.py"], "Setup Database")

    # Step 3: Build and run Go script
    go_build_cmd = ["go", "build", "-o", "main", "main.go"]
    run_command(go_build_cmd, "Go Build main.go")

    go_run_cmd = ["./main"] if os.name != "nt" else ["main.exe"]
    run_command(go_run_cmd, "Run Go Program")

    # Step 4: Run data_agg.py
    run_command([sys.executable, "agg_data.py"], "Aggregate Data")

    print("\n All scripts ran successfully!")


if __name__ == "__main__":
    main()
