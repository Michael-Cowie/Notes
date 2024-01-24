# Promises

A 'Promise' is an object that represents the eventual completion or failure of an asynchronous operation and allow you to attach callbacks that will be executed when the operation is completed or when an error occurs. It has 3 states

1. **Pending** - The initial state; the promise is neither fulfilled nor rejected.
2. **Fulfilled** - The operation completed successfully, and the promise has a resulting value.
3. **Rejected** - The operation failed, and the promise has a reason for the failure.

# Creating a Promise

```JavaScript
const myPromise = new Promise((resolve, reject) => {
  // Perform asynchronous operation (await something else, etc...)
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

myPromise.then(result => {
  console.log(result);
});
```

In this example, the asynchronous operation is a network request using `fetch`. The `resolve` and `reject` functions are used to signal the completion or failure of the operation. When an asynchronous operation completes, its corresponding `resolve` or `reject` callback is scheduled as a microtask. Microtasks have higher priority than regular tasks in the event loop, ensuring they are executed before the next rendering or user input handling.

The event loop continuously checks the microtask queue for pending tasks. If the microtask queue is not empty, the event loop executes the microtasks in the order they were added. Promises use the microtask queue to ensure that their callbacks are executed in a predictable order.

In this example, it is crucial to remember the definition of asynchronous functions, **asynchronous behaviour is executed later**. Inside our promise we call an asynchronous function `fetch`, returning a `Promise` and then calling `then()` to listen to the callback. In this code snippet, the complete execution of the code is ran and the underlying mechanism of `fetch` is ran, which listens to `I/O` requests in a background process. When the request has been retrieved from the server, the event is queued to be executed which will then pass the data to our function callback.

![](../images/promises_async.png)

Under the hood, the `fetch` API uses a `XMLHttpRequest` object to send HTTP requests and receive respones from the server. `XMLHttpRequest` is a low-level API. In a simplistic example, `fetch` could appear to work as the following.

```JavaScript
function fetch(url, options) {
  // create a new Promise object
  return new Promise((resolve, reject) => {
    // create a new XMLHttpRequest object
    const xhr = new XMLHttpRequest();

    // handle the response from the server
    xhr.onload = () => {
      const response = new Response(xhr.responseText, {
        status: xhr.status,
        statusText: xhr.statusText,
        headers: xhr.getAllResponseHeaders()
      });
      resolve(response);
    };

    // handle any errors that occur while fetching
    xhr.onerror = () => {
      reject(new TypeError('Network request failed'));
    };

    // open the connection to the server
    xhr.open(options.method || 'GET', url);

    // set any headers that were provided
    for (const header in options.headers) {
      xhr.setRequestHeader(header, options.headers[header]);
    }

    // send the request to the server
    xhr.send(options.body);
  });
}
```

# Promise Chaining

In the previous example,

```JavaScript
const myPromise = new Promise((resolve, reject) => {
  // Asynchronous operations
  fetch('https://jsonplaceholder.typicode.com/posts/1')
    .then(response => response.json())
    .then(data => resolve(data))
    .catch(error => reject(error));
});
```

we utilized `response.json()` and propagated it to another `then()`. The reason this occurred is because `response.json()` is asynchronous. Here, `.json()` returning another promise. When returning a promise inside of `then()`, the next `then()` does not receive an object, it waits until the promise is resolved and passes the result. This also means we could `await response.json()`.

Interestingly, after the initial `fetch()` call, only the headers have been read. So, to parse the body as JSON, first the body data has to be read from the incoming stream. Because reading from the TCP stream is asynchronous, the `.json()` operation ends up asynchronous. The actual parsing of the JSON itself is not asynchronous. It's just the retrieving of the data from the incoming stream that is asynchronous.

When you return something from a `then()` callback, it's a bit magic. **If you return a value**, the next `then()` is called with that value. However, **if you return something promise-like**, the next `then()` waits on it, and is only called when that promise settles (succeeds/fails).

```JavaScript
const five_promise = new Promise((resolve, reject) => {
  resolve(5); // Immediately resolve and pass 5 to the next `then()`
})

const ten_promise = new Promise((resolve, reject) => {
  resolve(10); // Immediately resolve and pass 10 to the next `then()`
})

const example = five_promise
  .then(d => {
      console.log(d); // 5
      return ten_promise; // Return a promise. This means it will wait until resolved and pass the resolved value.
  })
  .then(d => {
      console.log(d); // 10
      return 15 // Return a value. Passed to the next `then()`
  })
  .then(d => {
      console.log(d); // 15
  })
  .catch(error => {
      console.error(`Error occurred in one of the then() chains`);
  });
```

The `then()` method of a Promise returns a new Promise. This mechanism is what allows chaining in promise-based asynchronous code. Each call to `then()` returns a new Promise that represents the eventual completion or failure of the operation specified in that `then()` callback. The value that the new Promise is fulfilled with is the return value of the callback passed to that then call.

For arrow functions, if the function body consists of a single expression, the return statement is implicit. Hence, in our first example we could have instead have `.then(response => response.json())`.

In a promise chain, you generally only need one `catch()` at the end to handle errors that may have occurred at any point in the chain. This is because when an error occurs in any `then()` block in the chain, it will propagate down the chain until it encounters the next `catch()` block.