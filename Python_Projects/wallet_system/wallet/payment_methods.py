# wallet/payment_methods.py
from .account import Wallet
from .base import PaymentMethod
from .exceptions import InvalidAmountError


class CreditCard(PaymentMethod):

  def __init__(self, card_number: str, card_holder: str):
    self.card_number = card_number
    self.card_holder = card_holder

  def pay(self, amount: float) -> str:
    if amount <= 0:
      raise InvalidAmountError("Payment amount must be greater than zero.")
    last_four = self.card_number[-4:]
    return f"Paid ${amount:.2f} via Credit Card (ending in {last_four}) for {self.card_holder}"


class WalletPayment(PaymentMethod):

  def __init__(self, wallet: Wallet):
    self.wallet = wallet

  def pay(self, amount: float) -> str:
    # Leverages wallet's internal checks; raises InsufficientFundsError if empty
    self.wallet.withdraw(amount)
    return (
        f"Paid ${amount:.2f} using Wallet. Remaining balance:"
        f" ${self.wallet.balance:.2f}"
    )