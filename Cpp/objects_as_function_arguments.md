<div align="center">
  <h1>  Objects as Function Arguments</h1>
</div>

In C++ there are three different ways to pass data to a function. They're pass by **value, reference and by pointer**. All have different characteristics when it comes to efficiency, storage and behaviour. Passing by pointer is quite legacy, primarily used in C.

## Pass by Value

When an object (or built-in type) is passed by value to a function, **the underlying object is copied using its copy constructor**. The new object has additional memory allocated to it and all values and sub-objects are copied and stored separately. If the object passed is a built-in type such as an `int` or `double` value then copying process is cheap and will often not impact performance. However if the passed objects contains a lot of stored values, such as a vector or matrix then the copying process will be expensive in terms of both storage and CPU cycles.

Passing an object by value also means that any modifications made to the object, within the scpe of the function being passed, **will occur on the copied object and not on the object that was passed**.

e.g. Consider a norm function which calculates the Euclidian norm of a Vector of double values. The function returns one double precision value and takes a vector as parameter

The following is pass by value

```C++
double euclid_norm(vector<double> my_vector);
```

This will copy the vector and will make any underlying changes to the copy of that vector, rather than the vector itself. A norm function should not modify a vector, only read its data. This implementation is not needed. It is expensive and the interface does not imply correct usage.

## Passing by Reference

When an object (or built-in type) is passed by reference to a function, the underlying object **is not copied**. The function is given the memory address of the object itself. This saves both memory and CPU cycles as no new memory is allocated and no (expensive) copy constructors are being called. It is a much more efficient operation.

If the function now modifies the object inside the function, **the original object will reflect these modifications**, rather than a copy of the object.

Here is the same `euclid_norm` function modified to pass the vector by reference. Note the added reference symbol `&`.

```C++
double euclid_norm(vector<double>& my_vector);
```

## Passing by const Reference

To solve the problem of not copying AND not modifying the underlying data, a technique known as passing by reference to const is used. This tells `euclid_norm` not to modify `my_vector` within its own space.

```C++
double euclid_norm(const vector<double>& my_vector);
```

It is considered best practice to pass by `const` ref for all types, except built-in types (char, int, double, etc...), for iterators and for function objects (lambdas, classes deriving from `std::*_function`).