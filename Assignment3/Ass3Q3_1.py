# Create a class-based module  MathOperations  that encapsulates
# common mathematical functions (like addition, subtraction, matrix
# multiplication). Use this module in a program to perform operations
# based on user input.


    

def matrixCalc(choice):
    print("Enter dimensions of matrix 1")
    r1 = int(input("Enter number of rows: "))
    c1 = int(input("Enter number of columns: "))
    print("Enter elements of matrix 1 : ")
    matrix1 = []
    for i in range(r1):
        matrix1.append(list(map(int, input().split())))
    
    print("Enter dimensions of matrix 2")
    r2 = int(input("Enter number of rows: "))
    c2 = int(input("Enter number of columns: "))
    print("Enter elements of matrix 2 separated by space: ")
    matrix2 = []
    for i in range(r2):
        matrix2.append(list(map(int, input().split())))
        if choice ==1:
            matrixAddition(matrix1, matrix2)
        else:
            matrixSubtraction(matrix1, matrix2)
    
    


def matrixAddition(matrix1, matrix2):
    matrix3 = []
    r1,r2,c1,c2 = len(matrix1), len(matrix2), len(matrix1[0]), len(matrix2[0])
    if r1 == r2 and c1 == c2:
        for i in range(r1):
            matrix3.apend([])
            for j in range(c1):
                matrix3.append(matrix1[i][j] + matrix2[i][j])
        print("Addition of matrices is: ")
        for i in range(r1):
            for j in range(c1):
                print(matrix3[i][j] + " ", end = "")
            print("\n")
    else:
        print("Calculation is not possible")
        return

def matrixSubtraction(matrix1, matrix2):
     matrix3 = []
     r1,r2,c1,c2 = len(matrix1), len(matrix2), len(matrix1[0]), len(matrix2[0])
     if r1 == r2 and c1 == c2:
        for i in range(r1):
            matrix3.apend([])
            for j in range(c1):
                matrix3.append(matrix1[i][j] - matrix2[i][j])
        print("Addition of matrices is: ")
        for i in range(r1):
            for j in range(c1):
                print(matrix3[i][j] + " ", end = "")
            print("\n")
     else:
        print("Calculation is not possible")
        return

def matrixMultiplication():
    print("Enter dimensions of matrix 1")
    r1 = int(input("Enter number of rows: "))
    c1 = int(input("Enter number of columns: "))
    print("Enter elements of matrix 1 : ")
    matrix1 = []
    for i in range(r1):
        matrix1.append(list(map(int, input().split())))
    
    print("Enter dimensions of matrix 2")
    r2 = int(input("Enter number of rows: "))
    c2 = int(input("Enter number of columns: "))
    print("Enter elements of matrix 2 separated by space: ")
    matrix2 = []
    for i in range(r2):
        matrix2.append(list(map(int, input().split())))
    
    if c1 != r2:
        print("Calculation not possible")
        return
    else:
        matrix3 = []
        for i in range(r1):
            matrix3.append([])
            for j in range(c2):
                matrix3[i].append(0)
                for k in range(r2):
                    matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
        print("Multiplication of matrices is: ")
        for i in range(r1):
            for j in range(c2):
                print(matrix3[i][j], end = " ")
            print("\n")
    
    



    