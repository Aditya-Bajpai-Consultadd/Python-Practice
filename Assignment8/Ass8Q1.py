#Write a generator to produce the first 10 Fibonacci numbers.
#Extend it to handle user-specified ranges


def fibonacci_range(start=0, end=10):
    a, b = 0, 1
    while a <= end:
        if a >= start:
            yield a
        a, b = b, a + b


if __name__ == "__main__":
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))
    for i in fibonacci_range(start, end):
        print(i)



