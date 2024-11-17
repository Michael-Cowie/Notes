<div align="center">
  <h1>  Asynchronous File Handling </h1>
</div>

Asynchronous behaviour is specifically designed for IO operations, however file handling is treated slightly differently. Most operating systems don't support asynchronous file operations. That's why asyncio doesn't support them either. For now, the workaround is to use aiofiles that uses threads to handle files.

Asynchronous programming is best utilized for IO-bound and high-level structured network code for the performance improvement related to network and web-servers, database connection libraries, distributed task queues, etc...

This means asynchronous single threaded code is generally only truly asynchronous when we are **exclusively waiting** on an event. For example, when we send a network request we are **waiting** for the response, we are not performing some action during the waiting time such as reading/writing to a file. Another example could be an `await` for event driven behaviour such as clicking a button. During this time we are waiting for a button click event, when the click is complete this will send an event back to the event loop to continue the generator using the `send` method (Python).

The Linux kernel provides asynchronous operations on the filesystem (aio), but it requires a library and it doesn't scale with many concurrent operations.

# Windows OVERLAPPING flag

Above I said **most** operating systems do not support asynchronous file handling, Windows has an optional flag for this. Windows I/O is inherently asynchronous, so performing an async operation in .NET for example should not use a thread, once the operation completes some existing threads are briefly borrowed to notify of the operation's completion, but no threads are created.

Windows supports asynchronous file I/O via the OVERLAPPED flag (with the notable exception of opening files). This flag is what is libuv uses to accomplish the behaviour of asynchronous file handling.
