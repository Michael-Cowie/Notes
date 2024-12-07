<div align="center">
  <h1> C++ Structs </h1>
</div>
C and C++ both have the `struct` keyword available, in C it can hold several data types.

The C style struct will be,

```C
struct [structure tag] {
    member definition;
    ...
} [one or more structure definition];
```

However, in C++ `struct` can be closely thought of as a class because it can do everything a class can do. The better comparison would be, what is the difference between `struct` and `class` in C++.

In terms of language, except one little detail, there is no difference between `struct` and `class`. Contrary to what individuals coming from C first think, a `struct` can have constructors, methods (even `virtual` ones), public, private and protected members, use inheritance and be templated. All like a class.

The only difference is if you don't specify the visibility (`public`, `private` or `protected`) of the members, **they will be `public` in the `struct` and `private` in the class**.

The visibility by default goes just a little further than members, for inheritance if you don't specify anything then the struct will inherit publically from its base class.

```C++
struct T : Base // Same as, struct T: public Base
{
    ...
}
```

Whereas the class will do private inheritance by default,

```C++
class T : Base // Same as, class T : private Base
{
    ...
}
```
# Struct Alias

It is possible to create an alias for any `struct` by using the keyword `using` following the format,

```C++
using AliasName = struct {
    ...
};
```

In the above example we are creating a type alias named `AliasName` for the anonymous `struct`.

A different format could be,

```C++
struct MyStruct {
    int x;
    int y;
};

using Point = MyStruct;
```

Both accomplish the same thing, by creating an alias. However in this example it is creating an alias for `MyStruct`. In this example, we first define the `MyStruct` `struct`. Then, outside of the `struct` definition, we use the `using` keyword to create an alias named `Point` for the `MyStruct` type. From this point onwards, `Point` can be used interchangeably with `MyStruct` such as,

```C++
AliasStruct obj;
obj.x = 5;
obj.y = 10;
```

It is important to note that `Point` is not a new type, but simply an alias for `MyStruct`. It does not introduce any new memory overhead or create a separate definition.

An alias can also be create using the `typedef` approach, but it seen as the lessn modernized way,

```C++
typedef struct MyStruct {
    int x;
    int y;
} Point;
```
