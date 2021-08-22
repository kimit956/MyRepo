

asks = ""  # This is empty because the user can type 'quit' at the end to stop the program
while asks != "quit":
    result = 0
    doMore = ""
    num1 = int(input("Enter the first number: "))
    while doMore.lower() != "no":  # This will keep going while the user wants to do more calculations with the result as the first number
        num2 = int(input("Enter the second number: "))  #
        try:  # This is for the first time asking for operation
            operation = input("Would you like to add(+), subtract(-), multiply(*), or divide(/)?: ")
        except ValueError:
            operation.lower()
        if operation == "+" or operation == "add" or operation == "addition":
            result = num1 + num2
            print(str(num1),  "+", str(num2), "=", result)

        elif operation == "-" or operation == "subtract" or operation == "subtraction":
            result = num1 - num2
            print(str(num1),  "-", str(num2), "=", result)

        elif operation == "*" or operation == "multiply" or operation == "multiplication":
            result = num1 * num2
            print(str(num1),  "*", str(num2), "=", result)

        elif operation == "/" or operation == "divide" or operation == "division":
            try:
                result = num1 / num2
            except ZeroDivisionError:
                num2 = int(input("There is a division by 0 error. Please enter a different second number: "))
            print(str(num1),  "/", str(num2), "=", result)

        elif operation == "quit":
            break

        else:  # Makes sure that the user can't enter anything else when choosing the operation
            try:  # This is if the user does repeating operations (calculations)
                operation = input("There was an error with your input. Try something else: ")
            except ValueError:
                operation = operation.lower()

        doMore = input("Would you like to do another calculation (The result will become the first number if yes)? ")
        if doMore == "no" or doMore == "n":
            break
        else:
            num1 = result  # Changes the first number into the result for more calculations

    print("\nAddition:", (num1 + num2), "\tSubtraction:", (num1 - num2), "\tMultiplication:", (num1 * num2), "\tDivision:", (num1 / num2))  # This is all the operations in one

    asks = input("\nType 'quit' if you would like to stop making calculations, otherwise press 'enter': \n")

