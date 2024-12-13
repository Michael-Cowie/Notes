<div align=center>
 <h1> Asynchronous Programming in Python</h1>
</div>

Asynchronous programming in Python allows you to write code that performs non-blocking operations, **meaning one task can pause and allow other tasks to execute in the meantime**. This is particularly useful for I/O-bound and high-latency operations, such as working with databases, network requests and reading/writing files.

The Python `asyncio` library is an easy approach to allow for the execution of asynchronous code. The `async` and `await` keywords were introduced to prevent a heavy amount of callback code structure, often referred to as "callback hell". Instead, using `async` and `await` presents the flow of a program in a sequential manner similar as if those asynchronous operations were blocking.

**Asynchronous code is based around event loops**, like UI frameworks, in this case `asyncio` has its own event loop and the keyword `await` are used to determine current resource allocation. When an `await` is reached, the code execution will stop in that function and **control is given back to the event loop to resume other asynchronous code**, when the `await`'ed function has completed, it will be added back to the event loop queue and resumed when possible.

The `async` keyword wraps the function so that it **now returns a coroutine object**. The `await` keyword can be used to execute the coroutine in a blocking manner, or it can be added as a task to be executed later. `await` **will give control back to the event loop** so other functions can be executed. Under the hood `asyncio` utilizes coroutines for the internal implementation which also relies on generators, primarily the `send` method of generators.

Ideally, you want to utilize asynchronous programming when your program has I/O-bound operations, where we are "waiting" for responses that are out of our control and give us the ability to perform other tasks while waiting. You do not want to use asynchronous code when you need a simple program with little to no I/O-bound performance isssues. 

Mixing `asyncio` with UI frameworks can be a little tricky as `asyncio` will have its own event loop so will other UI frameworks. Let us suppose we are mixing `asyncio` and `tkinter`, running both event loops at the same time is a dubious proposition, but of course, can be done if we mix both to use a single event loop.

It is very important to know that all of the **code execution runs on a single thread**. Asynchronous programming is a form of concurrency not parallelism. 

```Python
if io_bound:
    if io_very_slow:
        print("Use Asyncio")
    else:
        print("Use Threads")
elif cpu_bound:
    print("Multi Processing")
```

The basic definition and simple example would be,

- `async` - is a keyword used to define an asynchronous function
- `await` is used **inside** an `async` function to pause execution until a coroutine or `async` operation completes. This will call `__await__` on the object.

```Python
async def fetch_data():
    await some_network_request()
```

While `async` and `await` are common keywords amongst multiple programming languages for asynchronous programs, Python also has `asyc for`. This is used to iterate over an asynchronous iterator or asynchronous generator.

```Python
import asyncio
import random

async def five_random_numbers():
    for i in range(5):
        await asyncio.sleep(1)
        yield random.random()

async def async_random():
    async for number in five_random_numbers():
        print(number)

asyncio.run(async_random())
```

# Event Loop

The event loop is a mechanism that manages the execution of asynchronous code. The event loop is a central component of the `asyncio` library, which is a built-in library for asynchronous programming in Python. The event loop is responsible for scheduling the execution of asynchronous tasks and managing the flow of control between them. It uses a non-blocking I/O model, which means that it can handle multiple tasks concurrently without waiting for any of them to complete.

When an asynchronous function is called, it returns an asynchronous task, which is represented by a special type of object called a `coroutine`. When a coroutine if `await`ed The event loop schedules the coroutine for execution and **continues running other tasks**.

The `await` keyword is used inside an asynchronous function to suspend its execution until an asynchronous operation completes. When an asynchronous function encounters an `await` expression, **it returns control to the event loop, allowing it to schedule other tasks**. Once the awaited operation completes, the event loop resumes the execution of the asynchronous function where it left off.

The `await` keyword is used to pause the execution of an asynchronous function and return control to the event loop. It does this by creating a suspension point in the function, where the function's execution can be resumed later on. This is done using a Python generator.

When an asynchronous function encounters an `await` expression, it creates a special object called a "future" that represents the result of the awaited operation. The function then returns control to the event loop, which schedules the future to be executed by a separate execution context, such as a thread or a process. For example, `await asyncio.sleep(2)` will be run in a seperate process, outside of `python.exe` as it will make system calls to the OS (Of course, the python GIL is freed used at this time).

![](../images/event_loop.png)

The event loop continues running other tasks while the future is being executed. When the future completes, it signals the event loop that the result is available. The event loop then resumes the execution of the asynchronous function where it left off, passing the result of the future to the `await` expression, back to the coroutine using the `send()` method from Python generators.

Another visualization of the Event Loop could be the following code snippet,


