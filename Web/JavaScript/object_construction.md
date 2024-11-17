<div align="center">
  <h1> Object Construction </h1>
</div>

Objects are the foundation of most data structures and applications. They allow you to group related data and behavior together, making your code more modular, reusable, and easier to understand.

JavaScript objects are collections of key-value pairs. Keys are strings, and values can be any data type (e.g., numbers, strings, arrays and functions). They are used to store and manage data in a structured way.

# Object Literals

Object literals are the most straightforward way to create an object. They are concise and easy to read, making them ideal for most cases.

```JavaScript
const person = {
    firstName: "John",
    lastName: "Doe",
    age: 30,
    greet() {
        console.log(`Hello, my name is ${this.firstName}`);
    }
};
```

In this example, `greet` fill be implicitly defined as a string key and the function will be the value. Additionally, their are other shorthands to create objects, such as,

```JavaScript
let myLocation = "New Zealand";

let myObject = { myLocation }
```

When you see a variable being used as the following, it means that the key will be the same name as the variable and the value will be the variable name, i.e. 

```JavaScript
console.log(myObject.myLocation)    // "New Zealand"
console.log(myObject["myLocation"]) // "New Zealand"
```

# Anonymous Objects

Anonymous objects are frequently used, especially used in frameworks such as React. They're simply created objects without a variable assigned to them,

```Jsx
<MyContext.Provider value={ { selectedDate, setSelectedDate } } >
```

In this example, `selectedDate` and `setSelectedDate` were variables returned by a `useState` function call. However, when we pass `{ selectedDate, setSelectedDate }` to `value` the following is happening,

1. We are creating an anonymous object with the syntax `{ ... }`
2. Assigning the key `selectedDate` to the value of `selectedDate`
3. Assigning the key `setSelectedDate` to the value of `setSelectedDate`

We are then passing that object to the context. As a smaller JavaScript based example,

```JavaScript
let x = 5;
let y = 10;

console.log({ x, y }); // {x: 5, y: 10}
```

# ES6 Classes

Classes provide a cleaner and more structured way to define objects, especially when you need to create multiple instances with shared behaviour.

```JavaScript
class Person {
    constructor(firstName, lastName, age) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
    }

    greet() {
        console.log(`Hello, my name is ${this.firstName}`);
    }
}

const person1 = new Person("John", "Doe", 30);
person1.greet()
```

# `Object.create()`

`Object.create()` allows you to create a new object with a specified prototype, giving you fine control over inheritance. A **prototype** is a mechanism through which objects inherit properties and methods from other objects. Every JavaScript object has a prototype, which is itself an object. 

Whenever you try to get a property on an object it will check the object for that property name. If it does not exist it will look in the prototype. When you try to access a property or method on an object and it doesn't exist on that object, JavaScript will look for it in the object's prototype. If it doesn't find it there, it will continue up the prototype chain until it either finds the property/method or reaches the end of the chain (which is `null`).

```JavaScript
var o = {
  "foo": "bar",
  "method": function() {
    console.log("A method");
  }
};

var o2 = Object.create(o);

console.log(o2.hasOwnProperty("foo")); // false
console.log(o2.foo); // "bar"
console.log(o2.__proto__ === o); // true

o.baz = "foobar";
console.log(o2.baz); // "foobar"
```

Therefore, because `o` is set as the prototype for `o2`, when searching for variables and they're not found on `o2` it will search for them on `o`. In this example, `o2` can access `baz` when it is later added on the prototype for `o2`, but it is not a directy property of `o2`.

# Spread and Rest Operators

You can use the spread operator to copy or merge objects, and the rest operator to collect remaining properties into a new object.

```JavaScript
const person = {
    firstName: "John",
    lastName: "Doe",
    age: 30
};


const personCopy = { ...person };

const personCopyWithModifiedAge = { ...person, age: 27};
```

Unlike using `Object.create(...)`, this does not set the provided object as the prototype.

# Computed Property Names

Computed property names allow you to dynamically define keys in an object.

```JavaScript
const key = "age";
const person = {
    firstName: "John",
    [key]: 30,
    lastName: "Doe"
};

console.log(person.age) // 30
```
