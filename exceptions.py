class BankingException(Exception):
    pass

class InsufficientFundsException(BankingException):
    def message(self):
        return 'An error occurred: Insufficent Funds'

class InvalidAccountNumberException(BankingException):
    def message(self):
        return "An error occurred: Invalid Account Number"
    
class MaximumTransferAmountExceededException(BankingException):
    def message(self):
        return "An error occurred: Transfer Amount Exceeded. Limited to 10,000."
    
class MaximumNumberofTransfersExceededException(BankingException):
    def message(self):
        return "An error occurred: Max Number of Transfers Exceeded. Limited to 3 per session."