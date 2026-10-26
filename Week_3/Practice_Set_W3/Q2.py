# Write a Program to Merge Two Text Files

file1 = "file1.txt"
file2 = "file2.txt"
output_file = "merged.txt"

try:
    with open(file1, "r", encoding="utf-8") as f1:
        content1 = f1.read()

    with open(file2, "r", encoding="utf-8") as f2:
        content2 = f2.read()

    with open(output_file, "w", encoding="utf-8") as output:
        output.write(content1)

        if content1 and not content1.endswith("\n"):
            output.write("\n")

        output.write(content2)

    print("Files merged successfully.")
    print("Merged content saved in", output_file)

except FileNotFoundError as error:
    print("Error: File not found -", error.filename)
