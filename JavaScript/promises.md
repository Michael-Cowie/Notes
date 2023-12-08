# Promises

A 'Promise' is an object that represents the eventual completion or failure of an asynchronous operationand allow you to attach callbacks that will be executed when the operation is completed or when an error occurs. It has 3 states

1. **Pending** - The initial state; the promise is neither fulfilled nor rejected.
2. **Fulfilled** - The operation completed successfully, and the promise has a resulting value.
3. **Rejected** - The operation failed, and the promise has a reason for the failure.

# Creating a Promise

```JavaScript
const myPromise = new Promise((resolve, reject) => {
  // Perform asynchronous operation
  const operation_successful = true;

  if (operation_successful) {
    resolve("Success Data");
  } else {
    reject("Error data");
  }
});
```

# Handling Promise States

- **then()** - Used to handle the resolved state.
- **catch()** - Used to handle the rejected state.
- **finally()** - Executed regardless of the promise state.

```JavaScript
myPromise
    .then(data => {
        console.log(data);  // "Success Data", i.e. data passed to 'resolve'
    })
    .catch(error => {
        console.log(error); // "Error Data", i.e. data passed to 'reject'
    })
    .finally(() => {
        console.log("Finally Block");
    })
```

# Promise Chaining

The `then()` method of a Promise returns a new Promise. This mechanism is what allows chaining in promise-based asynchronous code.
Each call to `then()` returns a new Promise that represents the eventual completion or failure of the operation specified in that `then()` callback. The value that the new Promise is fulfilled with is the return value of the callback passed to that then call.

 For arrow functions, if the function body consists of a single expression, the return statement is implicit. Hence, in our first example we have `.then(response => response.json())`. The value of `response.json()` represents the `resolve()` being called on our Promise and returning the value will then pass it as the data to the next `then()` call.

In a promise chain, you generally only need one `catch()` at the end to handle errors that may have occurred at any point in the chain. This is because when an error occurs in any `then()` block in the chain, it will propagate down the chain until it encounters the next `catch()` block.

```JavaScript
// Chain promises to make sequential HTTP requests using fetch
fetch('https://jsonplaceholder.typicode.com/posts/1')
    .then(response => response.json())
    .then(json_data => {
        console.log(`Request 1 succeeded with data: ${JSON.stringify(json_data)}`);
        return delay(1000); // Simulate a delay before the next request
    })
    .then(() => fetch('https://jsonplaceholder.typicode.com/posts/2'))
    .then(response => response.json())
    .then(json_data => {
        console.log(`Request 2 succeeded with data: ${JSON.stringify(json_data)}`);
        return delay(1000);
    })
    .catch(error => {
        console.error(`One of the requests failed: ${error}`);
    });
```

# Promises and Event Loop

When you create a Promise, its executor function is executed immediately. This function typically contains asynchronous operations. When you create a Promise and its executor function is immediately called, it might seem counterintuitive if you think of asynchrony purely in terms of I/O tasks. However, this immediate invocation is more related to the nature of the Promise mechanism and how it manages asynchronous control flow:

The immediate execution of the executor function allows for the decoupling of the asynchronous task from the Promise itself. The Promise is a placeholder for a value that may not be available yet. This design enables you to create a Promise and handle its resolution or rejection later, allowing for more flexible and expressive code.

Promises are designed to represent the eventual outcome of an asynchronous operation, whether it's I/O or some other form of delayed computation.

```JavaScript
const myPromise = new Promise((resolve, reject) => {
  // Asynchronous operations
  fetch('https://jsonplaceholder.typicode.com/posts/1')
    .then(response => response.json())
    .then(data => resolve(data))
    .catch(error => reject(error));
});
```

In this example, the asynchronous operation is a network request using fetch. The `resolve` and `reject` functions are used to signal the completion or failure of the operation. When an asynchronous operation completes, its corresponding `resolve` or `reject` callback is scheduled as a microtask. Microtasks have higher priority than regular tasks in the event loop, ensuring they are executed before the next rendering or user input handling.

The event loop continuously checks the microtask queue for pending tasks. If the microtask queue is not empty, the event loop executes the microtasks in the order they were added. Promises use the microtask queue to ensure that their callbacks are executed in a predictable order.