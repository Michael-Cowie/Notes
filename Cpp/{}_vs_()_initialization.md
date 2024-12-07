<div align="center">
  <h1> List Initialization using `{}` </h1>
</div>

In C++ 11, we have new syntax for initializing classes which gives us a big number of possibilities how to initialize variables, 

```C++
MyClass a1 {a};
MyClass a2 = {a};
MyClass a3 = a;
MyClass a4(a);
```

Using `{}` instead of `()` when setting variables is known as brace initialization or uniform initialization. Brace initialization has several characteristics and behaviors that differ from traditional parentheses initialization.

Our focus is on `MyClass a1 {a};`, initializion list using curly braces.

The key beneifts of List initialization using curly braces is that **it does not allow narrowing** (§iso.8.5.4). That is:

1. An integer cannot be converted to another integer that cannot hold its value. For example, `char` to `int` is allowed, but not `int` to `char`.

2. A floating-point value cannot be converted to another floating-point type that cannot hold its value. For example, `float` to `double` is allowed, but not `double` to `float`.

3. A floating-point value cannot be converted to an integer type.

4. An integer value cannot be converted to a floating-point type.

```C++
void fun(double val, int val2) {

    int x2 = val;    // if val == 7.9, x2 becomes 7 (bad)

    char c2 = val2;  // if val2 == 1025, c2 becomes 1 (bad)

    int x3 {val};    // error: possible truncation (good)

    char c3 {val2};  // error: possible narrowing (good)

    char c4 {24};    // OK: 24 can be represented exactly as a char (good)

    char c5 {264};   // error (assuming 8-bit chars): 264 cannot be 
                     // represented as a char (good)

    int x4 {2.0};    // error: no double to int value conversion (good)

}
```

# Constructors

There are MANY reasons to use brace initialization, but you should be aware that **the `initializer_list<>` constructor is preferred to the other constructors**, the exception being the default-constructor. This leads to problems with constructors and templates where the type `T` constructor can be either an initializer list or a plain old constructor.

```C++
struct Foo {
    Foo() {}

    Foo(std::initializer_list<Foo>) {
        std::cout << "initializer list" << std::endl;
    }

    Foo(const Foo&) {
        std::cout << "copy ctor" << std::endl;
    }
};

int main() {
    Foo a;
    Foo b(a); // copy ctor
    Foo c{a}; // copy ctor + initializer list!
}
```

In rare cases, such as `vector<int> v(10,20);` or `auto v = vector<int>(10,20);`, the result is a `std::vector` with 10 elements. If we uses braces, the result is a `std::vector` with 2 elements. This happens because different constructor 

# Member Initialization List

`{}` assignments can also be used inside the member initialization list.

```C++
class MyClass {
public:
    MyClass(int value) : memberVariable{value} {
        // Constructor body
    }

private:
    int memberVariable;
};
```

In this example, the member initialization list initializes the `memberVariable` using brace initialization syntax: `memberVariable{value}`. The provided `value` is used to initialize the `memberVariable` directly. By using `{}` in the member initialization list, you ensure that `memberVariable` is initialized using direct initialization, with potential type checking and prevention of narrowing conversions.

# User Defined-Classes

### Aggregates

If the user-defined type is an aggregate (a class or structure without user-declared constructors, virtual functions, or base classes), brace initialization performs aggregate initialization. Each member of the aggregate is initialized by the corresponding value provided within the braces.

```C++
struct Point {
    int x;
    int y;
};

Point p{10, 20};  // Aggregate initialization
```

### Constructor Matching

If the user-defined type has user-declared constructors, brace initialization attempts to match the provided values with the constructors of the type. If there is a constructor that matches the provided arguments, it will be used for initialization.

```C++
class MyClass {
public:
    MyClass(int value1, int value2) {
        // Constructor body
    }
};

MyClass obj{10, 20};  // Initialization using matching constructor
```

### Constructor Overload Resolution

If there are multiple constructors that can be potentially matched, overload resolution rules will be applied to determine the most appropriate constructor to use.

```C++
class MyClass {
public:
    MyClass(int value) {
        // Constructor body
    }

    MyClass(std::string str) {
        // Constructor body
    }
};

MyClass obj{10};       // Initialization using int constructor
MyClass obj2{"Hello"}; // Initialization using string constructor
````
