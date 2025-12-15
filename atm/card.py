class CreditCard:
    def __init__(self, balance=100000) -> None:
        self.balance = balance
        
    
    def get_balance(self) -> int:
        return self.balance
    
    
    def withdraw(self, amount: int) -> bool:
        if amount <= 0:
            return False
        
        if amount > self.balance:
            return False
        
        if amount % 100 != 0:
            return False
        
        self.balance -= amount
        return True
    
    
    def deposit(self, amount: int) -> bool:
        if amount <= 0:
            return False
        
        if amount % 100 != 0:
            return False
        
        self.balance += amount
        return True