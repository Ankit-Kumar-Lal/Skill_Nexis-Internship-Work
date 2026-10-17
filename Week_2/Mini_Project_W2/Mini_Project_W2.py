# Student Management System

import csv
import os

file = "students.csv"

# Create CSV file if it does not exist
if not os.path.exists(file):
    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Roll Number", "Name", "Marks"])


def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([roll, name, marks])

    print("Student added successfully!")


def display_students():
    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def search_student():
    roll = input("Enter roll number to search: ")

    with open(file, "r") as f:
        reader = csv.reader(f)
        found = False

        for row in reader:
            if row[0] == roll:
                print("Student found:", row)
                found = True
                break

        if not found:
            print("Student not found.")


def delete_student():
    roll = input("Enter roll number to delete: ")
    students = []

    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != roll:
                students.append(row)

    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(students)

    print("Student record deleted if it existed.")


while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Program ended.")
        break
    else:
        print("Invalid choice. Try again.")
