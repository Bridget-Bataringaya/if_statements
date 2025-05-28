#real world scenario or problems
 #bank accounts: saving account and current account inherit from bank account
 
 
 #deposite, withdraw,display balance, types of accounts
 
 #superclass
class BankAccount:
     def _init_(self, account_number, balance):
        self.account_number= account_number
        self.balance = balance
        
        
     def deposit(self, amount):
         self.balance += amount
         print(f'Deposited {amount}. New balnce: {self.balance}')
        