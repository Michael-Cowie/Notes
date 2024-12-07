"""
2. Open/Closed
    => Be able to add new functionality to existing code easily without modifying existing code.
        e.g. Use abstract classes. These can define what subclasses will require and strengthen Principle 1. by separating code duties.
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
        print(self.items)
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
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("USB Cable", 2, 5)
order.add_item("Mouse", 1, 25)

print(order.total_price())
processor = PaymentProcessor()
processor.pay_debit(order, "123456789")

"""
Taking the definition above to our example, we have our Order and PaymentProcessor
class. The issue is, if we want to add an extra payment method such as Paypal
we have to modify the PaymentProcessor class, thus, violating the Open/Closed
principle. Optimally, what we would like to do is create a structure of classes
and subclasses where we can just define a new subclass for each new payment type.

In order to do that we need to refactor the PaymentProcessor class.
First, let us turn it into an AbstractClass and create SubClasses for
each of the different payment types.
"""

from abc import ABC, abstractmethod # ABC = AbstractBaseClass


class PaymentProcessor(ABC):
    
    @abstractmethod
    def pay(self, order, security_code):
        pass
    
# Now, for each payment type, create a subclass
    
class DebitPaymentProcessor(PaymentProcessor):
    
    def pay(self, order, security_code):
        print("Paying with debit")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"
        
        
class CreditPaymentProcessr(PaymentProcessor):

    def pay(self, order, security_code):
        print("Paying with credit")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

# We would use them by creating them and calling the pay method, e.g.

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("USB Cable", 2, 5)
order.add_item("Mouse", 1, 25)

print(order.total_price())
processor = DebitPaymentProcessor()
processor.pay(order, "123456789")

# Now, we no longer violate the O/C principle because whenever we want to add
# a new payment method, we no longer modify the PaymentProcessor class, or
# the Order class, we simply create a new one and only EXTEND