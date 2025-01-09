#Design a class  BankAccount  with methods for deposit, withdrawal,
#and balance check. Include error handling for invalid transactions.


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
            print("Invalid amount")
        except:
            print("Unexpected error")

    def check_balance(self):
        print("Balance: ", self.balance)

