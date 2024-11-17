<div align="center">
  <h1> Namespaces </h1>
</div>

We have been defining variables in different scopes in C++ programs, such as classes, functions, blocks, etc. ANSI C++ standard has added a new keyword `namespace` to define a scope that could hold global identifiers. The best example of namespace scope is the C++ Standard Library. All classes, functions and templates are declared within the namespace named `std`. That is why we have been using the directive,

```C++
using namespace std;
```

in our programs that use the standard library. The `using namespace` statement specifies that the members defined in `std` namespace **are moved to the global namespace** and will be used frequently throughout the program. `cout` and `cin` are frequent examples of this and they're objects (not functions) defined inside the `std` namespace. Here are their declarations as defined by the C++ standard.

Header `<iostream>` synopsis,

```C++
#include <ios>
#include <streambuf>
#include <istream>
#include <ostream>

namespace std {
    extern istream cin;
    extern ostream cout;
    extern ostream err;
    ...
}

```

Hence, these two lines are frequently used together,

```C++
#include <iostream>

using namespace std;

...
```


# Defining a Namespace

We can define our own namespace in our programs. The syntax for defining a namespace is similar to the syntax for defining a class,

```C++
namespace namespace_name
{
    // Declaration of variables,
    // functions, classes, etc...
    ...
}
```

e.g.

```C++
namespace TestSpace
{
    int m;
    
    void display(int n)
    {
        cout << n << endl;
    }
}
```

Here, the variable `m` and the function `display` are inside the scope defined by the `TestSpace` namespace. If we want to assign a value to `m` we must use the scope resolution operator (`::`), as shown below.

```C++
TestSpace::m = 100;
```

This approach becomes cumbersome if the members of a namespace are frequently used. In such cases, we can use a `using` directive to simplify their access. This can be done in two ways,

```C++
using namespace namespace_name;    // using directive
using namespace_name::member_name; // using declaration
```

In the first form, all the members declared within the specified namespace may be accessed without using qualification. In the second form, we can access only the specified member in the program.

```C++
using namespace TestSpace;
m = 100;       // OK
display(200);  // OK
```

and

```C++
using TestSpace::m;
m = 100;       // OK
display(200);  // NOT OK, display not visible
```

# Nesting Namespaces

A namespace can be nested within another namespace.

```C++
namespace NS1
{
    ...

    namespace NS2
    {
        int m = 100;
        ...
    }
}
```

To access the variable  `m` we must qualify the variable with both the enclosing namespace names.

The statement,

```C++
cout << NS1::NS2::m; << endl;
```

will display the value of `m`. Alternatively, we can write

```C++
using namespace NS1
cout << NS2::m; << endl;
```

# Namespaces in multiple files

namespaces can be used alongside different files and essentially "shared". For example, if I include a 
namespace from `.hpp` and create my own namespace with the same name within a `.cpp`, I use utilize
the definitions from inside the namespace inside the `.hpp`. Namespaces do not have to be unique per
file. A minor example sharing a namespace could be,

```C++
#include <iostream>

using namespace std;

namespace MyExample {
    int a = 5;
}

namespace MyExample {
    int b = a + 10;
}

int main()
{
    
    cout << MyExample::b << endl; // 15
    return 0;
}
```

# Unnamed Namespaces

An unnamed namespace is one that does not have a name. Unnamed namespace members occupy global scope and are **accessible in all scopes following the declaration in the file**. We can access them without using any qualification.

A common use of unnamed namespace is to shield global data from potential name conflicts between files. Every file has its own, unique unnamed namespace.

Having something in an anonymous namespace **means it is local of this translation unit** (The `.cpp` file and its includes), this means that if another symbol with the same name is defined elsewhere there will not be a violation of the One Definition Rule (ODR).

All anonymous namespaces in the same file are treated as the same namespace and all anonymous namespaces in different files are distinct. An anonymous namespace is the equivalent of,

```C++
namespace __unique_compiler_generated_identifier {
    ...
}

using namespace __unique_compiler_generated_identifier;
```
