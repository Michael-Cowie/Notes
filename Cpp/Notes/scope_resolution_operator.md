<div align="center">
  <h1> Scope Resolution Operator </h1>
</div>

`::` is known as the scope resolution operator. The scope resolution operator is used to help resolve issues with scoping and can be used in various ways. When writing code, variables, classes and so forth are defined in scopes. When writing variables into a function for example, the variables "scope" is inside the function. When declaring variables are the top of a file, the variables scopes is the "Global" scope. The following are examples for utilize the scope resolution operator.

1 - Access a class inside another class

```C++
 class A
 {
    ...
    class B
    {
        static int var;
    }
 }

 int x = A::B::var;
```

2 - Access to a global variable when there is a local variable with same name. Using `::` with nothing specified to the left of it, means the *global* scope.

```C++
int gval = 5;
{
    int gval = 10;
    int y = ::gval;  //the value assign for y is 5
}
```

3 - To access to a static variable inside a class.

```C++
 class A
 {
    static int x;
 };

 int y = A::x;
```

4 - When using from multiple inheritance.

```C++
class A
{
   protected:
     int l;
}

class B
{
   protected:
     int l;
}

class C: class A, class B
{
   public:
    int f()
    {
       int c1 = A::l;
       int c2 = B::l;
    }
}
```

5 - Namespaces

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

cout << NS1::NS2::m; << endl;
```

6 - Defining Class functions

It is very common for a header file to declare a class member function and have it defined outside of the header file. This means the header file will be `#include ...` in other files.

```C++
#include <iostream>

using namespace std;

class Example
{
    public:
        Example(int m);     // Declaration
};

Example::Example(int m) // Definition
{
        cout << "Calling the constructor with " << m << endl;
}

int main()
{
    Example e(100);
}
```

Here, the SRO will be used to find the function `Example` defined inside the scope `Example`. This is crucial because it is valid to define a function in the global scope. Simply calling `Example(100);` will look for any definiton in the global scope, here, we are telling the compiler to look into the scope `Example` and define the function `Example`.

#### Example

```C++
::mediapipe::Status RunMPPGraph()
```

`RnuMMPGraph` is a function taking zero arguments and returning `::mediapipe::Status`. `Status` is a type defined in the `mediapipe` namespace which is defined in the global namespace.

#### Example

To access an STL iterator, you need a scope resolution operator and not the `.` operator.


 Hence,

```C++
vector<int>::iterator my_iterator;
```

and not

```C++
vector<int> numbers;
numbers.iterator;
```


Dot and arrow (`->`) operators are used to access all data (member variables, functions) that is specific to the given instance.

Scope resolution operator is used to access all data (static member variables, static functions, types) that is specific to the given type, not instance. Note that member types are never instance-specific so you will always use `type::member_type` to access them.

Hence, because `vector<int>` (and `vector<int>::iterator`) is a type, not a variable, the scope resolution operator is used.