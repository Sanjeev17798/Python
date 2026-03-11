import os

# Take filename from user
filename = input("Enter filename: ")

# Get current working directory
cwd = input("Input of CWD : ")

def find_file(filename):
    """Search for a file in the current working directory."""
    for f in os.listdir(cwd):
        if f == filename:
            return os.path.join(cwd, f)
    return None

# Find file
file_path = find_file(filename)

if file_path:
    print("File found at:", file_path)

    line_count = 0

    # Open and count non-comment lines
    with open(file_path, "r") as file:
        for line in file:
            stripped = line.strip()

            # Skip empty lines
            if stripped == "":
                continue

            # Skip commented lines that start with "#"
            if stripped.startswith("#"):
                continue

            line_count += 1

    print("Total non-comment lines:", line_count)

else:
    print("File not found in the current directory.")
