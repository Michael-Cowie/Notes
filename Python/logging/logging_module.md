<div align="center">
    <h1> The Python logging Module </h1>
</div>

The `logging` module in Python is a built-in and highly configurable framework for emitting log messages from Python programs. It is widely used for monitoring, debugging and auditing applications, especially as they grow in complexity. Rather than using `print()` statements, `logging` provides a more robust mechanism for tracking events that happen when software runs, offering various logging levels, configurable outputs and flexible handlers.

Logging allows developers to,

- Persist diagnostic messages across application runs.
- Log at different severity levels (info, warning, error, ...).
- Configure where and how messages are output - Console, files, remote servers etc...
- Format logs for readability and traceability.
- Use structured logs for easier parsing and analysis.

<div align="center">
    <h1> Logging Levels </h1>
</div>

| Level      | Function           | Description                     | Level |
|------------|--------------------|---------------------------------| ----- |
| `DEBUG`      | `logging.debug()`  | Detailed information, typically of interest only when diagnosing problems| 1 |
| `INFO`       | `logging.info()`   | Confirmation that things are working as expected. | 2 |
| `WARNING`    | `logging.warning()`| An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected. | 3 |
| `ERROR`      | `logging.error()`  | Due to a more serious problem, the software has not been able to perform some function.| 4 |
| `CRITICAL`   | `logging.critical()`| A serious error, indicating that the program itself may be unable to continue running. | 5 |

When configuring the logging level (e.g., with `level=logging.INFO`), **any logs below that level will be ignored**.

<div align="center">
    <h1> Configuration and Root Logger </h1>
</div>

The `basicConfig()` must be called **before any logging**, because if any logging call is made first, the root logger is automatically configured and later `basicConfig` calls **have no effect** unless `force=True` is specified.

The root logger is the top-level logger. When you call `logging.info()` or `logging.error()` without explicitly getting a logger, **you're using the root logger.**

<div align="center">
    <h1> Log Formatters </h1>
</div>

Log formatters control how log message appear. The `format` parameter in `basicConfig` or in `Formatter` string allows you to define this layout.

```python
"%(name)s: %(levelname)s - %(message)s"
```

Common format specifiers include,

- `%(levelname)s` - The logging level name.
- `%(message)s` - The logged message.
- `%(asctime)s` - Timestamp.
- `%(name)s` - The loggers name.

<div align="center">
    <h1> Logger Objects </h1>
</div>

Rather than relying solely on the root logger, it's good practice to create **named loggers**.

```python
my_logger = logging.getLogger("My_Logger")
```

This allows loggers to be modular, reusable and structured across files and modules. If the same name is reused, the same logger object is returned, preserving its handlers and configurations. Hence, the importance of using `getLogger()` across modules for consistency.

<div align="center">
    <h1> Handlers </h1>
</div>

Handlers **define where log messages go**. Python provides several built-in handler classes.

- `StreamHandler` - stdout/stderr
- `FileHandler` - File output
- `SMTPHandler` - Emails
- `SockerHandler`
- `HTTPHandler`
-  ...

```Python
handler = logging.FileHandler("my_logger.log", mode="w")
formatter = logging.Formatter("%(name)s: %(levelname)s - %(message)s")
handler.setFormatter(formatter)

my_logger.addHandler(handler)
```

**You can attach multiple handlers** to the same logger to log to both console and file simultaneously.

<div align="center">
    <h1> Propagation and Hierarchy</h1>
</div>

Loggers are hierarchical. A logger named `"a.b.c"` is a child of `"a.b"`, which is a child of `"a"`, which is a child of the root logger. This is helpful for large applications that want to isolate logs by module.

**By default, loggers propagate** their messages up the hierarchy.

```python
my_logger = logging.getLogger("parent.child")
my_logger.warning("test")
```

This message will be processed by the `"parent.child"` logger **any** any handlers attached to `"parent"` or event the root logger, unless `propagate=False` is set.

<div align="center">
    <h1> Subloggers </h1>
</div>

You can manually create subloggers with dot-separated names or use `getChild()`.

