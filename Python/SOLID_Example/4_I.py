"""
4. Interface Segregation
     => Make interfaces (parent abstract classes) more specific, rather than generic.
        e.g. Create more interfaces (classes) if needed and/or provide objects to constructors.
     => i.e Several more specific interfaces rather than a generic interface
"""
from abc import ABC, abstractmethod # ABC = AbstractBaseClass

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

class PaymentProcessor(ABC):
    
    @abstractmethod
    def pay(self, order):
        pass
    
class DebitPaymentProcessor(PaymentProcessor):
    
    def __init__(self, security_code):
        self.security_code = security_code
    
    def pay(self, order):
        print("Paying with debit")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"
        
        
class CreditPaymentProcessor(PaymentProcessor):
    
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Paying with credit")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor):
    
    def __init__(self, email_address):
        self.email_address = email_address

    def pay(self, order):
        print("Paying with paypal")
        print(f"Verifying using email address: {self.email_address}")
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("USB Cable", 2, 5)
order.add_item("Mouse", 1, 25)

print(order.total_price())
processor = PaypalPaymentProcessor("example@hotmail.com")
processor.pay(order)

"""
In this example, let us extend PaymentProcessor to include
two factor authentication and create...
"""

class PaymentProcessor(ABC):
    
    @abstractmethod
    def auth_sms(self, code):
        pass
    
    @abstractmethod
    def pay(self, order):
        pass
    
# Extend the DebitPaymentProcessor

class DebitPaymentProcessor(PaymentProcessor):
    
    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False
        
    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True
    
    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized")
        print("Paying with debit")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"
        
"""
The issue is, the CreditPaymentProcessor. Credit cards do not
require two factor authentication, however we need to include the
method because we inherit from the interface. What could be done?

Well we could add something such as,

def auth_sms(self, code):
    raise Exception("Credit card payments do not support SMS code authorization")
    
However, not only does this fail Liskov's Substitution principle, this is an
issue with a generic interface to do multiple things that are not always
applicable to subclasses. In this case, not all subclasses support two
factor authentication. It is therefore better to create seperate interfaces.
"""

class PaymentProcessor(ABC):
    
    @abstractmethod
    def pay(self, order):
        pass
    
class PaymentProcessor_SMS(PaymentProcessor):
    
    @abstractmethod
    def auth_sms(self, code):
        pass
    
# Now only inherit from PaymentProcessor_SMS if it is supported.

class DebitPaymentProcessor(PaymentProcessor_SMS):
    
    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False
        
    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True
    
    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized")
        print("Paying with debit")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"
        
# Alternatively we could instead use composition instead of inheritence

class SMSAuth:
    
    def __init__(self):
        self._authorized = False
        
    def verify_code(self, code):
        print(f"Verifying code {code}")
        self._authorized = True
        
    def is_authorized(self) -> bool:
        return self._authorized
    
class DebitPaymentProcessor(PaymentProcessor):
    
    def __init__(self, security_code, authorizer: SMSAuth):
        self.authorizer = authorizer
        self.security_code = security_code

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Paying with debit")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

"""        
Either through more specific inheritance or composition, we just need
to make sure that sublcasses do not need to implement methods that they do 
not need/use.

The new usage would therefore become,
"""

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("USB Cable", 2, 5)
order.add_item("Mouse", 1, 25)

print(order.total_price())
authorizer = SMSAuth()
processor = DebitPaymentProcessor("example@hotmail.com", authorizer)
authorizer.verify_code("123456789") # Could be moved to be inside "pay" etc...
processor.pay(order)
