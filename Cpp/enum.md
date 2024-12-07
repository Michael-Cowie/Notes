<div align="center">
  <h1> enum </h1>
</div>

An enumeration is a user-defined data type that consists of integral constants. To define an enumeration, keyword `enum` is used.

```C++
enum Days {
    Monday, 
    Tuesday, 
    Wednesday, 
    Thursday, 
    Friday, 
    Saturday,
    Sunday
};
```

Here, the name of our enumeration is called `Days` and `Monday`, `Tuesday`, ... are values of type `enum Days`. By default `Monday` is 0, `Tuesday` is 1, and so forth. We can change the default value on an `enum` element during declaration.

It is important to note here that `Days` is not a scope, nor object. It is a type.

```C++
enum Days {
    Monday = 1, 
    Tuesday = 2, 
    Wednesday = 5, 
    Thursday = 10, 
    Friday, 
    Saturday, 
    Sunday
};
```

Here `Monday` is now assigned to the value of `1` alongside other values. `Friday` will always be the previous value + 1, hence `Friday` is `11`.

# Using the an `enum`

When you create an enumerated type, only blueprint for the variable is created. To construct an object, we can use the following approach.

```C++
int main()
{
    enum Days day;
    cout << day;
    return 0;
}
```


Here, a variable `day` is created, which is of type `enum Days`.

Here is another way to achieve the same result,

```C++
enum Days {
    Monday = 1, 
    Tuesday = 2, 
    Wednesday = 5, 
    Thursday = 10, 
    Friday, 
    Saturday, 
    Sunday
} day;
```

To assign it to a particular value simply assign it,

```C++
int main()
{
    enum Days day = Wednesday;
    cout << day;
    return 0;
}
```

The values inside of the `enum` will be defined and accessed without needing any dot operators, which is common in other programming languages. Keep in mind that because `enum Days` **is a type, you cannot use the . operator on it, such as Days.Monday**. You use the . operator on an *instance* of a class.

The variables are also created in a way where we do not need `::` to access them, illustrated below.

```C++
#include <iostream>

using namespace std;

class Qt 
{
    public:
        enum FocusPolicy {
            NoFocus = 0,
            TabFocus = 1
        };
};



int main(){
    cout << Qt::TabFocus; // Not Qt::FocusPolicy::TabFocus
    return 0;
}
```

# `enum class`

C++ 11 has introduced `enum class` which aids in accessing values. C++ has two kinds of `enum`

1. `enum class`es
2. Plain `enum`s

Here are a couple of examples on how to declare them.

```C++
 enum class Color { red, green, blue }; // enum class
 enum Animal { dog, cat, bird, human }; // plain enum 
```

The key differences are,

1. `enum class`es - enumerator names are **local** to the enum and their values do not implicitly convert to other types (like another `enum` or `int`)
2. Plain `enum`s - where enumerator names are in the same scope as the enum and their values implicitly convert to integers and other types.

Here is an example illustrating the differences,

```C++
enum Color { red, green, blue };                    // plain enum 
enum Card { red_card, green_card, yellow_card };    // another plain enum 
enum class Animal { dog, deer, cat, bird, human };  // enum class
enum class Mammal { kangaroo, deer, human };        // another enum class

void fun() {

    // examples of bad use of plain enums:
    Color color = Color::red;
    Card card = Card::green_card;

    int num = color;    // no problem

    if (color == Card::red_card) // no problem (bad)
        cout << "bad" << endl;

    if (card == Color::green)   // no problem (bad)
        cout << "bad" << endl;

    // examples of good use of enum classes (safe)
    Animal a = Animal::deer;
    Mammal m = Mammal::deer;

    int num2 = a;   // error
    if (m == a)         // error (good)
        cout << "bad" << endl;

    if (a == Mammal::deer) // error (good)
        cout << "bad" << endl;

}
```

Therefore, `enum class` es should be preferred because they cause fewer surprises that could potentially lead to bugs due to additional typing support.

# `typedef` with `enum`s

It's a C heritage, in C, if you do,

```C
enum TokenType
{
    one = 1,
    two,
    ...
};
```

You will be able to use it by doing something as,

```C
enum TokenType foo;
```

but if you do it like this,

```C
typedef enum TokenType
{
    one = 1,
    two,
    ...
} TokenType;
```

We will be able to instead declare it as,

```C
TokenType foo;
```

As as are using `typedef` on `enum TokenType` to `TokenType`. In C++, you can use the former definition and use it as if it were in a C `typedef`. For example, in C++ we can have,

```C++
enum Result
{
    NOT_OK = 0;
    OK = 1;
}

Result func()
{
    return OK;
}
```