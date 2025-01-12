
#Use pytest to test a module that implements a basic calculator with
#add, subtract, multiply, and divide functions.
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("Enter the operation you want to perform:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = int(input())
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == 1:
        print(f"Addition of {num1} and {num2} is {add(num1, num2)}")
    elif choice == 2:
        print(f"Subtraction of {num1} and {num2} is {subtract(num1, num2)}")
    elif choice == 3:
        print(f"Multiplication of {num1} and {num2} is {multiply(num1, num2)}")
    elif choice == 4:
        try:
            print(f"Division of {num1} and {num2} is {divide(num1, num2)}")
        except ValueError as e:
            print(e)
    else:
        print("Invalid choice")
    

