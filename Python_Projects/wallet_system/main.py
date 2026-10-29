# main.py
from wallet import (
    CreditCard,
    InsufficientFundsError,
    InvalidAmountError,
    Wallet,
    WalletPayment,
)


def process_order(payment_method, amount):
  try:
    bill = float(amount)
    receipt = payment_method.pay(bill)
  except (InvalidAmountError, InsufficientFundsError) as err:
    print(f"❌ Payment Failed: {err}")
  except ValueError:
    print("❌ Input Error: Amount must be a valid numeric value.")
  except Exception as err:
    print(f"❌ Unexpected Error: {err}")
  else:
    print(f"✅ Success: {receipt}")
  finally:
    print("--- Transaction cycle finished ---\n")


if __name__ == "__main__":
  # Initialize user wallet and a card
  my_wallet = Wallet(owner="Nikesh", initial_balance=100.0)
  card = CreditCard("4111222233334567", "Nikesh")

  # Test 1: Successful wallet transaction
  process_order(WalletPayment(my_wallet), "40.00")

  # Test 2: Overdraft wallet transaction (handled safely)
  process_order(WalletPayment(my_wallet), "90.00")

  # Test 3: Fallback to credit card
  process_order(card, "90.00")