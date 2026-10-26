# Read a File and Count Total Lines

file_name = "sample.txt"

try:
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
        total_lines = len(lines)

    print("Total number of lines:", total_lines)

except FileNotFoundError:
    print("Error: File not found.")
