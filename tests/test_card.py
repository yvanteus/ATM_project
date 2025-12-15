from atm.card import CreditCard

def test_withdraw_success():
    card = CreditCard(balance=1000)
    assert card.withdraw(500) is True
    assert card.get_balance() == 500
    
def test_withdraw_fail_negative():
    card = CreditCard(balance=1000)
    assert card.withdraw(-100) is False
    assert card.get_balance() == 1000

def test_withdraw_fail_over_balance():
    card = CreditCard(balance=1000)
    assert card.withdraw(2000) is False
    assert card.get_balance() == 1000

def test_deposit_success():
    card = CreditCard(balance=1000)
    assert card.deposit(500) is True
    assert card.get_balance() == 1500

def test_deposit_fail_invalid_amount():
    card = CreditCard(balance=1000)
    assert card.deposit(150) is False
    assert card.get_balance() == 1000