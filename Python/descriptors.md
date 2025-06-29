<div align="center">
    <h1> Descriptors </h1>
</div>

Descriptors are a foundational feature of Pythons object model that enable fine-grained control over **how attributes are accessed, modified and deleted**. They are the underlying mechanism behind properties, methods and even classmethod and staticmethod decorators.

Descriptors are best understood as **objects that define any of the methods** `__get__`, `__set__` **or** `__delete__`. When such an object is assigned **to a class variable**, Python automatically routes attribute access through these special methods, thereby enabling customized behaviour for attribute lookup and mutation.

#### How Descriptors Work

To implement a descriptor, a class must define at least one of the following methods,

- `__get__(self, instance, owner)` - Called when the attribute is accessed.

- `__set__(self, instance, value)` - Called when a value is assigned.

- `__delete__(self, instance)` - Called when the attribute is deleted.

Importantly, **descriptors only function when defined as class variables**. Assigning a descriptor to an instance variable disables its special behaviour, because the instance directionary takes precedence.

The following code demonstrates a simple custom descriptor,

```python
from __future__ import annotations

class Descriptor:
    def __init__(self, initial_value):
        self.value = initial_value

    def __get__(self, instance: DescriptorUser, owner: type[DescriptorUser]):
        print("Getting descriptor value:", self.value)
        return self.value

    def __set__(self, instance: DescriptorUser, value):
        print("Setting descriptor value to:", value)
        self.value = value

class DescriptorUser:
    descriptor = Descriptor(100)

example = DescriptorUser()
example.descriptor        # Calls Descriptor.__get__
example.descriptor = 200  # Calls Descriptor.__set__
```

In this example, accessing or assigning to `example.descriptor` does not interact directly with `example`s `__dict__`, but instead invokes methods on the `Descriptor` instance stored on the class.

#### Instance Specific Behaviour

A common source of confusion is the fact that **descriptors must be defined on the class**, yet they are capable of handling **instance-specific data**. 

The key lies in how the descriptor is designed. A typical implementation **does not store values in the descriptor itself** as the previous `Descriptor.value` did, which was shared. Instead, it uses **the instances** `__dict__` to store data, often using a unique key.

```python
from __future__ import annotations

class BetterDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance: Example, owner: type(Example)):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance: Example, value):
        instance.__dict__[self.name] = value

class Example:
    descriptor = BetterDescriptor('descriptor')

a = Example()
b = Example()

a.descriptor = 10
b.descriptor = 20

print(a.descriptor)  # 10
print(b.descriptor)  # 20

print(type(a).descriptor)
print(type(b).descriptor)
```

The descriptor `descriptor` stores and retrieves values directly from `a.__dict__` and `b.__dict__`, not from within the descriptor object itself. This pattern ensures **per-instance state**, even though the descriptor lives on the class.

Using a decorator to return a descriptor can create a nice framework.

#### Relationship to `property`

When you use the `@property` decorator in Python, it transforms a **method into a descriptor object and assigns it to the class**, not the instance.

```python
class MyClass:

    @property
    def x(self):
        return 42
```


This is equivalent to,

```python
def x(self):
    return 42

x = property(x)
```

So Python does,

1. Define the method `x(self)`.

2. Pass `x` into `property(x)` → this returns a `property` **object**, which is a **descriptor**.

3. Assign that `property` object to `MyClass.x`.

So now, inside `MyClass`, `x` is **not** a method - it is a `property` object.

```python
>>> type(MyClass.__dict__['x'])
<class 'property'>
```

Now, because `@property` assigns the descriptor as a class variable, all instances will share the same instance.

```python
class MyClass:

    @property
    def x(self):
        return 42

o1 = MyClass()
o2 = MyClass()

print(type(o1).x)
print(type(o2).x)
```

Will all output the same value `<property object at 0x0000020312346200>`.

#### Descriptor Usage With Decorators to Build a Framework

Descriptors can be used in conjunction with decorators to create customized frameworks in Python. The following example alllows for the creation of descriptors with the same name as method name. Custom behaviour can be added into `__set__` such as the creation of an event driven framework, when we need to be aware of a variable changing.

```python
class Descriptor:
    def __init__(self, func):
        self.name = func.__name__

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

def decorator():
    def wrapper(func):
        return Descriptor(func)
    return wrapper

class ExampleUsage:

    @decorator()
    def example_variable(self, _):
        pass
```

The decorator is applied **at class creation time, not when an instance is created**. So, `@decorator()` replaces the method with a `Descriptor` object in the classes namespace, i.e. it becomes **a class variable**.

When Python sees this code inside a class body,

```python
@decorator()
def example_variable(self, _):
    pass
```

It **does not** mean,

```python
self.example_variable = decorator()(self.example_variable)  # ❌ Wrong!
```

Instead, this happens at **class definition time**, not per instance.

```python
def example_variable(self, _):
    pass

example_variable = decorator()(example_variable)  # ✅ happens once for the class
```

and Python inserts this `example_variable` (Now a `Descriptor`) into the class.

```python
ExampleUsage.__dict__['example_variable'] = Descriptor(...)
```

This means `example_variable` is a **class attribute**, **not stored in** `self.__dict__`. It's therefore shared across all instances like all descriptors must be.

To create a custom event driven framework that will run the function when changed, it would be modified to the following,

```python
class Descriptor:
    def __init__(self, func):
        self._func = func
        self.name = func.__name__

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        old_value = instance.__dict__.get(self.name, None)

        instance.__dict__[self.name] = value

        if old_value != value:
            self._func()
```