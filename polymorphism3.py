class Payment :
    def pay(self,amount):
        raise NotImplementedError("Subcalss must impliment pay()")

class CreditCard(Payment) :
    def __init__(self,card_number,card_holder):
        self.card_number = card_number
        self.card_holder = card_holder

    def pay(self,amount):
        last_four = self.card_number[-4:]
        return f"Paid {amount} of the credit card ending {last_four} , owner is : {self.card_holder}"


class PayPal(Payment) :
    def __init__(self,mail):
        self.mail = mail

    def pay(self,amount):
        return f"Paid {amount} Via paypal account {self.mail}"


class GooglePay(Payment) : 
    def __init__(self,upi_id):
        self.upi_id = upi_id

    def pay(self,amount):
        return f"Paid {amount} Via Google Pay Id : {self.upi_id}"

class ApplePay(Payment) :
    def __init__(self,apple_id):
        self.apple_id = apple_id

    def pay(self,amount):
        return f"Paid {amount} Via Apple Pay Id : {self.apple_id}"

def process_checkout(payment_method,amount):
    reciept = payment_method.pay(amount)
    print(reciept)

card = CreditCard("98765432109", "Nikesh")
paypal = PayPal("nikeshms101@gmail.com")
googlepay = GooglePay("Ni98765")

# process_checkout(card,150)

# process_checkout(paypal,45)

process_checkout(googlepay,100)

applepay = ApplePay("Aplle456")

process_checkout(applepay,800)