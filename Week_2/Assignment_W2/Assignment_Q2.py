# Word Counter from Text File

file = input("Enter file name: ")

try:
    with open(file, "r") as f:
        text = f.read()

    words = text.split()
    lines = text.splitlines()
    characters = len(text)

    print("Number of words:", len(words))
    print("Number of lines:", len(lines))
    print("Number of characters:", characters)

except FileNotFoundError:
    print("File not found.")
