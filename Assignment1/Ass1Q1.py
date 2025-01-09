# Write a program to calculate the area and perimeter of different 
# geometric shapes(square, rectangle, parallelogram, triangle, circle)
#  based on user input. The program should include error handling for 
# invalid inputs.

def main():
    print("Whose area and perimeter do you want to calculate?")
    print("1. Square")
    print("2. Rectangle")
    print("3. Parallelogram")
    print("4. Triangle")
    print("5. Circle")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        square()
    elif choice == 2:
        rectangle()
    elif choice == 3:
        parallelogram()
    elif choice == 4:
        triangle()
    elif choice == 5:
        circle()
    elif choice == 6:
        exit()
    else:
        print("Invalid choice")
        main()
def square():
        side = int(input("Enter the side of the square: "))
        area = side * side
        perimeter = 4 * side
        print("Area of the square is: ", area)
        print("Perimeter of the square is: ", perimeter)
        main()
def rectangle():
        length = int(input("Enter the length of the rectangle: "))
        breadth = int(input("Enter the breadth of the rectangle: "))
        area = length * breadth
        perimeter = 2 * (length + breadth)
        print("Area of the rectangle is: ", area)
        print("Perimeter of the rectangle is: ", perimeter)
        main()
def parallelogram():
        base = int(input("Enter the base of the parallelogram: "))
        height = int(input("Enter the height of the parallelogram: "))
        area = base * height
        perimeter = 2 * (base + height)
        print("Area of the parallelogram is: ", area)
        print("Perimeter of the parallelogram is: ", perimeter)
        main()
def triangle():
        base = int(input("Enter the base of the triangle: "))
        height = int(input("Enter the height of the triangle: "))
        side1 = int(input("Enter the first side of the triangle: "))
        side2 = int(input("Enter the second side of the triangle: "))
        area = 0.5 * base * height
        area = format(area, '.2f')
        perimeter = base + side1 + side2
        print("Area of the triangle is: ", area)
        print("Perimeter of the triangle is: ", perimeter)
        main()
def circle():
        radius = int(input("Enter the radius of the circle: "))
        area = 3.14 * radius * radius
        area = format(area, '.2f')
        perimeter = 2 * 3.14 * radius
        print("Area of the circle is: ", area)
        print("Perimeter of the circle is: ", perimeter)
        main()
main()