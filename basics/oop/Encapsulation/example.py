class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
        self._PIN ="sanMariento"
    
    @property
    def balance(self):
        return self.__balance
        
    @balance.setter
    def balance(self, balance):
        if (balance >= 0):
            self.__balance = balance
        else:
            raise ValueError("Balance should be greater than 0")
        
        
account1 = BankAccount(39999)
account1.balance = -99
