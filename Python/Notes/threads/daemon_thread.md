# Daemon Threads

A daemon thread is a type of thread that runs in the background and **does not prevent the application from exiting**. These threads are typically used for background tasks that are not essential to the main program's execution.

Because daemon threads do not halt the main process from finishing they're ideal for background threads such as,

1. Garbage collection
2. Session management
3. Periodic clean-up operations
4. Logging
5. Background monitoring

The lifecycle of a daemon thread is tied to the lifecycle of the main thread. If all non-daemon threads finish execution, the Python interpreter will exit, **stopping all daemon threads immediately**.

Let's view a quick example,

```python
import threading
import time


def daemon_thread():
    print("Daemon Thread: Starting")
    time.sleep(2)  # simulate some work
    print("Daemon Thread: Finished")


thread = threading.Thread(target=daemon_thread)
thread.daemon = True  # set the thread as a daemon thread

thread.start()

# The program will terminate before the daemon thread finishes
print("Main Thread: Done")
```

In this example, the output will be

```
Daemon Thread: Starting
Main Thread: Done

Process finished with exit code 0
```

It is crucial to understand that `Daemon Thread: Finished` was never outputted to console. This is because the main application execution completed and because it is a daemon thread, it was killed.

Now, let us compare it to what would happened without this being set.

First, we remove,

```python
thread.daemon = True  # set the thread as a daemon thread
```

Rerunning the script, we can see

```
Daemon Thread: Starting
Main Thread: Done

Daemon Thread: Finished

Process finished with exit code 0
```

Here, the main application ran to completion, **because it is not a daemon thread** the main process did not stop and it waited for all thread to complete their execution.