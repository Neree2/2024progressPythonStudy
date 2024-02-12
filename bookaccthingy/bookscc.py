class BankAccount:
    def __init__(self, balance, account_number):
        self.__balance=balance
        self.__account_number=account_number
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        self.__balance-=amount   
        self.__check(amount) 
    def __check(self,amount):
        if self.__balance<amount:
            print('you cannot')
            
        else:
            print('yea')
    def display(self):
        print('acount num: ',self.__account_number,'balance:', self.__balance)

ban=BankAccount(200,123)
ban.deposit(100)
ban.withdraw(500)
ban.display()