<div align="center">
  <h1>  async for </h1>
</div>

This tutorial is to explain the behaviour of `async/await` and explain how the following code below works by using the combination of `yield`, `async/await` and `async for`.

```Python
import asyncio


async def get_network_request_async():
    await asyncio.sleep(1)
    return 'a_network_response'


async def my_generator():
    for i in range(3):
        yield i
        r = await get_network_request_async()
        yield r


async def my_coroutine():
    async for value in my_generator():
        print(value)


async def main():
    await my_coroutine()


asyncio.run(main())
```

The `async` keyword is used to indicate that a function is an asynchronous function, also known as a coroutine.

The `get_network_request_async()` function is defined as an asynchronous function, which means it uses the `await` keyword to perform asynchronous operations. In this case, the function uses `await asyncio.sleep(1)` to simulate a network request. This pauses the execution of the function for 1 second, allowing other tasks to run as it yields up a future object to the event loop.

The `my_generator()` function is defined as an **asynchronous generator** function. It uses the `yield` keyword to **produce values** and the `await` keyword to **perform asynchronous operations**. On each iteration of the loop the function uses the `yield` keyword to return the current value of `i` which is then printed. Then, it will execute `r = await get_network_request_async()` and assign the value to `r` which will then be yielded up. Remember that each iteration of the generator will forward it to the next `yield`.

The `my_coroutine()` function is also defined as a coroutine. It starts by using the `async for` loop to iterate over the values produced by the `my_generator()` function. The `async for` loop is **used to iterate over asynchronous iterators such as asynchronous generators**.

The `async for` loop is used to iterate over asynchronous iterators, such as asynchronous generators. It allows you to iterate over the values produced by an asynchronous generator function, one at a time, and it allows other tasks to run while waiting for the next value to be produced. This is important in asynchronous programming because it allows you to write code that runs concurrently, rather than sequentially, which can lead to more efficient use of system resources and can improve performance.

Here, the `yield` keyword is used to produce a value from a generator. In this case, the generator function `my_generator()` uses `yield` to produce value of the loop. The `yield` statement is used to **return a value from the generator and pause execution of the generator function**. The execution of the generator can later be resumed by calling the `next()` function or by using the `async for` loop.

The `my_generator()` function also uses the `await` keyword to wait for the result of the `get_network_request_async()` function before yielding back the result. This allows the event loop to run other tasks while waiting for the result. This improves performance and responsiveness of the program by allowing other tasks to run concurrently.

It's important to note that the `async for` loop can only be used with asynchronous iterators, such as asynchronous generators. A normal generator function (defined with `def` and `yield`) cannot be used with the `async for` loop. The `async for` loop is intended for use with **asynchronous iterators**, which allow you to iterate over a sequence of values, one at a time, while also allowing other tasks to run concurrently when we reach an `await` inside the asynchronous generator.