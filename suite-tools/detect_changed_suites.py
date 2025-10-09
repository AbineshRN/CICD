import json
import subprocess
import os

def get_changed_files():
    result = subprocess.run(
        ['git', 'diff', '--name-only', 'HEAD~1', 'HEAD'],
        capture_output=True,
        text=True
    )
    return result.stdout.strip().splitlines()

def main():
    changed_files = get_changed_files()
    suites = []

    for file in changed_files:
        if file.startswith("Test Suites/") and file.endswith(".ts"):
            # remove the .ts extension
            suite_path = os.path.splitext(file)[0]
            suites.append(suite_path)

    # Default to empty list if nothing changed
    print(json.dumps(suites if suites else []))

if __name__ == "__main__":
    main()