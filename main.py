from atm.card import CreditCard
from atm.atm import ATM
from atm.ui import get_number, show_menu, check_balance, withdraw, deposit

def main():
    
    card = CreditCard()
    atm = ATM()
    
    print("\nДобро пожаловать в 404 банк\n")
    
    while True:
        
        show_menu()
        
        choice = input().strip()
        
        if choice == "1":
            check_balance(atm=atm, card=card)
        elif choice == "2":
            withdraw(atm=atm, card=card)
        elif choice == "3":
            deposit(atm=atm, card=card)
        elif choice == "0":
            print("\nСпасибо, что выбираете 404 банк")
            print("Не забудьте вашу карту")
            break
            
            
if __name__ == "__main__":
    main()