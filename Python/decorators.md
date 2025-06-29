<div align="center">
    <h1> Decorators </h1>
</div>

Decorators are a powerful and expressive feature that allow developers to modify or extend the behaviour of functions and methods without changing their underlying code. They are often described as *syntactic sugar*, providing a clean and elegant syntax for what is essentially function wrapping. 

#### Motiviation and Background

Decorators are traditionally used to **add additional behaviour** to function calls. In many scenarios, there is a need to perform tasks such as logging, access control, caching or timing without cluttering the core logic of a function. Rather than duplicating code or introducing boilerplate logic around each function call, decorators provide a reusable and modular approach.

Suppose we want to measure the runtime of a function. One simple way to do this is to pass a function as an argument to another function.

```python
import time

def timer(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print("Total function runtime:", end_time - start_time)

def my_slow_function():
    time.sleep(3)  # Simulates a delay of 3 seconds

timer(my_slow_function)
```

Here, the `timer` function accepts another function as an argument, executes it and prints the time it took to run. While functional, this approach is somewhat cumbersome, especially when we want to apply the timing logic to many functions throughout the codebase.

#### How Decorators Work

Python provides a concise syntax for applying such wrapping behaviour to functions using the `@decorator` notation.

The following code,

```python
@decorator
def my_function(...):
    ...
```

Is functionally equivalent to,

```python
my_function = decorator(my_function)
```

This transformation makes it clear that a decorator is simply a function that takes another function as input and returns a new function, typically with added behaviour.

To apply this concept to the previous timing example, we can rewrite the `timer` function as a proper decorator.

```python
import time

def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("Total function runtime:", end_time - start_time)
    return wrapper
```

With this new defintion, we can apply the decorator to a function using the `@timer` syntax.

```python
@timer
def my_slow_function():
    time.sleep(3)
```

Now, calling `my_slow_function()` will automatically invoke the `wrapper` defined inside the decorator, timing its executin without requiring any additional code from the function caller. This decorator-based approach is cleaner, more modular and scales more effectively accross larger codebases.

#### Preserving Function Metadata

When writing decorators, the inner wrapper function **replaces the original function**, which can lead to the loss of important metadata such as the function names, docstring and annotations. Pythons `functool.wraps` solves this problem.

```python
@timer
def my_slow_function():
    time.sleep(3)

print(my_slow_function)
```

Due to the decorator behaviour of `my_slow_function = timer(my_slow_function)`, we will now be pointing to the function `wrapper` and hence printing `my_slow_function` will output,

```
<function timer.<locals>.wrapper at 0x000001E8FC123100>
```

Hence, we will use `functools.wraps` to resolve this.

```python
from functools import wraps
import time

def timer(func):
    @wraps(func)
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("Total function runtime:", end_time - start_time)
    return wrapper
```

Now, printing `my_slow_function` will correctly give us,

```
<function my_slow_function at 0x00000190E07C3100>
```