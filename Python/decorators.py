"""
Decorators are traditonally used to add additional behaviour
to function calls and are best described as syntactic sugar
"""

# Let's first give an example where a decorator could be used

import time

def timer(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print("Total function runtime:", end_time - start_time)
    
def my_slow_function():
    time.sleep(3) # Wait three seconds
    
timer(my_slow_function)

"""
What a decorator does is allow us to change the function behaviour as follows,

@decorator
def my_function(...):
    ....
    
Now becomes, 

my_function = decorator(my_function)
"""

# Now, instead of having to time our function by calling the timer function,
# we can now do it as

@timer
def my_slow_function():
    time.sleep(3) # Wait three seconds
    
# Which is equivalent to, my_slow_function = timer(my_slow_function)