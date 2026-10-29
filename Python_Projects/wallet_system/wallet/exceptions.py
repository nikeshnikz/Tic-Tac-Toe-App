# wallet/exceptions.py
class WalletError(Exception):
  """Base exception for wallet system errors."""

  pass


class InsufficientFundsError(WalletError):
  """Raised when a withdrawal or payment exceeds current balance."""

  pass


class InvalidAmountError(WalletError):
  """Raised when an entered transaction amount is zero or negative."""

  pass