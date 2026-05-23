def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "0 diye vag kora jay na"


number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

operation = input("Choose operation (+, -, *, /): ")


if operation == "+":
    print("Result =", add(number1, number2))

elif operation == "-":
    print("Result =", subtract(number1, number2))

elif operation == "*":
    print("Result =", multiply(number1, number2))

elif operation == "/":
    print("Result =", divide(number1, number2))

else:
    print("Invalid operation")