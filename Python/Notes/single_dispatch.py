
 # singledispatch
 
`singledispatch` is a decorator aimed at functional programming. This decorator will transform a regular function into a single dispatch generic function. The `singledispatch` determines which registered function to call **based on the first argument type**.

To utilize `singledispatch`, import it from `functools` and decorate a function with `@singledispatch`. From here, use the decorated function by registering the type in the form of `@decorated_function.register(type)`. Below is an example where I turn the function `add` into a `singledispatch` and have three registered types.

```python
from functools import singledispatch  

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
  
  
if __name__ == '__main__':  
    add(1, 2)                     # Calls @add.register(int) because of 1
    add('Python', 'Programming')  # Calls @add.register(str) because of 'Python'
    add([1, 2, 3], [5, 6, 7])     # Calls @add.register(list) because of [1, 2, 3]
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
