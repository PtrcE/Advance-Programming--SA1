def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot be divide by zero"
    return x / y

def modulus(x, y):
    if y == 0:
        return "Cannot find modulus with zero"
    return x % y

while True:
    #calculator menu
    print("\nCalculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")

    #get user choice
    choice = input("Choose operation (1-5): ")

    #checks if the choice is valid
    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice. Please choose a number from 1 to 5.")
        continue

    #user input to get values
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    #performs the calculation based on user input
    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    elif choice == '5':
        result = modulus(num1, num2)

    print(f"Result: {result}")

    #asks the user if they want to do another calculation
    another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
    if another_calculation != 'yes':
        print("Thank you for using the calculator. Goodbye!")
        break
