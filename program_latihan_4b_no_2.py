while True:

    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

    except ValueError:
        print("Error: please enter numbers only.")
        continue

    result = num1 + num2
    print("Result:", result)

    break