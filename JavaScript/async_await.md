# `async` and `await`

`async` and `await` are features introduced in ECMAScript 2017 (ES8) that simplify the use of Promises and asynchronous code in JavaScript. They provide a more synchronous-like syntax for working with asynchronous operations.

The `async` keyword is used to define a function that **returns a Promise implicitly**. Inside an `async` function, you can use the `await` keyword to pause the execution of the function until the Promise that is being `await`ed is resolved, `await` can only be used within an `async` function.

```JavaScript
async function fetchData() {
  const response = await fetch('https://jsonplaceholder.typicode.com/posts/1');
  const data = await response.json();
  return data;
}
```

Because `async` and `await` are syntactic sugar for Promises, we can still mix and match both if we chose to,

```JavaScript
// An async function that returns a Promise
async function exampleAsyncFunction() {
    // Within the async function, you can use await to perform asynchronous operations
    // For demonstration purposes, we'll use a setTimeout to simulate an asynchronous task

    // You can await a Promise directly, as await a function is implicitly awaiting a Promise
    await new Promise(resolve => setTimeout(resolve, 1000));
  
    // After the asynchronous task is completed, the function continues execution
    return 'Async operation completed'; // The return value is passed to the `then()`
  }
  
// Call the async function
exampleAsyncFunction()
    .then(result => {
        console.log(result); // Output: 'Async operation completed'
    })
    .catch(error => {
        console.error('Error:', error);
    });
```

# Error Handling

Async/await makes error handling more straightforward. You can use `try/catch` blocks to catch errors, making the code look similar to synchronous code.

```JavaScript
async function fetchData() {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts/1');
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error:', error);
  }
}
```

Async/await allows you to write asynchronous code that looks more like synchronous code, making it easier to write and understand sequential operations.

# Event Loop

Async/await, like Promises, is built on top of the event loop. When you use `await` inside an `async` function, it doesn't block the entire event loop; instead, it pauses only the execution of that particular function. The use of `await` doesn't prevent other parts of your code or other asynchronous operations from running concurrently. It allows the event loop to continue processing other tasks while waiting for the awaited Promise to resolve.

# Using `async`

`await` is simple to understand, it **must be used inside an `async` defined function**. Therefore, it is more important to understand the limitations of `async` and when we can use it. Here, I will list locations on when we can define a function using `async`.

**1. In the Global Scope (Top Level)** 

You can define an `async` function at the top level of our code. However, keep in mind that top-level `await` is not allowed outside of modules.

    
```JavaScript
// Valid use of async function in the global scope
async function globalAsyncFunction() {
    console.log("Inside globalAsyncFunction");
    return 100;
  }

console.log(globalAsyncFunction());
```

In this example, the value of `globalAsyncFunction()` will be a Promise object. Remember that Promises are ran immediately, hence `console.log("Inside globalAsyncFunction");` will be executed. Then return value `100` will not be received because we cannot `await` this top-level `async` function. 

To utilize this `async` function in the top-level we need to use the Promise `then()` to receive the return value.

```JavaScript
globalAsyncFunction()
  .then(data => {
    console.log(data);
  })
```

**2. In Other Functions**

You can define an `async` function inside another function, including other `async` functions.

```JavaScript
function outerFunction() {
  async function innerAsyncFunction() {
    // ...
  }
  // ...
}
```

Here, the inner async function creates a Promise, and its execution becomes asynchronous, but it doesn't inherently change the behavior of the event loop itself. Let's break down the behaviour from a different example,

```JavaScript
function regularFunction() {
    // Synchronous code
  
    async function asyncInnerFunction() {
      // This function runs asynchronously and returns a Promise
      console.log("Inside asyncInnerFunction");
      return "Some Data 123"    // Passes to 'then()'
    }

    console.log("Before asyncInnerFunction");
    asyncInnerFunction()
        .then(result => {
            console.log(result);
        })
    console.log("After asyncInnerFunction");
    // More synchronous code
}

regularFunction();
```

The order of console outputs is as follows,

1. `Before asyncInnerFunction`
2. `Inside asyncInnerFunction`
3. `After asyncInnerFunction`
4. `Some Data 123`

The `async` function is called immediately, likewise with a Promise executor function. It's return value
is what is passed back to be queued to the event loop, which calls the `then()`. Here, we first 
call the logging from before the `async` function, enter inside and call that logging and then finally exit
and called the after log. During this time, the return value from the asynchronous function is being
queued and calls `then()` which finally logs the result.

**3. Inside Objects or Classes**

You can define an `async` function as a method inside an object or a class.

```JavaScript
const myObject = {
    async myAsyncMethod() {
        // ...
    }
};
  
class MyClass {
    async myAsyncMethod() {
        // ...
    }
}
```
