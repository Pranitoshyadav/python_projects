class student:
    def __init__(self):  
        self.__marks = 90

    def show_marks(self):
        print(self.__marks)

s = student()
s.show_marks()



class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("balance : ", self.__balance)

account = BankAccount(1000)

account.deposit(500)
account.show_balance()