"""
Logging is useful for persistent storage when dealing with complicated projects
that is going to store all of the data from our program and have different
levels of logs. Levels being something that is `info`, `warning`, ...
"""
import logging

"""
basicConfig needs to be called prior to any logging calls. The functions
`debug`, `info`, `warning`, `error` and `critical` will call basicConfig() 
automatically if no handlers are defined for the root logger. basicConfig does
nothing if the root logger already has handlers configured for it. Therefore
calling basicConfig after for example, `logging.info` will not work as the first
call made by logging.info made some automatic configurations. The later 
configuration attempt silently failed because of the automatic configuration
that had already happened

The logging level is what we want to start outputting or logging at, so if 
I pass a logging.INFO, this means we're going to log everything at the `info`
level and above.

The format attributes / documentation can be found at https://docs.python.org/3/library/logging.html
"""
logging.basicConfig(level=logging.INFO, 
                    filename='log.log', 
                    filemode="w",
                    format="%(levelname)s - %(message)s")

# Logging Levels
logging.debug("debug_message")        # Lowest   |
logging.info("info_message")          #          |
logging.warning("warning_message")    #          |
logging.error("error_message")        #          |
logging.critical("critical_message")  # Highest  V
"""
By default, when using the logging module, you're only going to get the 
output for anything that is at the `warning` level or above. Hence, 
`warning`, `error` and `critical` will log to the console, anything that is 
`info` and `debug` will not. Due to the basicConfig setting the level to
logging.INFO, I have enabled the output of `info` and hence will receive...

INFO:root:info_message
WARNING:root:warning_message
ERROR:root:error_message
CRITICAL:root:critical_message

Where "root" stands for what logger I am using and I am using the "root" logger
because we have not configured our own at this point,
"""

"""
Return a logger with the specified name, creating it if necessary. Always
use getLogger to get the logger, even between different modules. It can be
helpful to make the logger module specific by using __name__.
"""
my_logger = logging.getLogger('My_Logger')
"""
By default this will go into the file and use the format specified by 
basicConfig above, to change this we need to specify a handler. A handler is
what will allow us the configure this logger.

Be aware that my_logger propagates logs to the root logger. (all loggers do).
So any log sent to my_logger will appear in both files, i.e. `log.log` and
`my_logger.log`
"""
handler = logging.FileHandler("my_logger.log", mode="w")
formatter = logging.Formatter("%(name)s: %(levelname)s - %(message)s")
handler.setFormatter(formatter)

my_logger.addHandler(handler)
my_logger.info("Successfully created My Logger!")
try:
    1/0
except ZeroDivisionError as e:
    my_logger.exception("ZeroDivisionError")
