
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum1 = num1 + num2
diff1 = num1 - num2
prod1 = num1 * num2

try:
    divide1 = num1 / num2
except ZeroDivisionError:
    num2 = int(input("Cannot divide by 0. Please enter a different number: "))

divide1 = num1 / num2

print("Sum:", sum1, "\tDifference:", diff1, "\tProduct:", prod1, "\tQuotient:", divide1)