```python
import logging

parent_logger = logging.getLogger("app")
child_logger = parent_logger.getChild("database")
print(child_logger.name)  # Outputs: 'app.database'
```

This ensures naming consistency and proper log hierarchy. Subloggers inherit configurations and handlers unless explicitly changed.

<div align="center">
    <h1> Logging Exceptions </h1>
</div>

Python allows capturing exception traceback using `logger.exception()`.

```python
try:
    1 / 0
except ZeroDivisionError:
    my_logger.exception("An exception occurred")
```

This logs the message and includes the full traceback.

<div align="center">
    <h1> Subloggers Example </h1>
</div>

In Pythons logging system all loggers are arranged in a hierarchical tree. When a logger emits a log message it,

1. Processes the message **with its own handlers**.
2. If `propagate = True` (Which it is by default), it will **passes the message up** to its parent logger and that loggers handlers will also process it.
3. This continues all the way up to the **root logger**

The below hierarchy is,

```
root
└── My_Logger
    └── My_Logger.subcomponent
```

In this example `sub_logger` is a child of `my_logger`. When `sub_logger.warning(...)` is called it is first handled by `my_logger`s handler, therefore writing to `my_logger.log`. Then it's propagated **up to the root logger**, which also has a handler configured via `basicConfig` to write to `log.log`. Here, we get different results in each file because each handler can format it the way they choose.

If we don't want a sublogger to propagate messages up the tree we would have set `sub_logger.propagate = False`.

| Logger             | Handler Writes To | Propagates To   |
|--------------------|-------------------|-----------------|
| `root`             | `log.log`         | –               |
| `My_Logger`        | `my_logger.log`   | ✅ root         |
| `My_Logger.subcomponent` | (none)        | ✅ `My_Logger` → ✅ root |

```python
import logging

# Configure root logger
logging.basicConfig(
    level=logging.INFO,
    filename='log.log',
    filemode='w',
    format='%(levelname)s - %(message)s'
)

# Log from root logger
logging.debug("Debug message (won’t appear)")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")

# Create a named logger with its own handler
my_logger = logging.getLogger('My_Logger')
handler = logging.FileHandler("my_logger.log", mode="w")
formatter = logging.Formatter("%(name)s: %(levelname)s - %(message)s")
handler.setFormatter(formatter)
my_logger.addHandler(handler)

# Log with the named logger
my_logger.info("Successfully created My Logger!")

# Log an exception
try:
    1 / 0
except ZeroDivisionError:
    my_logger.exception("ZeroDivisionError occurred")

# Demonstrate sublogger
sub_logger = my_logger.getChild("subcomponent")
sub_logger.warning("This is a sublogger warning")
```

<div align="center">
    <h1> Logging Levels Example </h1>
</div>

The Python `logging` module defines five standard logging levels, from lowest to highest severity illustrated previously.

| Level Name   | Numeric Value | Purpose                      |
|--------------|----------------|------------------------------|
| `DEBUG`      | 10             | Detailed information for diagnosing problems. |
| `INFO`       | 20             | General information about program execution. |
| `WARNING`    | 30             | An indication something unexpected happened, but the program is still running. |
| `ERROR`      | 40             | A more serious problem that prevented some function from running. |
| `CRITICAL`   | 50             | A very serious error, possibly a program crash. |

When you configure the level using `basicConfig()` or `logger.setLevel()`, **you're setting a threshold**. It will **only log messages at or above that threshold will be processed**.

```python
logging.basicConfig(level=logging.ERROR)
```

As a result, this will log `ERROR` and `CRITICAL` messages only. This filtering happens **before** any message is passed to handlers. So if the loggers level is `ERROR`, even if your handlers are ready to write, **a `WARNING` message won't be seen by them at all**.


```python
import logging

logging.basicConfig(
    handlers=[logging.FileHandler("level_demonstration.log", mode="w")],
    level=logging.ERROR,
    format="%(levelname)s - %(message)s"
)

logging.debug("This won't show")
logging.info("This won't show either")
logging.warning("Still won't show")
logging.error("This WILL show")
logging.critical("This WILL show too")
```
