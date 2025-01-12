#Create a list comprehension to generate a list of squares for even
#numbers from 1 to 50

list = [x**2 for x in range(1, 51) if x % 2 == 0]
print(list)