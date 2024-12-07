<div align="center">
    <h1> Generators </h1>
</div>

Python generators are a unique feature that allows that allow you to **generate a sequence of values lazily**. This means they produce items one at a time and only as needed, instead of generating all values at once and storing them in memory (like lists or other iterables). Generators are useful for working with large datasets or streams of data where holding everything in memory is impractical.

The key components of generators are,

1. **Lazy Evaluation** - Generators compute values on the fly, reducing memory usage.

2. **Iterator Protocol** - Generators are iterators, meaning they implement `__iter__()` and `__next__()` methods.

3. **Statefulness** - Generators maintain their state between calls, making them ideal for tasks requiring incremental computation.

4. **Yield Statement** - The `yield` keyword is used to produce a value and pause execution of the generator function.

5. **One-Time Iteration** - Generators can only be iterated once. After completion, they're exhausted and cannot be reused.

## Creating Generators

#### Generator Functions

A generator function is a normal function defined with the `def` keyword, but instead of `return`, it uses `yield`. When the function is called, it does not execute immediately. Instead, it **returns a generator object**.

```python
def count_up_to(max_value):
    count = 1
    while count <= max_value:
        yield count
        count += 1

gen = count_up_to(5)
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(list(gen))  # Output: [3, 4, 5]
```

The `yield` statement pauses the function and saves it state. The first call using `next` will start the function execution until it meets a `yield` statement. Here, it will first be `yield 1`. This means `1` is "returned" and the function execution is paused and its state saved. Calling `next` resumes the generator from where it left off.

#### Generator Expressions

Similar to list comprehensions but use parentheses `()` instead of square brackets `[]`. They are concise and efficient for simple cases.

```Python
gen = (x ** 2 for x in range(5))
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(list(gen))  # Output: [4, 9, 16]
```

## How Generators Work Internally

Under the hood, when a generator function is called,

1. **Generator Object** - A generator object is returned. This object implements the iterator protocol.

2. **Execution Suspended** - The functions execution is suspended at the `yield` statement.

3. **State Preservation** - Local variables and execution context are saved.

4. **Execution Resumed** - When `next()` is called, execution resumes from the `yield` statement.

```python
def example():
    yield 1
    yield 2
    yield 3

gen = example()
print(next(gen))  # Start execution, yield 1
print(next(gen))  # Resume execution, yield 2
print(next(gen))  # Resume execution, yield 3
```

## Advantages of Generators

#### Memory Efficiency

Large sequences can be processed without using significant memory.

```python
def large_sequence():
    for i in range(1_000_000):
        yield i

for num in large_sequence():
    print(num)
```

In this example, it only processes the numbers one by one. It will not generate and hold the entire list in memory and then iterate through the list.

#### Pipelining

Generators can be chained together to form a pipeline by passing the generator object,

```python
def read_file(file):
    for line in open(file):
        yield line.strip()

def filter_lines(lines):
    for line in lines:
        if "error" in line:
            yield line

def count_errors(lines):
    return sum(1 for _ in lines)

lines = read_file("log.txt")
error_lines = filter_lines(lines)
print(count_errors(error_lines))
```

In this example, the crucial component to understand is that we first call the function to retrieve the generator object. From there, we pass this generator object to another function which can iterate through it.

#### Infinite sequences

Unlike lists, generators can represent infinite sequences.

```python
def infinite_counter():
    count = 1
    while True:
        yield count
        count += 1

counter = infinite_counter()
for _ in range(5):
    print(next(counter))  # Output: 1, 2, 3, 4, 5
```

## Advanced Features of Generators

#### `send()` - Sending Data to Generators

A generator can accept input using the `send()` method. The data is received by assigning it to a variable where `yield` is used, e.g. `received_data = yield`. This is unaffected if the generator function `yield`ed data. The behaviour is the same if it was instead `received_data = yield "cats"`

```python
def coroutine():
    value = yield
    while True:
        print(f"Received: {value}")
        value = yield

gen = coroutine()
next(gen)     # Priming the generator, alternatively use `gen.send(None)`
gen.send(10)  # Output: Received: 10
gen.send(20)  # Output: Received: 20
```

When we meet any of the lines `value = yield` the following is happening,

1. `None` is `yield`ed back and the function pauses execution.
2. The value that is passed to `send()` is assigned to `value` and the generator continues.

A generator without a `send` method will appear one way,

```
          ==========       yield       ========
          Generator |   ----------->   | User |
          ==========                   ========
          
          
but with send it becomes two way,

          ==========       yield       ========
          Generator |   ----------->   | User |
          ==========    <-----------   ========
                           send 
```

#### `throw()` - Raising Exceptions in Generators

Use the `throw()` method to inject exceptions into a generator.

```python
def generator():
    try:
        yield 1
    except ValueError:
        print("ValueError caught!")
    yield 2

gen = generator()
print(next(gen))              # Output: 1
print(gen.throw(ValueError))  # Output: ValueError caught! and also yields back the 2
```

#### `close()` - Terminating Generators

You can terminate a generator using `close()`. It raises a `GeneratorExit` exception.

```python
def generator():
    try:
        while True:
            yield 1
    except GeneratorExit:
        print("Generator closed!")

gen = generator()
print(next(gen))  # Output: 1
gen.close()       # Output: Generator closed!
```