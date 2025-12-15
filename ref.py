class CreditCard:
    def __init__(self, balance=2430000):
        self.balance = balance
        
        
    def get_balance(self) -> int:
        return self.balance
    
    
    def withdraw(self, amount: int) -> bool:
        if amount <= 0:
            return False
        
        if self.balance < amount:
            return False
        
        self.balance -= amount
        return True
    
    
    def deposit(self, amount: int) -> bool:
        """пополнение баланса. купюры должны быть кратны 10"""
        if amount <= 0:
            return False
        
        if amount % 10 != 0:
            return False
        
        
        self.balance += amount
        return True
    
    
class ATM:
    def __init__(self, has_cash=378400):
        self.has_cash = has_cash
        
    
    def is_alailable(self, amount: int) -> bool:
        return amount <= self.has_cash
        
    
    def display_balance(self, card: CreditCard) -> int:
        return card.get_balance()
    
    
    def withdraw(self, card: CreditCard, amount: int) -> bool:
        if amount <= 0:
            return False
        
        if amount > self.has_cash:
            return False
        
        if card.withdraw(amount):
            self.has_cash -= amount
            return True
        return False
        
            
    def deposit(self, card: CreditCard, amount: int) -> bool:
        return card.deposit(amount)
       
       
#функции для UI ---------------------------------------------------------------------------  
def check_balance(atm: ATM, card: CreditCard):
    print(f"Текущий баланс: {atm.display_balance(card)}")
    
    
def withdraw(atm: ATM, card: CreditCard):
    print("===Снять денежные средства===")
    print(f"Доступно в банкомате: {atm.has_cash}")
    while True:
        try:
            amount = int(input("Введите необходимую сумму\n"))
            break
        except ValueError:
                    print("Укажите числовое значение")        
            
    if atm.withdraw(card, amount):
        print("\nУспешная операция. Не забудьте забрать деньги")
        print(f"Текущий баланс {atm.display_balance(card)}\n")
    else:
        print("Операция не может быть выполнена")
        
                
def deposit(atm: ATM, card: CreditCard):
    print("===Пополнение счета===")
    while True:
        try:
            amount = int(input("Внесите купюры, кратные 10\n")) #понятно, что в реальном банкомате это лишнее....
            break
        except ValueError:
            print("Операция не может быть выполнена")
                    
    if atm.deposit(card, amount):
        print(f"\nУспешная операция. Новый баланс {atm.display_balance(card)}")
    else:
        print("Операция не может быть выполнена")
        
        
def show_menu():
    print("1 - посмотреть баланс"
              "\n2 - снятие средств"
              "\n3 - пополнить баланс"
              "\n0 - завершить работу")
#-----------------------------------------------------------------------------------------

def main():
    
    card = CreditCard()
    atm = ATM()
    
    print("Добро пожаловать в банк")
    
    while True:
        show_menu()
        
        choice = input()
        
        if choice == "1":
            print("===Текущий баланс===")
            check_balance(atm=atm, card=card)
            
        elif choice == "2":
            withdraw(atm=atm, card=card)
                
        elif choice == "3":
            deposit(atm=atm, card=card)
                
        elif choice == "0":
            print("Не забудьте вашу карту")
            break
            
        
if __name__ == "__main__":
    main()
    