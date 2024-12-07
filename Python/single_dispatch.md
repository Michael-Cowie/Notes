<div align="center">
  <h1>  singledispatch </h1>
</div>
 
`singledispatch` is a decorator aimed at functional programming. This decorator will transform a regular function into a single dispatch generic function. The `singledispatch` determines which registered function to call **based on the first argument type**.

To utilize `singledispatch`, import it from `functools` and decorate a function with `@singledispatch`. From here, use the decorated function by registering the type in the form of `@decorated_function.register(type)`. Below is an example where I turn the function `add` into a `singledispatch` and have three registered types.

```python
from functools import singledispatch


class Adder:

    def __init__(self, value):
        self.value = value

    def __add__(self, other: 'Adder'):
        return self.value + other.value


@singledispatch
def add(a, b):
    raise NotImplementedError('Unsupported type')


@add.register(int)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


@add.register(str)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


@add.register(list)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


@add.register(Adder)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


if __name__ == '__main__':
    add(1, 2)                     # Calls @add.register(int) because of 1
    add('Python', 'Programming')  # Calls @add.register(str) because of 'Python'
    add([1, 2, 3], [5, 6, 7])     # Calls @add.register(list) because of [1, 2, 3]
    add(Adder(10), Adder(15))     # Calls @add.register(Adder) because of the Adder instance
```

From the examples above, remember that **the first parameter type determines which function is called**. If I were to change `add('Python', 'Programming')` to `add(1, 'Programming')`, then it would be calling `@add.register(int)` which would result in an error as we cannot concatenate a `int` and a `str`.

When calling `add` with an unregistered type, then we will call the original decorated function, in this case it will raise an exception from `raise NotImplementedError('Unsupported type')`.

# Different Ways to Register a Function

In the examples above I use decorators to register all of my callbacks. This works by inspecting the source code and seeing why,

```python
def register(cls, func=None):  
    """
    generic_func.register(cls, func) -> func  

    Registers a new implementation for the given *cls* on a *generic_func*.  
    """
    nonlocal cache_token  
    if _is_valid_dispatch_type(cls):  
        if func is None:  
            return lambda f: register(cls, f)  <--- When using a decorator, this will be returned
        ...
    ...
```

Remember, when using decorators a function must be used. Therefore, `add.register(list)` must return a function. This is done from `return lambda f: register(cls, f)`. When we decorate our function as,

```python
@add.register(list)  
def _(a, b):  
    print("First argument is of type ", type(a))  
    print(a + b)  
```

The `add.register(list)` will be changed to the lambda function where `f` is our function `_`. From here, it will implicitly call `_ = register(cls, _)`, where `cls` was the previously given `list`. However, this can also be done in a non-decorator approach by calling register directly, e.g.

```python
def add_list(a, b):  
    print("First argument is of type ", type(a))  
    print(a + b)  
  
add.register(list, func=add_list)
```

Will also work. Hence, we have two different approaches to register the function, either a decorator or calling it directly.

It is also possible to decorate a single function multiple times,

```python
@add.register(float)  
@add.register(int)  
def _(a, b):  
    print("First argument is of type ", type(a))  
    print(a + b)  
  
  
if __name__ == '__main__':  
    add(1.0, 2)  # First argument is of type  <class 'float'>  
    add(1, 2.0)  # First argument is of type  <class 'int'>
```

# Registering a Class

When reading single dispatch and a registered function such as,

```python
@singledispatch
def add(a, b):
    raise NotImplementedError('Unsupported type')

@add.register(int)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)

add('5', '5')
add(5, 5)
```

It's important to read it as, *When calling `add`, the callback that will be called is determined by the first parameter
type, otherwise it will call the function decorated with `singledispatch`*. However, during the `register` process, there
is no restriction to be a function, it can be classes too.

```python
import functools


@functools.singledispatch
def create_description_for(animal):
    raise NotImplementedError(f'description not implemented for { animal }')


class RedPanda:
    pass


class Capybara:
    pass


class Dolphin:
    pass


@create_description_for.register(Dolphin)
class SeaAnimal:

    def __init__(self, sea_animal):
        self._sea_animal = sea_animal

    def get_description(self):
        print(f"A useful description of a { self._sea_animal.__class__.__name__ }")


@create_description_for.register(RedPanda)
@create_description_for.register(Capybara)
class LandAnimal:

    def __init__(self, land_animal):
        self._land_animal = land_animal

    def get_description(self):
        print(f"A useful description of a { self._land_animal.__class__.__name__ }")


capybara = Capybara()
capybara_description = create_description_for(capybara)  # Calls LandAnimal(capybara)
capybara_description.get_description()                   # A useful description of a Capybara

dolphin = Dolphin()
dolphin_description = create_description_for(dolphin)    # Calls SeaAnimal(dolphin)
dolphin_description.get_description()                    # A useful description of a Dolphin
```

Using this definition, I will create a way to utilize `register` to return an instance of another Class by the provided
Class type.

```python
@functools.singledispatch
def create_description_for(animal):
    raise NotImplementedError(f'description not implemented for { animal }')
```

creates a decorated function which takes a single parameter `animal`. I will register a class as follows,

```python
@create_description_for.register(Dolphin)
class SeaAnimal:
    ...
```

This means, *When calling `create_description_for` when the first parameter is an instance of `Dolphin`, call the
registered callback. Here, the registered callback will be the Class `SeaAnimal`.*

Remember that calling `@create_description_for.register(Dolphin)` will call,

```python
if func is None:
    return lambda f: register(cls, f)
```

Here, `cls` is `Dolphin` and `f` will be the decorated callback (The Class `SeaAnimal`). The decorated callback in 
this instance is the Class `Dolphin`. This is hooked up inside `register(cls, func=None)` via,

```python
registry[cls] = func
```

Therefore, calling `create_description_for(dolphin)` will know that `dolphin` is an instance of `Dolphin`, meaning, 
the determined callback will be the Class `SeaAnimal`. This means it will be the equivalent of `SeaAnimal(dolphin)`. 