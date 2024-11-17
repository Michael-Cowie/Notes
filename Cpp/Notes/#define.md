<div align="center">
  <h1> #define </h1>
</div>

The `#define` is part of the preprocessor language for C and C++. When they're used in code, the compiler just replaces the `#define` statement with whatever you want. For example, if you're sick of writing `for (int i = 0; i <= 10; i++)` often, you could be doing the following,

```C++
#include <iostream>

using namespace std;

#define fori10 for (int i = 0; i <= 10; i++)

int main()
{
    fori10 {
        cout << i << endl;
    }

    return 0;
}
```

Will output `1` to `10`.

# `typedef` vs `#define`

The "idea" is similar, but they're not the same.

- `#define` is a preprocessor token, the compiler itself will never see it.
- `typedef` is a compiler token, the preprocessor does not care about it.

You can use one or the other to (nearly, but not always) achieve the same effect, but it's better to use the proper one for your needs.

`typedef` obeys scoping rules just like variables, whereas `#define` stays valid until the end of the compilation unit (or until a matching `undef`).

Also, some things can be done with `typedef` that cannot be done with `#define`, 

```C++
typedef int* int_p1;
int_p1 a, b, c;      // a, b and c are all int pointers.

#define int_p2 int*  // Only the first is a pointer.
int_p2 a, b, c;
```

In the example with `#define`, only the first is a pointer. This is because `int_pt2` is replaced with `int*`, producing `int* a, b, c`. Remember that this is equivalent to,

```C++
int* a;
int b;
int c;
```

Therefore, these two statements are not equivalent. The asterisk belongs to the variable, not to the type.

However,

```C++
typedef int a10[10];
a10 a, b, c; // Creates three 10 integer arrays.
```