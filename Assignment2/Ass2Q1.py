#Write a program to classify numbers as prime, composite,
#  or neither (for negative or zero values).
#  Ensure it handles invalid inputs gracefully.

def main():
    numbers  = list(map(int,input("Enter numbers separated by space: ").split(" ")))
    for i in numbers:
        if i<=0:
            print(i," is neither prime nor composite")
        elif i==1:
            print(i," is neither prime nor composite")
        elif i==2:
            print(i," is prime")
        else:
            flag = 0
            for j in range(2,i):
                if i%j==0:
                    flag = 1
                    break
            if flag==0:
                print(i," is prime")
            else:
                print(i," is composite")

main()