# Calculator

from calculator_art import logo

print(logo)


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


# Exponent
def exponent(n1, n2):
    return n1 ** n2


# Exit
def exit_calculator():
    return


# A Dictionary with math operations as keys
# and method names as values
# ( method names can be used without parentheses so they aren't called ).
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": exponent,
    "exit": exit_calculator
}


def calculator():
    num1 = float(input("What's your first number?: "))
    for key in operations:
        print(key)

    yes_or_no = ""
    while not yes_or_no == "n":
        operation = input("Pick an operation: ")
        next_num = float(input("What's the next number?: "))
        function_to_run = operations[operation]
        result = function_to_run(num1, next_num)
        print(f"{num1} {operation} {next_num} = {result}")
        # result = function_to_run(result, next_num)
        num1 = result
        yes_or_no = input(
            f"Type 'y' to continue calculating with {result}, type 's' to start a new calculation or type 'n' to exit.: ")
        if yes_or_no == "s":
            calculator()
        elif yes_or_no == "n":
            return


calculator()
