num1 = int(input("Enter a number:\t")) # enter first number
num2 = int(input("Enter another number:\t")) # enter second number
operator = input("Enter an operator (+, -, *, /):\t" ) # enter an operator

# decision making to perform the operation
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("\nError: Cannot divide by 0!\n")
else:
    print("Please enter valid numbers and/or operators")

print(num1, operator, num2, "=", result) # output the result
