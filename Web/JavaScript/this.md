<div align="center">
  <h1> `this` </h1>
</div>

The `this` keyword is a special keyword that refers to the object on which a method or function is being invoked. The value of this is determined by the execution context and how a function is called.

## Global Context

In the global context (outside of any function or object), `this` refers to the global object. In a web browser environment, the global object is typically `window`.

```JavaScript
console.log(this === window); // Output: true (in a browser environment)
```

In other environments this can change, for example `this` in NodeJS global scope is the current module.exports object, not the global object. This is different from a browser where the global scope is the global `window` object. Consider the following code executed in Node,

```Node
console.log(this);    // logs {}

module.exports.foo = 5;

console.log(this);   // log { foo:5 }
```

First we log an empty object because there are no values in `module.exports` in this module. Then we put `foo` on the `module.exports` object, when we then again log `this` we can see that it now logs the updated `module.exports` object.

We can access the `global` object in Node using the `global` keyword.

```Node
console.log(global);
```

The `global` object exposes a variety of useful properties about the environment. Also this is the place where functions such as `setImmediate` and `clearTimeout` are located.

## Function Context
What is important to understand in JavaScript is that every single function or method call in JavaScript sets a new value for `this`. And, which value is set is determined by how the function is called. `this` inside a function call gets set according to how a function is called. There are six main ways that `this` gets set.

**1. Normal Function Call** - In a normal function call such as `foo()`, `this` is set to their the global object (which is `window` in a browser or `global` in nodejs) or to `undefined` (in JavaScripts strict mode).

**2. Method Call** - If a method is called such as `obj.foo()` where the method `foo` is a normal method declaration using the `function` keyword or using the regular method declaration syntax for a `class`, then `this` is set to `obj` inside the function.

**3. `.apply()` or `.call()`** - If `.apply()` or `.call()` is used, then `this` is set according to what is passed to `.apply()` or `.call()`. For example, you could do `foo.call(myObj)` and cause `this` to be set to `myObj` inside of `foo()` for that particular function call.

**4. using `new`** - If you call a function with `new` such as `new foo()`, then a new object is created and the constructor function `foo` is called with `this` set to the newly created object.

**5. using `.bind()`** - When using `.bind()` a new stub function is returned from that call that internally uses `.apply()` to set the `this` pointer as was passed to `.bind()`. FYI, this isn't really a different case because `.bind()` can be implemented with `.apply()`

**6. Using ES6 Fat Arrow Function** - Defining a function via the arrow syntax in ES6+ will bind the current lexical value of `this` to it. So, no matter how the function is called elsewhere (with any of the previous ways to call it), the `this` value will be set by the interpreter to the value that `this` has when the function was defined. This is completely different than all other function calls. In JavaScript, arrow functions do not have their own `this` binding. Instead, they inherit the this value from the surrounding scope (lexical scoping)

# Arrow Function and Functions

Arrow functions **don't have their own `this` or `arguments` binding**. Instead, those identifiers are resolved in the lexical scope like any other variable. That means that inside an arrow function, `this` and `arguments` refer to the values of `this` and `arguments` in the environment the arrow function is *defined* in (i.e. "outside" the arrow function).

```JavaScript
// Example using a function expression
function createObject() {
  console.log('Inside `createObject`:', this.foo); // This will use the provided 'foo', i.e. 21
  return {
    foo: 42,
    bar: function() {
      console.log('Inside `bar`:', this.foo);     // This will refer to the 'foo' inside the object, i.e. 42
    },
  };
}

createObject.call({foo: 21}).bar(); // override `this` inside createObject with the provided object.
```

In the function expression case, `this` refers to the object that was created **inside** the createObject.

```JavaScript
// Example using a arrow function
function createObject() {
  console.log('Inside `createObject`:', this.foo);
  return {
    foo: 42,
    bar: () => console.log('Inside `bar`:', this.foo), // 21, not 42!
  };
}

createObject.call({foo: 21}).bar(); // override `this` inside createObject
```

In the arrow function case, `this` refers to `this` of createObject itself, i.e. `{foo: 21}`.

This makes arrow functions useful if you need to access the `this` of the current environment,

```JavaScript
// currently common pattern
var that = this;
getData(function(data) {
  that.data = data;
});

// better alternative with arrow functions
getData(data => {
  this.data = data;
});
```

This also means that it is not possible to set an arrow functions `this` with `.bind` or `.call`.

Adding to the previous example, by calling directly `createObject().bar();`, `this` will be set to the global object, resulting in `undefined` as the environment global will most likely not have `foo` set to the global object for the first `this.foo`.
In this example `this.a` will print `undefined`

```JavaScript
let a = 5;

const test = () => {
  let a = 10;
  return console.log(this.a);
};

test();
```
In the context of arrow functions, the value of `this` is determined by where the arrow function is defined, not where it is called. In the example above, the arrow function is defined at the top level (not within a specific object or class), so `this` in the arrow function refers to the global object (`window` in browsers, or `global` in Node.js). Running this, both will print `undefined` as neither have an attirbute `a`. In this example, the same goes for if it was defined using `function test() {`
