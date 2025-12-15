from atm.card import CreditCard

class ATM:
    def __init__(self, has_cash=3000000) -> None:
        self.has_cash = has_cash
        
    
    def display_balance(self, card: CreditCard) -> int:
        return card.get_balance()
    
    
    def withdraw(self, card: CreditCard, amount: int) -> bool:
        if amount > self.has_cash:
            return False
        
        if card.withdraw(amount=amount):
            self.has_cash -= amount
            return True
        return False
    
    
    def deposit(self, card: CreditCard, amount: int) -> bool:
        if card.deposit(amount=amount):
            self.has_cash += amount
            return True
        return False