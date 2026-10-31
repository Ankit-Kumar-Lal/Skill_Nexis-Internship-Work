# Major Project – Employee Data Analysis Using Python

# ==========================================
# EMPLOYEE DATA ANALYSIS PROJECT
# Using Python, Pandas, OOP and File Handling
# ==========================================

import pandas as pd
import os
from pathlib import Path


# Creating Employee Analysis Class
class EmployeeAnalysis:

    def __init__(self, file_name):
        self.file_name = file_name
        self.df = None

        # Creating output directory
        self.output_folder = Path("output")
        self.output_folder.mkdir(exist_ok=True)

    # Function to load employee CSV file
    def load_data(self):

        try:
            self.df = pd.read_csv(self.file_name)

            print("\nEmployee dataset loaded successfully!")

            print("\nFirst 5 Records:")
            print(self.df.head())

            print("\nTotal Employees:", len(self.df))

        except FileNotFoundError:
            print("Error: Employee dataset file not found!")

        except Exception as e:
            print("Error loading dataset:", e)

    # Function to identify salary and department columns
    def get_column(self, possible_names):

        if self.df is None:
            return None

        columns = {
            str(col).strip().lower().replace("_", "").replace(" ", ""): col
            for col in self.df.columns
        }

        for name in possible_names:
            key = name.lower().replace("_", "").replace(" ", "")

            if key in columns:
                return columns[key]

        return None

    # Function to calculate average salary
    def calculate_average_salary(self):

        salary_col = self.get_column([
            "Salary",
            "AnnualSalary",
            "MonthlyIncome"
        ])

        if salary_col is None:
            print("Salary column not found!")
            return

        salary = pd.to_numeric(self.df[salary_col], errors="coerce")

        average_salary = salary.mean()

        print("\n===== AVERAGE SALARY ANALYSIS =====")

        print("Average Employee Salary:", round(average_salary, 2))

    # Function to count employees in each department
    def department_count(self):

        department_col = self.get_column(["Department"])

        if department_col is None:
            print("Department column not found!")
            return

        department_data = self.df[department_col].fillna("Unknown")

        department_summary = department_data.value_counts()

        print("\n===== DEPARTMENT-WISE EMPLOYEE COUNT =====")

        print(department_summary)

        print("\nTotal Departments:", department_data.nunique())

        return department_summary

    # Function to filter employees above salary threshold
    def filter_high_salary(self, threshold):

        salary_col = self.get_column([
            "Salary",
            "AnnualSalary",
            "MonthlyIncome"
        ])

        if salary_col is None:
            print("Salary column not found!")
            return None

        salary = pd.to_numeric(self.df[salary_col], errors="coerce")

        high_salary_employees = self.df[salary > threshold].copy()

        print("\n===== HIGH SALARY EMPLOYEES =====")

        print(high_salary_employees)

        print(
            "\nNumber of employees earning above threshold:",
            len(high_salary_employees)
        )

        return high_salary_employees

    # Function to export high salary employees to CSV
    def export_high_salary(self, employees):

        if employees is None:
            return

        file_path = self.output_folder / "high_salary_employees.csv"

        try:
            employees.to_csv(file_path, index=False)

            print("\nHigh salary employee data exported successfully!")

            print("File Location:", file_path)

        except Exception as e:
            print("Error exporting employee data:", e)

    # Function to export department summary
    def export_department_summary(self):

        department_col = self.get_column(["Department"])

        if department_col is None:
            print("Department column not found!")
            return

        salary_col = self.get_column([
            "Salary",
            "AnnualSalary",
            "MonthlyIncome"
        ])

        data = self.df.copy()
        data[department_col] = data[department_col].fillna("Unknown")

        summary = data.groupby(department_col).size().reset_index(
            name="Employee_Count"
        )

        if salary_col is not None:
            data[salary_col] = pd.to_numeric(
                data[salary_col], errors="coerce"
            )

            average = data.groupby(department_col)[salary_col].mean()

            summary["Average_Salary"] = summary[department_col].map(
                average
            )

        file_path = self.output_folder / "department_summary.csv"

        try:
            summary.to_csv(file_path, index=False)

            print("\nDepartment summary exported successfully!")

            print("File Location:", file_path)

        except Exception as e:
            print("Error exporting department summary:", e)


# ==========================================
# MAIN PROGRAM
# ==========================================

def main():

    print("======================================")
    print("     EMPLOYEE DATA ANALYSIS SYSTEM")
    print("======================================")

    # Create object of EmployeeAnalysis class
    employee = EmployeeAnalysis("employee_dataset.csv")

    # Load employee dataset
    employee.load_data()

    # Stop if dataset could not be loaded
    if employee.df is None:
        return

    # Calculate average salary
    employee.calculate_average_salary()

    # Display department-wise employee count
    employee.department_count()

    # Take salary threshold from user
    print("\n===== SALARY FILTER =====")

    try:
        threshold = float(
            input("Enter salary threshold: ")
        )

        # Filter employees above threshold
        high_salary = employee.filter_high_salary(threshold)

        # Export filtered employee data
        employee.export_high_salary(high_salary)

    except ValueError:
        print("Invalid input! Please enter a numeric salary.")

    # Export department summary
    employee.export_department_summary()

    print("\n======================================")
    print("       PROJECT EXECUTION COMPLETE")
    print("======================================")


# Execute main function
if __name__ == "__main__":
    main()


