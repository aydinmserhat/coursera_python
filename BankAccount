#pen = 0
#pen2= 0
class BankAccount:
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.balance = initial_balance
       
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.balance = self.balance + amount
        return self.balance
       
        
    def withdraw(self, amount):
        #global pen , pen2
        if self.balance - amount < 0:
            self.balance = self.balance - amount - 5
            #if self == account1:
                #pen += 5
            #elif self == account2:
                #pen2 += 5
        else:
            self.balance = self.balance - amount
           
            
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
       
    def get_balance(self):
        return self.balance
        """Returns the current balance in the account."""
        
    def get_fees(self):
        return 5
        #if self == account1:
            #return pen 
        #elif self == account2 :
            #return pen2
        """Returns the total fees ever deducted from the account."""
      
        
        
