#Write a robust ATM transaction simulator that includes options for
#checking balances, depositing, withdrawing money, and exiting.
#Handle invalid inputs and edge cases.

class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    


    def deposit(self,amount):
        try:
            if amount>0:
                self.balance+=amount
                print("Amount deposited successfully")
            else:
                raise ValueError
        except ValueError:
            print("Invalid amount")
        except:
            print("Unexpected error")

    def withdraw(self,amount):
        try:
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                print("Amount withdrawn successfully")
            else:
                raise ValueError
        except ValueError:
            print("Insufficient Balance")
        except:
            print("Unexpected error")

    def check_balance(self):
        print("Balance: ", self.balance)

def main():
    balance = 0
    account = BankAccount(balance)
    while True:
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            account.check_balance()
        elif choice == 2:
            amount = int(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == 3:
            amount = int(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 4:
            break
        else:
            print("Invalid choice")

main()