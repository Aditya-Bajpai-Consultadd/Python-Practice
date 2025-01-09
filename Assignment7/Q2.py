#Implement a polymorphic function to calculate areas of different
#shapes (e.g., circle, rectangle, triangle) using method overriding


class Shape:
    def __init__(self):
        pass

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
def calculate_area(shape):
    return shape.area() 

circle = Circle(5)
rectangle = Rectangle(5, 10)
triangle = Triangle(5, 10)

print(calculate_area(circle))
print(calculate_area(rectangle))
print(calculate_area(triangle))