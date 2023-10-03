def main():
    # Get the operator and operands from the user.
    operator = input("Enter the operator ('+', '-', '*', '/'): ")
    operand1 = float(input("Enter the first operand: "))
    operand2 = float(input("Enter the second operand: "))

    # Calculate the result.
    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        result = operand1 / operand2

    # Print the result.
    print("The result is:", result)

if __name__ == "__main__":
    # Call the main function.
    main()  # This line calls the main function.s