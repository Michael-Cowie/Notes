# Rest Operator

The rest operator in JavaScript is denoted by three dots `(...)`. It's used in various contexts, but here we'll focus on its primary use within function parameters and with arrays.

**Rest Operator in Function Parameters**

The rest parameter syntax allows a function to accept an indefinite number of arguments as an array. It collects the remaining arguments into a single parameter, represented by the rest operator.

```JavaScript
function sum(...numbers) {
  return numbers.reduce((total, num) => total + num, 0);
}

console.log(sum(1, 2, 3, 4, 5)); // Output: 15
```

In this example, the `sum` function can take any number of arguments. The rest operator (`...numbers`) gathers all the arguments into an array called numbers. This makes it easy to handle a variable number of parameters within the function.

**Rest Operator with Destructuring**

The rest operator can also be used in destructuring assignments to collect the remaining elements into a new array or object.


**With Arrays,**


```JavaScript
const [first, ...rest] = [1, 2, 3, 4, 5];

console.log(first); // Output: 1
console.log(rest);  // Output: [2, 3, 4, 5]
```

In array destructuring, the rest operator can be used to capture all remaining elements after extracting the first one. It creates a new array (`rest`) containing the remaining values.

**With Objects,**

```JavaScript
const person = { name: "John", age: 30, city: "New York" };
const { name, ...details } = person;

console.log(name);    // Output: John
console.log(details); // Output: { age: 30, city: "New York" }
```

**Spread operator in function calls**

The spread operator can be used to spread elements of an array or properties of an object into individual elements or properties. When used in function calls, it allows you to pass elements of an array or properties of an object as separate arguments to a function.

Here we can spread with Arrays,

```JavaScript
function sum(x, y, z) {
  return x + y + z;
}

const numbers = [1, 2, 3];

console.log(sum(...numbers)); // Output: 6
```

and with Objects,

```JavaScript
function greet(person) {
  console.log(`Hello, ${person.name}! You are ${person.age} years old.`);
}

const person = { name: "John", age: 30 };

greet({ ...person });
```

Object spreading is very common with React for passing properties to componenets.

Let's have an example of the usage in React,

```HTML
<Modal {...this.props} title='Modal heading' animation={false}>
```

`{...this.props}` spreads out the "own" enumerable properties in props as discrete properties on the Modal element you're creating. For instance, if `this.props` contained `a: 1` and `b: 2`, then this would be the equivalent of,

```HTML
<Modal a={this.props.a} b={this.props.b} title='Modal heading' animation={false}>
```

**Spread operator for conditionally adding to objects**

The spread operator can be useful when conditionally adding to an object.

```JavaScript
const includeExtra = true;

const test_object = {
    'test' : {
        'a': 'a',
        'b': 'b',
        ...(includeExtra && {
            'extra': 'extra'
        })
        
    }
}
```

This syntax is leveraging the fact that if the condition is `false` (i.e., `includeExtra` is `false`), the inner object is an empty object `{}`.

- If `includeExtra` is true, the resulting object is `{ 'extra': 'extra' }`.
- If `includeExtra` is false, the resulting object is `{}` because `false` is treated as a `falsy` value, and the spread operator effectively spreads nothing.