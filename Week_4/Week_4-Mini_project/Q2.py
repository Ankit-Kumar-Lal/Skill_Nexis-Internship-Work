# 2. Simple Calculator Using Functions

# Function for addition
def add(a, b):
    return a + b


# Function for subtraction
def subtract(a, b):
    return a - b


# Function for multiplication
def multiply(a, b):
    return a * b


# Function for division
def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


# Main program
while True:

    print("\n===== SIMPLE CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Calculator closed. Goodbye!")
        break

    if choice in ["1", "2", "3", "4"]:

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)

            elif choice == "2":
                result = subtract(num1, num2)

            elif choice == "3":
                result = multiply(num1, num2)

            elif choice == "4":
                result = divide(num1, num2)

            print("Result:", result)

        except ValueError:
            print("Invalid input! Please enter numeric values.")

    else:
        print("Invalid choice! Please select again.")

