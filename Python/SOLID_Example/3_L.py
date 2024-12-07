"""
3. Liskov Substitution
    => Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it.
    =>  if S is a subtype of T, then objects of type T may be replaced with objects of type S (i.e., an object of type T may be 
        substituted with any object of a subtype S) without altering any of the desirable properties of the program (correctness, task performed, etc.)
    => When a class inherits from another class, the program shouldn't break and you shouldn't need to hack anything to use the subclass.
        e.g. Define constructor arguments to keep inheritance flexible.
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

class PaymentProcessor:
    
    def pay_debit(self, order, security_code):
        print("Paying with debit")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"
        
    def pay_credit(self, order, security_code):
        print("Paying with credit")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

class PaymentProcessor(ABC):
    
    @abstractmethod
    def pay(self, order, security_code):
        pass
    
class DebitPaymentProcessor(PaymentProcessor):
    
    def pay(self, order, security_code):
        print("Paying with debit")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"
        
        
class CreditPaymentProcessor(PaymentProcessor):

    def pay(self, order, security_code):
        print("Paying with credit")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("USB Cable", 2, 5)
order.add_item("Mouse", 1, 25)

print(order.total_price())
processor = DebitPaymentProcessor()
processor.pay(order, "123456789")

"""
First, let us begin by extending the PaymentProcessor by adding
PayPal as an optional payment type, because our boss told us to.
"""

class PaypalPaymentProcessor(PaymentProcessor):

    def pay(self, order, security_code):
        print("Paying with paypal")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"
        
"""
Now, the thing is, Paypal payments do not work with security codes,
instead they will require an email address. Initially, we could keep
the pay method and instead change "security_code" to "email_address"
and then provide an email address when paying, e.g. processor.pay(order, "example@hotmail.com")

The issue is that the parameter is not suppose to be a security code, but an
email address. So, we are abusing the interface type to do something differently
compared to what we are suppose to. This means we are violating Liskov's
substitution principle.

One way to solve this is by removing the "security_code" parameter dependency
and instead construct an __init__ so we can do different things in the 
initializer depending on the type of class we create.
"""

# Firstly, remove security_code and create

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
        
# This means, the usage will now become

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("USB Cable", 2, 5)
order.add_item("Mouse", 1, 25)

print(order.total_price())
processor = PaypalPaymentProcessor("example@hotmail.com")
processor.pay(order)

"""
Now, we are properly using the pay method instead of changing what parameters
mean in order to fit our specific use case.


                        PaymentProcessor ------------ T
                        /       |      \
                       /        |       \
                      /         |        \
                   Debit      Credit      PayPal ---- S
                   
Liskov Substitution Principle states that within our example, "S is a subtype 
of T, then objects of type T may be replaced with objects of type S". 

Another way to think about this is to have the original line,
processor.pay(order, "123456789") and think, this method call adheres to the 
interface, and I am passing the security_code as stated by the PaymentProcessor 
interface. Now, would this line of code work with all subclasses of T? 

DebitPaymentProcessor? Yes
CreditPaymentProcessor? Yes
PaypalPaymentProcessor? NO!       BUG PRONE!

Now the developer needs to actively think of the type being passed through
and think "Do I need to pass a security_code or an email_address?",
this should not be something to think about, any subclass of 
PaymentProcessor (T) should be actively swapped to any of the subtypes (S) and
have no change in behaviour!

This is very important for the scalability of projects, especially if 
generic functions utilized the previous order function, it would become
dangerous or require hacks such as "isinstance(PaypalProcessor)" to be
added to EVERY call of the order function around the entire project if
major class refactoring was undesireable!
"""