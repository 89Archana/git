from abc import ABC, abstractmethod
class Bank(ABC):
    acc_no=0
    name=" "
    phone=""
    type=" "
    balance=0
    def create_account(self):
        self.acc_no=int(input("Enter the account no: "))
        self.name=input("Enter Account Holder Name: ")
        self.acc_no = int(input("Enter the account no: "))
        self.type=input("Enter Account type[S/C]: ")
        self.balance=int(input("Enter initial amount >=500 for Savings Account and >=1000 for Current Account:  "))
        print("\nAccount Created Successfully.")
    def deposit_amount(self,amount):
        self.balance=self.balance+amount
        print(amount, "Deposited Successfully.")
        print("Total Amount is: ", self.balance)
    def withdraw(self,bal):
        if bal<=self.balance:
            self.balance = self.balance - bal
            print("Withdraw successfully:",+bal)
            print("Available balance is:", self.balance)
        else:
            print("Insufficient balance to withdraw.")
    def transfer(self,amount):
        if amount <= self.balance:
            self.balance = self.balance -amount
            self.acc_no = int(input("Enter the account no: "))
            self.name = input("Enter Account Holder Name: ")
            self.phone = int(input("Enter Phone no: "))
            self.balance=int(input("Enter the amount to transfer: "))
            print(amount,"Transaction Completed Successfully.")
        else:
            print("Insufficient Amount to make a Transaction.")
    def close(self):
        self.acc_no= int(input("Enter the account no: "))
        self.name = input("Enter Account Holder Name: ")
        self.phone = int(input("Enter Phone no: "))
        print("Account closed successfully.")
class customer(Bank):
    def create_account(self):
        self.acc_no=int(input("Enter the account no: "))
        self.name=input("Enter Account Holder Name: ")
        self.acc_no = int(input("Enter the account no: "))
        self.type=input("Enter Account type[S/C]: ")
        self.balance=int(input("Enter initial amount >=500 for Savings Account and >=1000 for Current Account:  "))
        print("\nAccount Created Successfully.")
    def deposit_amount(self,amount):
        customer.balance=customer.balance+amount
        print(amount, "Deposited Successfully.")
        print("Total Amount is: ", customer.balance)
    def withdraw(self,bal):
        if bal <= customer.balance:
            customer.balance = customer.balance - bal
            print("Withdraw successfully:",+bal)
            print("Available balance is:", self.balance)
        else:
            print("Insufficient balance to withdraw.")
    def transfer(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            self.acc_no = int(input("Enter the account no: "))
            self.name = input("Enter Account Holder Name: ")
            self.phone = int(input("Enter Phone no: "))
            print(amount, "Transaction Completed Successfully.")
        else:
            print("Insufficient Amount to make a Transaction.")
    def close(self):
        self.acc_no= int(input("Enter the account no: "))
        self.name = input("Enter Account Holder Name: ")
        self.phone = int(input("Enter Phone no: "))
        print("Account closed successfully.")
customer1=customer()
customer2=customer()
customer1.deposit_amount(500)
customer1.withdraw(100)
customer2.transfer(1000)
customer2.close()
