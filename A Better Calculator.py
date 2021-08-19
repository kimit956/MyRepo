#Variables for the program should be named according to the data it represents. Comments need to be entered so that
#anyone who looks at the code can figure out what is happening. Error traps need to be used to validate data that is
#entered. Remember to keep the program as simple as possible, and add complexity if desired only after the core program works.

#The calculator will have the fillowing requirements:

#Take numbers from the user and store them as variables (5 points)
#The program should not crash if strings are entered when numbers are expected (10 points)
#The user should have the choice of addition, subtraction, multiplication and devision (5 points)
#The program should not crash if an error happens durring math type selection (10 points)
#The program should not crash from a division by zero error (10 points)
#10 point extra credit:

#The program does all of the above
#The program allows for continous calculations untill the user wants to 'quit'
#The program takes the output from the first calculation, uses that as the input for the first number for the second calculation

playAgain = True
result = 0
while playAgain:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    try:
        operation = input("Enter what you would like to do (addition, subtraction, multiplication, or division): ")
    except ValueError:
        operation = operation.lower()
    if (operation == "+" or operation == "add" or operation == "addition"):
        operation = "+" #This is only for printing use
        result = num1 + num2
    elif (operation == "-" or operation == "subract" or operation == "subtraction"):
        operation = "-" #This is only for printing use
        result = num1 - num2
    elif (operation == "*" or operation == "multiply" or operation == "multiplication"):
        operation = "*" #This is only for printing use
        result = num1 * num2
    elif (operation == "/" or operation == "divide" or operation == "division"):
        operation = "/" #This is only for printing use
        try:
            result = num1 / num2
        except ZeroDivisionError:
            num2 = int(input("There is a division by 0 error. Please enter a different second number: "))
    print(str(num1), operation, str(num2), "=", result)