#Create a real-world problem-solving program, such as calculating
#monthly loan payments based on principal, rate of interest, and
#tenure.

def main():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest anually: "))
    tenure = int(input("Enter the tenure in months: "))
    rate=rate/100/12
    monthly_payment = (principal * rate * (1 + rate) ** tenure) / ((1 + rate) ** tenure - 1)
    monthly_payment = format(monthly_payment, '.2f')
    print("You have to pay a monthly amount of: ", monthly_payment)
    return


main()