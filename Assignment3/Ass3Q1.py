#Write a function that accepts *args to calculate the product of all
#numbers provided. Add error handling to manage non-numeric inputs.


def main(*args):
    prod = 1
    for i in args:
        try:
            prod = prod*int(i)
        except ValueError:
            print("Input formal invalid")   
            return
    print("Product of all numbers is", prod)

main(1, 2, 3, 4, 5,6,7,8,9,) 
    