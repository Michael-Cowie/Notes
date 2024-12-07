"""
Descriptors let objects customize attribute lookup, storage, and deletion.

Descriptors work by implementing custom behaviour using __get__, __set__ and __delete__

Descriptors only work when used as class variables. When put in instances, they have no effect.
"""

class Descriptor:
    
    def __init__(self, initial_value):
        self.value = initial_value
        
    def __get__(self, instance, owner):
        print("Getting descriptor value:", self.value)
        return self.value
        
    def __set__(self, instance, value):
        print("Setting descriptor value to:", value)
        self.value = value
        
class DescriptorUser:
    
    descriptor = Descriptor(100)
        
example = DescriptorUser()
example.descriptor       # Calls Descriptor.__get__
example.descriptor = 200 # Calls Descriptor.__set__

"""
Note: This is actually how the python "property" is implemented.

A reimplementation could be something similar to,
"""

class Property:
    "Emulate PyProperty_Type() in Objects/descrobject.c"

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        ...
        
    def __set__(self, instance, owner):
        ...
        self.fset()

class PropertyDescriptorUser:
    
    property_descriptor = property(lambda *_args: print("Getting"),
                                   lambda *_args: print("Setting"),
                                   lambda *_args: print("Deleting"))
o = PropertyDescriptorUser()
o.property_descriptor       # Calls fget()
o.property_descriptor = 100 # Calls fset()
del o.property_descriptor   # Calls fdel()
