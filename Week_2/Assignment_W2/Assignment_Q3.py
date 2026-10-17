# JSON File Reader: Load JSON data & print formatted output

import json

file = input("Enter JSON file name: ")

try:
    with open(file, "r") as f:
        data = json.load(f)

    print("JSON Data:")
    print(json.dumps(data, indent=4))

except FileNotFoundError:
    print("File not found.")

except json.JSONDecodeError:
    print("Invalid JSON file.")
