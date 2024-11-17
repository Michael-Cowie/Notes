<div align="center">
  <h1> Conditional Chaining </h1>
</div>

The `?.` syntax is called the "optional chaining" operator provides a concise way to handle cases where you want to access a property or call a method on an object **that might be null or undefined**, without causing an error. Optional chaining allows you to succinctly and safely navigate through nested object properties or method calls, gracefully handling scenarios where intermediate properties might be null or undefined without causing errors.

```JavaScript
const user = {
    profile: {
        address: {
            city: "New York",
            postalCode: 10001
        }
    }
};

// Accessing a deeply nested property without optional chaining
const city1 = user && user.profile && user.profile.address && user.profile.address.city;
console.log(city1); // Outputs: "New York"

// Accessing a deeply nested property with optional chaining
const city2 = user?.profile?.address?.city ?? "Default City";
console.log(city2); // Outputs: "New York"

/**
 * Example with a missing property.
 * 
 * In this example, trying to access `location` will result in `undefined` because it's not on the object.
 * However, instead of throwing errors by trying to access `city` on undefined, it can safely stop and
 * be assigned to the default value provided after `??`.
**/
const missingCity = user?.profile?.location?.city ?? "Default City";
console.log(missingCity); // Outputs: "Default City"
```

# `??`

The `??` operator, known as the "nullish coalescing" operator, is used to provide a default value when a variable is `null` or `undefined`. The nullish coalescing operator is often used in conjunction with optional chaining `?.` to handle cases where you want to provide a default value when a property access or method call might result in null or undefined. It can be utilized without optional chaining too,

```JavaScript
let result = null ?? "Default Value";
console.log(result); // Outputs: "Default Value"
```
