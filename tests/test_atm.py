from atm.atm import ATM
from atm.card import CreditCard

def test_display_balance():
    card = CreditCard(balance=1000)
    atm = ATM(has_cash=5000)
    assert atm.display_balance(card) == 1000

def test_withdraw_success():
    card = CreditCard(balance=1000)
    atm = ATM(has_cash=5000)
    result = atm.withdraw(card, 500)
    assert result is True
    assert card.get_balance() == 500
    assert atm.has_cash == 4500

def test_withdraw_fail_over_atm_cash():
    card = CreditCard(balance=1000)
    atm = ATM(has_cash=400)
    result = atm.withdraw(card, 500)
    assert result is False
    assert card.get_balance() == 1000
    assert atm.has_cash == 400

def test_withdraw_fail_over_card_balance():
    card = CreditCard(balance=300)
    atm = ATM(has_cash=5000)
    result = atm.withdraw(card, 500)
    assert result is False
    assert card.get_balance() == 300
    assert atm.has_cash == 5000

def test_deposit_success():
    card = CreditCard(balance=1000)
    atm = ATM(has_cash=5000)
    result = atm.deposit(card, 500)
    assert result is True
    assert card.get_balance() == 1500
    assert atm.has_cash == 5500

def test_deposit_fail_invalid_amount():
    card = CreditCard(balance=1000)
    atm = ATM(has_cash=5000)
    result = atm.deposit(card, 125)
    assert result is False
    assert card.get_balance() == 1000
    assert atm.has_cash == 5000
