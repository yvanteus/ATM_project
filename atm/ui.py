from atm.atm import ATM
from atm.card import CreditCard

def get_number(prompt) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Введите числовое значение")


def show_menu():
    print("1 - Посмотреть баланс"
          "\n2 - Снять средства"
          "\n3 - Внести наличные"
          "\n0 - Завершить работу")
    
    
def check_balance(atm: ATM, card: CreditCard):
    print(f"\nТекущий баланс {atm.display_balance(card=card)}\n")
    
    
def withdraw(atm: ATM, card: CreditCard):
    print("\n===Снять наличные===")
    print(f"Доступно к снятию {atm.has_cash}")
    amount = get_number("Введите необходимую сумму\n")
    
    if atm.withdraw(card=card, amount=amount):
        print("\nОперация выполнена. Не забудьте забрать деньги\n")
    else:
        print("\nОперация не может быть выполнена\n")
        
        
def deposit(atm: ATM, card: CreditCard):
    print("\n===Внесение наличных===")
    amount = get_number("Внесите купюры, кратные 100\n")
    
    if atm.deposit(card=card, amount=amount):
        print("\nОперация выполнена\n")
    else:
        print("\nОперация не может быть выполнена\n")
        
        