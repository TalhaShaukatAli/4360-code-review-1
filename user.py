from message import Message
from exceptions import BankingException, InvalidAccountNumberException, MaximumTransferAmountExceededException, MaximumNumberofTransfersExceededException


message = Message()

class User:
    def __init__(self, name, accounts):
        self.name = name
        self.accounts = accounts
        self.transfer_count = 0

    def show_accounts(self):
        message.print("{:<20}{:<0}".format("Account Number", "Amount"))
        for key, val in self.accounts.items():
            balance = val.check_balance()
            message.print("{:<20}{:<0}".format(key, balance))

    
    def deposit(self, args):
        self.perform_account_action(args, False)

    def withdraw(self, args):
        self.perform_account_action(args, True)


    def perform_account_action(self, args, withdraw):
        try:
            account_number = float(args[0])
            amount = float(args[1])
            account = self.accounts.get(account_number)

            if not account:
                raise InvalidAccountNumberException

            if withdraw:
                account.withdraw(amount)
            else:
                account.deposit(amount)

            return account.check_balance()
        except BankingException as e:
            message.print(e.message())
        except:
            message.print("An error occurred")


    def transfer(self, args):
        from_account_number = float(args[0])
        to_account_number = float(args[1])
        amount = float(args[2])

        if amount > 10_000:
            raise MaximumTransferAmountExceededException          

        account1 = self.accounts[from_account_number]
        account2 = self.accounts[to_account_number]

        if not account1 or not account2:
            raise InvalidAccountNumberException
        
        if self.transfer_count >= 3:
            raise MaximumNumberofTransfersExceededException
        self.transfer_count += 1

        account1.withdraw(amount)
        account2.deposit(amount)