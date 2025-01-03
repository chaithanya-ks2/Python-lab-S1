class Bank:
    name = ""
    type = ""
    acc_no = ""
    balance = 0

    def create_acc(self):
        self.name = input("Name: ")
        self.type = input("Type: ")
        self.acc_no = input("Account No.: ")    

    def deposit(self):
        amount = int(input("Enter the amount to be deposited: "))
        self.balance += amount
        print("Amount deposited successfully!")
    
    def withdraw(self):
        amount = int(input("Enter the amount to be withdrawn: "))
        if (amount <= self.balance):
            self.balance -= amount
            print("Amount withdrawn successfully!")
        else:
            print("No sufficient balance")


user1 = Bank()
user1.create_acc()
print(user1.name)
print(user1.type)
print(user1.acc_no)
print(user1.balance)

user1.deposit()
print(user1.balance)
user1.withdraw()
print(user1.balance)





