import Ass3Q3_1 as p1;


def main():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        p1.matrixCalc(choice)
    elif(choice == 2):
        p1.matrixCalc(choice)
    elif(choice == 3):
        p1.matrixMultiplication()
    else:
        print("Invalid choice")