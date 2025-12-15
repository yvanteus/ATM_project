from atm.atm import ATM
from atm.card import CreditCard

def get_number(prompt) -> int:
    
    '''Запрашиваем числовой ввод у пользователя'''
    
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Введите числовое значение")


def show_menu() -> None:
    
    '''Показываем главное меню банкомата пользователю'''
    
    print("1 - Посмотреть баланс"
          "\n2 - Снять средства"
          "\n3 - Внести наличные"
          "\n0 - Завершить работу")
    
    
def check_balance(atm: ATM, card: CreditCard) -> None:
    
    '''Функция показывает текущий баланс карты пользователю'''
    
    print(f"\nТекущий баланс {atm.display_balance(card=card)}\n")
    
    
def withdraw(atm: ATM, card: CreditCard) -> None:
    
    '''Функция показывает пункт меню СНЯТЬ НАЛИЧНЫЕ пользователю. 
    Запрашиваем числовой ввод и оповещает: операция выполнена/не выполнена'''
    
    print("\n===Снять наличные===")
    print(f"Доступно к снятию {atm.has_cash}")
    amount = get_number("Введите необходимую сумму\n")
    
    if atm.withdraw(card=card, amount=amount):
        print("\nОперация выполнена. Не забудьте забрать деньги\n")
    else:
        print("\nОперация не может быть выполнена\n")
        
        
def deposit(atm: ATM, card: CreditCard) -> None:
    
    '''Функция показывает пункт меню ВНЕСТИ НАЛИЧНЫЕ пользователю. 
    Запрашиваем числовой ввод и оповещает: операция выполнена/не выполнена'''
    
    print("\n===Внесение наличных===")
    amount = get_number("Внесите купюры, кратные 100\n")
    
    if atm.deposit(card=card, amount=amount):
        print("\nОперация выполнена\n")
    else:
        print("\nОперация не может быть выполнена\n")
        
        