```Python
import asyncio

async def task_one():
    print("Task 1: Start")
    await asyncio.sleep(1)
    print("Task 1: Resumed after 1 second")
    await asyncio.sleep(1)
    print("Task 1: Done")

async def task_two():
    print("Task 2: Start")
    await asyncio.sleep(2)
    print("Task 2: Resumed after 2 seconds")
    print("Task 2: Done")

async def task_three():
    print("Task 3: Start")
    await asyncio.sleep(0.5)
    print("Task 3: Resumed after 0.5 seconds")
    await asyncio.sleep(0.5)
    print("Task 3: Done")

async def main():
    await asyncio.gather(task_one(), task_two(), task_three())

asyncio.run(main())
```

To illustrate the behaviouir with respect to the event loop, it can be illustrated like this,

```txt
Time    | Event
--------|--------------------------------------------------------
0.0s    | Task 1: Start
        | - The event loop starts executing `task_one()`.
        | - Task 1 prints "Task 1: Start" and reaches `await asyncio.sleep(1)`.
        | - The event loop pauses Task 1 and marks it as waiting.

0.0s    | Task 2: Start
        | - The event loop moves to `task_two()` as Task 1 is sleeping.
        | - Task 2 prints "Task 2: Start" and reaches `await asyncio.sleep(2)`.
        | - The event loop pauses Task 2 and marks it as waiting.

0.0s    | Task 3: Start
        | - The event loop moves to `task_three()` as Task 2 is sleeping.
        | - Task 3 prints "Task 3: Start" and reaches `await asyncio.sleep(0.5)`.
        | - The event loop pauses Task 3 and marks it as waiting.

0.5s    | Task 3: Resumed after 0.5 seconds
        | - Task 3's sleep finishes. The event loop resumes Task 3.
        | - Task 3 prints "Task 3: Resumed after 0.5 seconds."
        | - Task 3 encounters another `await asyncio.sleep(0.5)` and pauses again.
        | - The event loop moves to check other tasks.

1.0s    | Task 1: Resumed after 1 second
        | - Task 1's sleep finishes. The event loop resumes Task 1.
        | - Task 1 prints "Task 1: Resumed after 1 second."
        | - Task 1 encounters another `await asyncio.sleep(1)` and pauses again.
        | - The event loop moves to check other tasks.

1.0s    | Task 3: Done
        | - Task 3's second sleep finishes. The event loop resumes Task 3.
        | - Task 3 prints "Task 3: Done" and completes execution.
        | - Task 3 is removed from the event loop's task list.

2.0s    | Task 2: Resumed after 2 seconds
        | - Task 2's sleep finishes. The event loop resumes Task 2.
        | - Task 2 prints "Task 2: Resumed after 2 seconds."
        | - Task 2 prints "Task 2: Done" and completes execution.
        | - Task 2 is removed from the event loop's task list.

3.0s    | Task 1: Done
        | - Task 1's second sleep finishes. The event loop resumes Task 1.
        | - Task 1 prints "Task 1: Done" and completes execution.
        | - Task 1 is removed from the event loop's task list.

3.0s    | Event loop completes
        | - All tasks are finished. The event loop stops execution.
                  
```

It's crucial to understand the event loop as this illustrates how asynchronous code is single threaded and is handled by the event loop. If we were to instead use `time.sleep(...)` instead of `yield asyncio.sleep(...)`, this would block the execution of the entire event loop **as it is a blocking call and does not yield back control to the event loop** to execute other tasks while it's sleeping.

We can illustrate this with the following code snippet,

```Python
import asyncio
import time

async def task_one():
    print("Task 1: Start")
    time.sleep(5)
    print("Task 2: End")

async def task_two():
    print("Task 2: Start")
    await asyncio.sleep(2)
    print("Task 2: Done")


async def main():
    await asyncio.gather(task_one(), task_two())

asyncio.run(main())
```

```
Time    | Event
--------|--------------------------------------------------------
0.0s    | Task 1: Start
        | - The event loop starts executing `task_one()`.
        | - Task 1 prints "Task 1: Start."
        | - Task 1 encounters `time.sleep(5)`, which blocks the event loop.
        | - No other tasks can proceed while `time.sleep(5)` runs.
        
5.0s    | Task 1: End
        | - Task 1 resumes after the blocking `time.sleep(5)`.
        | - Task 1 prints "Task 2: End."
        | - Task 1 completes execution.
        
5.0s    | Task 2: Start
        | - The event loop finally moves to `task_two()`.
        | - Task 2 prints "Task 2: Start."
        | - Task 2 encounters `await asyncio.sleep(2)` and pauses.
        | - The event loop pauses Task 2 and starts waiting.

7.0s    | Task 2: Done
        | - Task 2's `await asyncio.sleep(2)` finishes.
        | - Task 2 resumes and prints "Task 2: Done."
        | - Task 2 completes execution.

7.0s    | Event loop completes
        | - Both tasks are finished. The event loop stops execution.
```

The crucial component in this example to understand is that when `time.sleep(5)` is called in `task_one`, the event loop is blocked entirely for 5 seconds as this `sleep` implementation does not yield control back to the event loop to run other tasks. This prevents `task_two()` or any other tasks from running during this period, defeating the purpose of asynchronous programming.

# System Calls for Non-Blocking I/O

