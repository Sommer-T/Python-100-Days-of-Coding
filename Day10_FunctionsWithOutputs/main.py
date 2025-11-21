# Day 10 - Calculator Program

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return "Error: Cannot divide by zero."
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print("Welcome to the Calculator!")

    num1 = float(input("What's the first number?: "))

    should_continue = True

    while should_continue:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calculation_function = operations.get(operation_symbol)

        if calculation_function:
            result = calculation_function(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {result}")
        else:
            print("Invalid operation.")
            continue

        choice = input("Type 'y' to continue calculating with the result, or 'n' to start over: ")

        if choice.lower() == "y":
            num1 = result
        else:
            should_continue = False
            calculator()  # restart the calculator


calculator()