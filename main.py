import time

# Functions for operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Fancy header
def print_welcome():
    print("\033[95m" + "="*40)
    print("       WELCOME TO PY-CALC 3000")
    print("="*40 + "\033[0m")
    time.sleep(0.5)

# Calculator logic
def calculator():
    print_welcome()
    while True:
        print("\033[94mSelect operation:\033[0m")
        print("  1. ➕ Add")
        print("  2. ➖ Subtract")
        print("  3. ✖ Multiply")
        print("  4. ➗ Divide")
        print("  5. ❌ Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == '5':
            print("\n\033[92mThank you for using Py-Calc 3000. Goodbye!\033[0m")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("\033[91mInvalid input! Please enter numeric values.\033[0m\n")
                continue

            if choice == '1':
                result = add(num1, num2)
                op = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                op = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                op = "*"
            elif choice == '4':
                result = divide(num1, num2)
                op = "/"

            print(f"\033[93m\nResult: {num1} {op} {num2} = {result}\033[0m\n")
        else:
            print("\033[91mInvalid input! Please select a valid option (1-5).\033[0m\n")

# Run the calculator
calculator()
