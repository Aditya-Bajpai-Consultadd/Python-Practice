#Write unit tests for a function that determines if a number is prime.
#Add edge case tests for negative numbers and zero.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    n = int(input())
    print(f"Is {n} prime? ",is_prime(n))