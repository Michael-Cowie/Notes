"""
Beginning, small example code to demonstrate and create an easy
to remember reference to issue the SOLID Principles.

1. Single Responsibility
    => Make things (classes, functions, etc.) responsible for fulfilling one type of role.
        => e.g. Refactor code responsibilities into separate classes.
        => I like to think of this as, make the class as cohesive as you can.

2. Open/Closed
    => Be able to add new functionality to existing code easily without modifying existing code.
        e.g. Use abstract classes. These can define what subclasses will require and strengthen Principle 1. by separating code duties.

3. Liskov Substitution
    => Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it.
    =>  if S is a subtype of T, then objects of type T may be replaced with objects of type S (i.e., an object of type T may be 
        substituted with any object of a subtype S) without altering any of the desirable properties of the program (correctness, task performed, etc.)
    => When a class inherits from another class, the program shouldn't break and you shouldn't need to hack anything to use the subclass.
        e.g. Define constructor arguments to keep inheritance flexible.

4. Interface Segregation
     => Make interfaces (parent abstract classes) more specific, rather than generic.
        e.g. Create more interfaces (classes) if needed and/or provide objects to constructors.

5. Dependency Inversion
    => Make classes depend on abstract classes rather than non-abstract classes.
        e.g. Make classes inherit from abstract classes.
    => High-level modules should not import anything from low-level modules. Both should depend on abstractions (e.g., interfaces).
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
            
    
