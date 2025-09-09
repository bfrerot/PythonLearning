# EX: a class that provides methods to operate on bank accounts including a method that validates 
# the correctness of the account number recorded in accordance with the IBAN standard


class Bank_Account:
    def __init__(self, iban):
        print('__init__ called')
        self.iban = iban
            
    @staticmethod
    def validate(iban):
        if len(iban) == 20:
            return True
        else:
            return False


account_numbers = ['8' * 20, '7' * 4, '2222'] # "8"*20 is an element, etc

for element in account_numbers:
    if Bank_Account.validate(element): # implicit == True
        print('We can use', element, ' to create a bank account')
    else:
        print('The account number', element, 'is invalid')
# We can use 88888888888888888888  to create a bank account
# The account number 7777 is invalid
# The account number 2222 is invalid