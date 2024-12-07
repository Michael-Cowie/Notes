"""
5. Dependency Inversion
    => Make classes depend on abstract classes rather than non-abstract classes.
        e.g. Make classes inherit from abstract classes.
    => High-level modules should not import anything from low-level modules. Both should depend on abstractions (e.g., interfaces).
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

"""
The final principle in SOLID is dependency inversion.

Dependency inversion means we want our classes to depend on abstractions,
rather than concrete subclasses. In this code, this is currently an issue
because the payment processors are depending on a specific authoriser (SMSAuth).
In order to solve this we need to create an abstract authoriser class that
we now pass to the payment processors.
"""
class SMSAuth:
    
    def __init__(self):
        self._authorized = False
        
    def verify_code(self, code):
        print(f"Verifying code {code}")
        self._authorized = True
        
    def is_authorized(self) -> bool:
        return self._authorized


class Authorizer(ABC):
    
    @abstractmethod
    def is_authorized(self) -> bool:
        pas

class SMSAuth(Authorizer):
    
    def __init__(self):
        self._authorized = False
        
    def verify_code(self, code):
        print(f"Verifying code {code}")
        self._authorized = True
        
    def is_authorized(self) -> bool:
        return self._authorized
    
# Now, we can create another Authorizer without any problems or typing issues.
class NotARobot(Authorizer):
    def __init__(self):
        self._authorized = False
        
    def not_a_robot(self):
        print("Are you a robot? -> No!")
        self._authorized = True
        
    def is_authorized(self) -> bool:
        return self._authorized    

class DebitPaymentProcessor(PaymentProcessor):
    
    def __init__(self, security_code, authorizer: Authorizer): # SMSAuth -> Authorizer
        self.authorizer = authorizer
        self.security_code = security_code

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Paying with debit")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("USB Cable", 2, 5)
order.add_item("Mouse", 1, 25)

print(order.total_price())
authorizer = SMSAuth()
processor = DebitPaymentProcessor("example@hotmail.com", authorizer)
authorizer.verify_code("123456789") # Could be moved to be inside "pay" etc...
processor.pay(order)
