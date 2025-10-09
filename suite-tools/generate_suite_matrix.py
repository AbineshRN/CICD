import os
import json

# Define the directory containing test suites
test_suites_dir = os.path.join("Test Suites")

# List to hold suite paths
suite_paths = []

# Walk through the directory and collect .ts files
for root, _, files in os.walk(test_suites_dir):
    for file in files:
        if file.endswith(".ts"):
            # Build the relative suite path and strip .ts extension
            relative_path = os.path.relpath(os.path.join(root, file), ".").replace("\\", "/")
            suite_path = relative_path.replace(".ts", "")
            suite_paths.append(suite_path)

# Output the suite paths as a JSON array
with open("suite_matrix.json", "w") as f:
    json.dump(suite_paths, f, indent=2)

print("suite_matrix.json has been generated with the following test suites:")
print(json.dumps(suite_paths, indent=2))