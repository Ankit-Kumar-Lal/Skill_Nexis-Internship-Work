# Create a JSON File and Read Data From It

import json

student = {
    "name": "Ankit",
    "age": 20,
    "course": "B.Tech CSE",
    "marks": 88.5,
    "subjects": ["Python", "DBMS", "Computer Networks"]
}

# Write data to a JSON file
with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)

print("JSON file created successfully.")

# Read data from the JSON file
try:
    with open("student.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    print("\nStudent Details:")
    print("Name:", data["name"])
    print("Age:", data["age"])
    print("Course:", data["course"])
    print("Marks:", data["marks"])
    print("Subjects:", ", ".join(data["subjects"]))

except FileNotFoundError:
    print("Error: JSON file not found.")
except json.JSONDecodeError:
    print("Error: Invalid JSON format.")
