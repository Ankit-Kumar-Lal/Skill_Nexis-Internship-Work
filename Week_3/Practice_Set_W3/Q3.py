# Use Pandas to Load and Analyze a CSV File

import pandas as pd

try:
    # Load the CSV file
    data = pd.read_csv("students.csv")

    print("First five rows:")
    print(data.head())

    print("\nDataset Information:")
    print(data.info())

    print("\nStatistical Summary:")
    print(data.describe())

    if "Marks" in data.columns:
        print("\nAverage Marks:", data["Marks"].mean())

except FileNotFoundError:
    print("Error: CSV file not found.")
except pd.errors.EmptyDataError:
    print("Error: The CSV file is empty.")
