# For `[in, of]` looping.

Both `for...in` and `for...of` are looping constructs which are used to iterate over data structures. The only difference between them is the entities they iterate over,

1. `for...in` iterates over all enumerables **property keys of an object**.
2. `for...of` iterates over the **values of an iterable object**. Iterable objects are arrays, strings, etc...

The `for...of` is defined by the [Symbol.iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols, this defines the values returned by `for...of`. The iterable protocol involves defining the `Symbol.iterator` method on your object, which returns an iterator object with a `next` method. The `next` method should return an object with `value` and `done` properties.

To create an example with a customizable `for...of` behaviour, it would appear as the following.

```JavaScript
// Define a custom data structure
function SquareDataStructure(data) {
    this.data = data;
}

// Implement the iterable protocol
SquareDataStructure.prototype[Symbol.iterator] = function () {
    let index = 0;

    return {
        next: () => {
            if (index < this.data.length) {
                const squaredValue = this.data[index] ** 2;
                index++;
                return { value: squaredValue, done: false };
            } else {
                return { done: true };
            }
        }
    };
};

// Use the custom data structure with for...of
let myInstance = new SquareDataStructure([1, 2, 3, 4, 5]);

// Will output 1, 4, 9, 16, 25
for (let squaredValue of myInstance) {
    console.log(squaredValue);
}
```

Additional key points,

1. `SquareDataStructure.prototype`: In JavaScript, every function has a `prototype` property. This property is used when creating instances of the function using the `new` keyword. It allows you to add properties and methods that will be shared by all instances created from that constructor function. So, `SquareDataStructure.prototype` is accessing the `prototype` object associated with the `SquareDataStructure` function.

2. `[Symbol.iterator]`: Square brackets `[]` are used for property access, and `Symbol.iterator` is a special symbol in JavaScript. When you define a method with the key `Symbol.iterator` on an object, it indicates that the object is iterable. The `Symbol.iterator` symbol is part of the iterable protocol, enabling objects to define their own iteration behavior.

The equivalent being as Class instead of a function would be,

```JavaScript
class SquareDataStructure {
    constructor(data) {
        this.data = data
        this.index = 0;
    }

    // Implement the iterable protocol
    [Symbol.iterator]() {
        return {
            /**
             * Must use lambda function.
             * 
             * When using the function keyword, it creates its own context, 
             * and `this` inside that function doesn't refer to the instance 
             * of SquareDataStructure. Instead, it refers to the context of 
             * the `next` function itself.
             */
            next: () => {
                if (this.index < this.data.length) {
                    const squaredValue = this.data[this.index] ** 2;
                    this.index++;
                    return { value: squaredValue, done: false };
                } else {
                    return { done: true };
                }
            }
        };
    }
}

let myInstance = new SquareDataStructure([1, 2, 3, 4, 5]);

// Will output 1, 4, 9, 16, 25
for (let squaredValue of myInstance) {
    console.log(squaredValue);
}
```

# Arrays

Let us take an example of looking using `in`.

```JavaScript
let myArray = [1, 2, 3];

myArray.addedProp = 'arrProp';

for (let elementKey in myArray) {
    console.log(elementKey);
}

console.log(myArray);
console.log(Object.keys(myArray));
console.log(Object.values(myArray));
```

Will output,

```JavaScript
0
1
2
addedProp
(3) [1, 2, 3, addedProp: 'arrProp']
(4) ['0', '1', '2', 'addedProp']
(4) [1, 2, 3, 'arrProp']
```

As we can see here, it is iterating over the property keys when using `in`, which will include the added property `addedProp` via `myArray.addedProp = ...`. The keys are `0, 1, 2` (which correspond to the array elements), these are the indexes.

Now, let us take an example of using `of`.

```JavaScript
let myArray = [1, 2, 3];

myArray.addedProp = 'arrProp';

for (let elementKey of myArray) {
    console.log(elementKey);
}

console.log(myArray);
console.log(Object.keys(myArray));
console.log(Object.values(myArray));
```

Will output, 

```JavaScript
1
2
3
(3) [1, 2, 3, addedProp: 'arrProp']
(4) ['0', '1', '2', 'addedProp']
(4) [1, 2, 3, 'arrProp']
```

The key point here is that while the `keys` and `values` of the array are identical, the iteration is different. The output was `0, 1, 2, addedProp` when using `in`, but `1, 2, 3` when using `of`. The `for...of` loop in our example iterates over the **values** of a data structure. The values in this specific example are `1, 2, 3`. The values which an iterable data structure will return using `for...of` is dependent on the type of iterable object.

# Objects

When iterating over `in` we iterate over the enumerable properties.

```JavaScript
let myObject = { a: 1, b: 2, c: 3 };

for (let key in myObject) {
    console.log(key); // Outputs: 'a', 'b', 'c'
}

console.log(Object.keys(myObject)); // Outputs: (3) ['a', 'b', 'c']
```

Now, the thing is `for...of` is not supported for objects. The `for...of` loop is intended for use with iterable objects, such as arrays or strings. By default, plain JavaScript objects (like those created using object literals) are not iterable. To iterate over the values, instead use `Objects.values()` or take the approach of iterating over the `keys` and then grab them,

```JavaScript
let myObject = { a: 1, b: 2, c: 3 };

for (let key in myObject) {
    console.log(myObject[key]); // Outputs: 1, 2, 3
}

console.log(Object.values(myObject)); // Outputs: (3) [1, 2, 3]
```

The other approach is to customize behaviour as previously mentioned using `[Symbol.iterator]` on the object.