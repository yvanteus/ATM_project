class CreditCard:
    def __init__(self, balance=170000) -> None:
        self.balance = balance
        
    
    def get_balance(self) -> int:
        
        '''Метод возвращает текущий баланс карты'''
        
        return self.balance
    
    
    def withdraw(self, amount: int) -> bool:
        
        '''Метод проверяет условия для снятия денег.
        Осуществена проверка на положительное число
        Неравенство нулю
        Запрашиваемая сумма не должна быть больше баланса карты'''
        
        if amount <= 0:
            return False
        
        if amount > self.balance:
            return False
        
        if amount % 100 != 0:
            return False
        
        self.balance -= amount
        return True
    
    
    def deposit(self, amount: int) -> bool:
        
        '''Метод проверяет условия для внесения наличных
        Проверяется на положительное число
        Не равенство нулю
        Кратность 100'''
        
        if amount <= 0:
            return False
        
        if amount % 100 != 0:
            return False
        
        self.balance += amount
        return True