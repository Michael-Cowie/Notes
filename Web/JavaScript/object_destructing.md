# Object Destructing

**1. Basic object destructing by extracting values from objects and assign them to variables.**

```JavaScript
const person = { name: "John Doe", age: 30};
const { name, age } = person;

console.log(name); // John Doe
console.log(age);  // 30
```

This is the equivalent of,

```JavaScript
const person = { name: "John Doe", age: 30 };
const name = person.name;
const age = person['age'];

console.log(name); // John Doe
console.log(age);  // 30
```

**2. It can be helpful to provide default values too,**

```JavaScript
const { name, age, city = "Unknown" } = person;
console.log(city); // Unknown if 'city' is not present in 'person', else, the value inside 'person'
```

**3. Nested Destructing**

```JavaScript
const nestedObj = { 
    outer: { 
        inner: "value" 
    } 
};

const { 
    outer: { 
        inner
    } 
} = nestedObj;

console.log(inner); // value
```

Keep in mind, you must keep the name the same as the key inside the nested object. To change the variable from `inner` to a different one, the colon `:` must be used.

```JavaScript
const nestedObj = { 
    outer: { 
        inner: "value" 
    } 
};

const { 
    outer: { 
        inner: myVariable
    } 
} = nestedObj;

console.log(myVariable); // value
```

**4. Rest operator**

The `...` operator can be used to assign a variable to the remaining, unobtained keys.

```JavaScript
const person = { name: "John Doe", age: 30, city: "Christchurch"};
const { name, ...rest } = person;

console.log(name); // John Doe
console.log(rest); // { age: 30, city: "Christchurch" }
```

**5. Function parameters**

```JavaScript
function printPersonDetails({ name, age }) {  // The `{` and `}` are destructing during the function call.
  console.log(`${name} is ${age} years old.`);
}

printPersonDetails(person);
```

**5. Object destruction using TypeScript**

For this to work in TypeScript, objects need to have an interface for all accessible variables.

```JavaScript
interface Person {
  name: string;
  age: number;
  city: string;
}

const person: Person = { name: "John Doe", age: 30, city: "New York" };
const { name, age, city }: Person = person;

console.log(name); // John Doe
console.log(age);  // 30
console.log(city); // New York
```

For function parameter typing, it's done as follows,

```JavaScript
function printPersonDetails({ name, age }: Person) {
  console.log(`${name} is ${age} years old.`);
}

printPersonDetails(person);
```
