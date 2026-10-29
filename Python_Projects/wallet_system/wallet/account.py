# wallet/account.py
from .exceptions import InsufficientFundsError, InvalidAmountError


class Wallet:

  def __init__(self, owner: str, initial_balance: float = 0.0):
    self.owner = owner
    self.__balance = float(initial_balance)

  @property
  def balance(self) -> float:
    return self.__balance

  def deposit(self, amount: float) -> None:
    if amount <= 0:
      raise InvalidAmountError("Deposit amount must be strictly positive.")
    self.__balance += amount

  def withdraw(self, amount: float) -> None:
    if amount <= 0:
      raise InvalidAmountError("Withdrawal amount must be strictly positive.")
    if amount > self.__balance:
      raise InsufficientFundsError(
          f"Cannot withdraw ${amount:.2f}. Available balance: ${self.__balance:.2f}"
      )
    self.__balance -= amount