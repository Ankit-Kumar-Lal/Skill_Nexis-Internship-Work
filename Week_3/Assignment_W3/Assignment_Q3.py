# Calculator Class with Exception Handling

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b


# Main program
calculator = Calculator()

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        result = calculator.add(num1, num2)
    elif choice == "2":
        result = calculator.subtract(num1, num2)
    elif choice == "3":
        result = calculator.multiply(num1, num2)
    elif choice == "4":
        result = calculator.divide(num1, num2)
    else:
        raise ValueError("Invalid operation selected.")

    print("Result:", result)

except ValueError as error:
    print("Input Error:", error)

except ZeroDivisionError as error:
    print("Calculation Error:", error)