The event loop uses a single thread to schedule the execution of multiple coroutines concurrently and manage the flow between them.

However, the `asyncio` library uses a technique called "asynchronous I/O" to avoid blocking the event loop while waiting for I/O to complete. This is achieved by using non-blocking I/O primitives provided by the operationg system and the Python standard library, such as the `select` and `poll` modules for sockets, and the `threading` and `multiprocessing` modules for running code in seperate threads of processes.

When the `asyncio.sleep` function is called, it schedules the **sleep operation to be executed by the operating system and not by the Python interpreter**. This allows the event loop to continue running and scheduling other tasks while the sleep is in progress. When the sleep operation is complete, then operating system will signal back and signal to the future that is can be continued.

In this way, the `asyncio.sleep` function is able to release the control of the thread while it waits for the sleep operation to complete, which allows for other tasks to be executed. Keep in mind this is still **all executed in a single thread**. By release the control of the thread, I mean `asyncio.sleep` function releases the control of the execution of flow to the event loop, allowing it to schedule other coroutines for the execution, even though all the tasks are running in a single thread.

It is important to note that the non-blocking behaviour is achieved by the usage of the underlying system capabilities, like the `select` or `poll` system calls to wait for I/O events, **which are provided by the operating system and are not specific to the Python interpreter**.

# Common Mistakes

## Not Running Independent Tasks Together

The first common mistake with asynchronous programming is failing to run independent tasks concurrently when given the opportunity.

In this example we `await` each network request, this means we wait for the response before we continue, similar to synchronous blocking code. However, network request two does not depend on the result from the first. Additonally, the third network request does not depend on the result of either the first or second. Therefore it is perfectly fine to continue to run asynchronously, that is we can execute network request one and while it is waiting for the response we can execute other tasks in the meantime by giving control back to the event loop. The current code approach is necessary if the response from further network requests are dependent on earlier requests.

This approach has a significant impact on performance and till takes 3 seconds to perform all three network requests.

```Python
import asyncio

async def network_request():
    await asyncio.sleep(1)


async def mistake_one():
    network_request_one = await network_request()
    network_request_two = await network_request()
    network_request_three = await network_request()

asyncio.run(mistake_one())
```

If we instead used `asyncio.gather` it will allow each coroutine to execute and free up resources when waiting on the network response.

```Python
async def mistake_one():
    network_request_one, network_request_two, network_request_three = (
        await asyncio.gather(network_request(), network_request(), network_request())
    )
```

**This has a significant impact on performance as it reduced execution time from 3 seconds to 1**. This is only possible as they're independent network requests, if the second network request results the first from the first, this is not possible.

## Not Using Resource Freeing Calls

When writing asynchronous code, using `async` and `await` it does not "magically" make it asynchronous when writing anything inside of the function when adding `async`. It is vital to understand and remember the event loop and use functions **that yield back control to the event loop when waiting** on the response.

An example of this is using `time.sleep` instead of `await asyncio.sleep`. It does not matter that `time.sleep` is inside an `async` function, it will not yield back control to the event loop and will therefore not allow other tasks to execute while waiting on the response. An example can be shown like this,

```Python
import asyncio
import time


async def network_request_synchronous():
    time.sleep(1)


async def mistake_one():
    network_request_one, network_request_two, network_request_three = (
        await asyncio.gather(
            network_request_synchronous(),
            network_request_synchronous(),
            network_request_synchronous(),
        )
    )

asyncio.run(mistake_one())
```

The following code takes 3 seconds to execute! This occurs because each `sleep` call is blocking and does not yield back control to the event loop to perform the other `sleep` operations. If we replace this back to our previous implementation, it will correctly execute in 1 second! 

```Python
async def network_request_synchronous():
    await asyncio.sleep(1)
```

Now, keep in mind when using libraries we may not be able to accomplish this as we do not have control over the library source code. For example, if we were to use the library `isort` to run over a specific file we cannot run this asynchronous. We have the function `isort.check_file` and we need this to behave in an asynchronous way. So, let us embed this inside a `async`.

```Python
async def check_file(self, changed_file):
        return isort.check_file(changed_file)
```

Now, we need to pause for a moment and realize why this **will not work**. `isort.check_file` is a **synchronous function** - just wrapping it with `async` does not make it magically asynchronous. What our `async` function `check_file` is doing is just the same without `async` added. **To get any meaningful performance with asynchronous code we need to have a function that yields back control to the event loop, which this does not do**. As `isort.check_file` is a synchronous function, to get any benefits we will be forced to take a different approach such as using threads.

# Asynchronous File Handling

Asynchronous behaviour is specifically designed for IO operations, however file handling is treated slightly differently. Most operating systems don't support asynchronous file operations. That's why asyncio doesn't support them either. For now, the workaround is to use aiofiles that uses threads to handle files. Asynchronous programming is best utilized for IO-bound and high-level structured network code for the performance improvement related to network and web-servers, database connection libraries, distributed task queues, etc...