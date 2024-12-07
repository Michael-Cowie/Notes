"""
1. Single Responsibility
    => Make things (classes, functions, etc.) responsible for fulfilling one type of role.
        => e.g. Refactor code responsibilities into separate classes.
        => I like to think of this as, make the class as cohesive as you can.
"""


class Order:
    
    items = []
    quantities = []
    prices = []
    status = "open"
    
    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)
        
    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total
    
    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("Paying with debit")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("Paying with credit")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        else:
            raise Exception(f"Unknown payment type: {payment_type}")
        
        
order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("USB Cable", 2, 5)
order.add_item("Mouse", 1, 25)

print(order.total_price())
order.pay("debit", "123456789")

"""
The first of five principles is the Single Responsibility.

We want classes and methods to have a single responsibility, in order words,
high cohesion. This helps to ensure that we can reuse them later on.

In this case the Order class does way too much, adding items and calcuating
the price would make sense for an Order, but handling the payment definitely
should not be part of the order and causes the class to have way too many
responsibilities.

To begin we are going to create a new class called PaymentProcessor
and create two methods pay_credit and pay_debit to remove the "if, else"
chaining.
"""

class Order:
    
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"   
    
    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)
        
    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

class PaymentProcessor:
    
    def pay_debit(self, order, security_code):
        print("Paying with debit")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"
        
    def pay_credit(self, order, security_code):
        print("Paying with credit")
        print(f"Verifying security code: {security_code}")
        order.status = "paid" # Alternatively also create a set_status


# Now we can change the usage of the Order class to become,

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("USB Cable", 2, 5)
order.add_item("Mouse", 1, 25)

print(order.total_price())
processor = PaymentProcessor()
processor.pay_debit(order, "123456789")

# We have successfully increased the cohesion of the Order class and each
# of the two classes now only have one responsibility.