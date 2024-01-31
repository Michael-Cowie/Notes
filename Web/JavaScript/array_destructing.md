# Array Destructing

When trying to destruct values from an array, it's essential to encapsulate the variables inside square brackets `[]`. When creating an array with 3 elements such as,

```JavaScript
const numbers = [1, 2, 3];
```

We can assign variables to values in the array using the following format,

```JavaScript
const [variable1, variable2, ...] = ...;
```

From the example above, the array destruction will work as,

```JavaScript
const numbers = [1, 2, 3];
const [one, two, three] = numbers;

console.log(one);   // 1
console.log(two);   // 2
console.log(three); // 3
```

This is frequently used in React for usage of `useState`, for example,

```JavaScript
const [errorMessage, setErrorMessage] = useState<string>('');
```

This works as `useState` returns an array with two items.

# Caveat

Without using `[]`, **you're not destructing the array**.

Take this example code,

```JavaScript
let a = [1, 2, 3];
let b, c, d = a;

console.log(b);
console.log(c);
console.log(d);
```

The output is,

```JavaScript
undefined
undefined
(3) [1, 2, 3]
```

Now, `b` and `c` are `undefined` and `d` is equal to the entire list of `a`.

Well, `let b, c, d = a;` declares 3 variables and assigns a value to one of them. This is equivalent to,

```JavaScript
let b;
let c;
let d = a;
```

This syntax allows you to declare (and optionally assign) several variables in a single statement, e.g.

```JavaScript
let tmp, x = 4, i, y = 2, z = x * 10 + y;
```

Unassigned variables are default-initialized to `undefined`.