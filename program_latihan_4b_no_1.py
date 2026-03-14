try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 + num2

    print("The result is:", result)

except ValueError:
    print("Error: please enter numbers only.")