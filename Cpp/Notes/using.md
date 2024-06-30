# Table of Contents

1. [Introduction](#introduction)
2. [Using Declarations (Importing Members)](#using-declarations-importing-members)
3. [Using Directives (Importing Namespaces)](#using-directives-importing-namespaces)
4. [Type Aliases](#type-aliases)
5. [Using in Inheritance (Access Control)](#using-in-inheritance-access-control)
6. [Using for Template Aliases](#using-for-template-aliases)
7. [`using` with `enum`](#using-with-enum)

# Introduction
The `using` keyword in C++ is a versatile tool designed to enhance code readability, maintainability, and ease of use. It was introduced to simplify various aspects of the language and provide more flexible ways of managing names, types and inheritance.

The `using` keyword in C++ is a multi-purpose directive that simplifies the process of,

1. Importing specific members of entire namespaces.
2. Creating type aliases for readability and ease of maintenance.
3. Bringing base class members into derived class scope, often to change access control.
4. Simplifying template definitions and usage.

### Using Declarations (Importing Members)

This usage allows you to bring a specific member from a namespace into the current scope

```C++
#include <iostream>

using std::cout;

int main() {
    cout << "Hello, world!\n";
    return 0;
}
```

In this example, the namespace is `std` and the specific member is `cout`.

### Using Directives (Importing Namespaces)

This usage brings all of the members of a namespace into the current scope.

```C++
#include <iostream>

using namespace std;

int main() {
    cout << "Hello, world!\n";
    return 0;
}
```

In this example, the namespace is `std` and the specific member is `cout`, however, you can also bring all members of the namespace `std` into the current scope.

### Type Aliases

This usage allows you to create an alias for a type, making your code more readable or easier to modify.

```C++
#include <iostream>

int main() {
    using String = std::string;
    
    String name = "John Doe";
    std::cout << name;
    return 0;
}
```

In this example, we can now use `String` instead of `std::string`. Keep in mind, this is notably identical to the syntax of `typedef <type> <alias_name>`, 

```C++
#include <iostream>

int main() {
    typedef std::string String;
    
    String name = "John Doe";
    std::cout << name;
    return 0;
}
```

Hence we can do both,
```C++
using String = std::string;
```

and 

```C++
typedef std::string String;
```

The `using` alias declaration is compatible with templates, whereas the C style `typedef` is not.

### Using in Inheritance (Access Control)

When dealing with classes, `using` can be used to bring a base class's member into the derived class's scope, often to change access control.

```C++
#include <iostream>

class Base {
protected:
    void display() { std::cout << "Base display" << std::endl; }
};

class Derived : public Base {
public:
    using Base::display; // Changes protected to public in Derived
};

int main() {
    Derived d;
    d.display(); // Now accessible publicly
    return 0;
}
```

Generally, you cannot call the `display` method if you made an instance of `Base` because it's `protected`. However, in this example we use `using` to change the access control of `display` to `public`, allowing us to call `display` when making an instance of `Derived`.

### Using for Template Aliases

We can use `using` for creating aliases to template instantiations, making code more concise.

```C++
#include <iostream>
#include <unordered_map>
#include <string>

// Create a template alias for a hash table
template <typename Key, typename Value>
using HashTable = std::unordered_map<Key, Value>;

int main() {
    // Use the alias for a more readable type definition
    HashTable<std::string, int> ageMap;
    ageMap["Alice"] = 30;
    ageMap["Bob"] = 25;

    for (const auto& entry : ageMap) {
        std::cout << entry.first << ": " << entry.second << std::endl;
    }

    return 0;
}
```

In this example, we create a template as,

```C++
template <typename Key, typename Value>
```

This `template` is generally used above a `class`, however, in this example we are using it above our `std::ordered_map` creation. When using a template, we instantiate it with `<` and `>`.

Hence,

```C++
template <typename Key, typename Value>
using HashTable = std::unordered_map<Key, Value>;
```

allows the creation of `HashTable` using `HashTable<type1, type2>` where `type1` is replaced to `Key` and `type2` to `Value`.

Because of `using HashTable = std::unordered_map<Key, Value>;` we can now create instances such as `HashTable<std::string, int> ageMap;`.

### `using` with `enum`

C++20 introduced a new feature called `using enum` to import all enumeration constants into the current scope.

```C++
enum class Color { Red, Green, Blue };

int main() {
    using enum Color;
    Color c = Red; // No need to prefix with Color::
    return 0;
}
```