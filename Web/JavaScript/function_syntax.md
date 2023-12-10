# Function Definition Syntax

**1. Function Declaration**

Using the `function` keyword,

```JavaScript
function regularFunction() {
  // Function body
}
```

**2. Function Expression**

Assigning a function to a variable,

```JavaScript
const regularFunction = function() {
  // Function body
};
```

**3. Arrow Function**

A concise way to write functions introduced in ES6,

```JavaScript
const arrowFunction = () => {
  // Function body
};
```

This is essentially assigning a variable to an anonymous function. `let` can also
be used, but generally avoided as `const` prevents reassignment.

**4. Arrow Function (Short Syntax)**

For a single-expression functions, curly braces and `return` can be omitted,

```JavaScript
const shortArrowFunction = () => expression;
```

**5. Async Functions**

A function that returns a Promise and can use `await` for asynchronous operations,

```JavaScript
async function asyncFunction() {
  // Asynchronous function body
}
```

**6. Async Arrow Functions**

An asynchronous arrow function,

```JavaScript
const asyncArrowFunction = async () => {
  // Asynchronous function body
};
```

**7. Named Function Expression**

Giving a name to a function expression,

```JavaScript
const namedFunctionExpression = function namedFunction() {
  // Function body
};
```

The name `namedFunction` is only visible within the function itself (for recursion or referencing the function inside itself).