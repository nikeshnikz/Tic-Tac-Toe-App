class CreditCard :
    def __init__(self, card_number,card_holder):
        self.card_number = card_number
        self.card_holder = card_holder

    def pay(self,amount):
        last_four = self.card_number[-4:]
        return(
            f"Paid {amount} using Credit card ending in {last_four} owner : {self.card_holder}"
        )

class PayPal :
    def __init__(self,email):
        self.email = email

    def pay(self,amount):
        return f"Paid {amount} via paypal acoount {self.email}"

def process_checkout(payment_method,amount):
    receipt =payment_method.pay(amount)
    print(receipt)

card =CreditCard("1234567890","Nikesh")
paypal = PayPal("nikeshms101@gmail.com")

process_checkout(card,150)
process_checkout(paypal, 45)