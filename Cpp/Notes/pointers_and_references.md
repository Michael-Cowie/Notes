<div align="center">
  <h1> Pointers and References</h1>
</div>

When a variable is declared, the memory needed to store its value is assigned a specific location in memory (its memory address). Generally, C++ programs do not actively decide the exact memory address where its variables are stored. Fortuneately, that task is left to the environment where the program is run - generally, an operating system decides the particular memory locations on runtime. However, it may be useful for a program to be able to obtain the address of a variable during runtime in order to access data cells that are at a certain position relative to it.

## Address-of operator (&)

The address of a variable can be obtained by preceding the name of a variable with an ampersand sign `&`, known as **address-of-operator**, e.g.

```C++
foo = &myvar;
```

This would assign the memory address of the variable `myvar` to `foo`. By preceding the name of the variable `myvar` with the **address-of operator**, we no longer assigning the teont of the variable itself to `foo`, but rather it's memory address.

The actual address of a variable in memory cannot be known before runtime, but let's assume, in order to help clarify some concepts, that `myvar` is placed during runtime in the memory address 1776. In this case, consider the following code fragment.

```
myvar = 25;
foo = &myvar;
bar = myvar;
```

The values contained in each variable after the execution of this are shown in the following diagram.

![images](images/reference_operator.png)

First, we have assigned the value 25 to `myvar` (A variable whose address in memory we assumed to be 1776). <br>
The second statement assigns `foo` the address of `myvar`. <br>
Finally, the third statement assigns the values contained in `myvar` to `bar`. This is a standard assignment operation.

The main difference between the second and third statements is the appearance of the **address-of operator** (&).

The variable that stores the address of another variable (like `foo` from above) is what in C++ is called a **pointer**.

## Dereference operator (*)

An interesting property of pointers is that they can be used to access the variable they point to directly. This is done by preceding the pointer name with the **dereference operator (*)**. The operator itself can be read as "The value pointed to by".

Therefore, following with the values of the previous example above;

```C++
baz = *foo;
```

This can be read as "`baz` is equal to the value pointed to by `foo`". The statement would actually assign the value 25 to `baz`, since `foo` is 1776 and the value located at 1776 would be 25.

```
baz = foo;   // baz equal to foo (1776)
baz = *foo;  // baz equal to value pointed to by foo (25)  
```

The reference and dereference operators are thus complementary <br>
& is the **address-of operator**, and can be read simply as "address of" <br>
\* is the **dereference operator**, and can be read simply as "value pointed to by" <br>

## Declaring pointers

Due to the ability of a pointer to directly refer to the value that it points to once dereferenced, the type needs to be known. For that, the declaration of a pointer needs to include the data type the pointer is going to point to. The declaration of pointers follow this syntax,

```C++
type * name;
```

where `type` is the data type pointed to by the pointer. This type is not the pointer itself, but the type of the data the pointer points to, e.g.

```C++
int * number;
char * character;
double * decimals;
```

These are three declarations of pointers. Each one is intended to point to a different data type, but, infact all of them are pointers and all of them are likely going to occupy the same amount of memory space (the size in memory of a pointer depends on the platform where the program runs).

Note that the asterik (*) used when declaring a pointer only means that it is a pointer (it is part of its type compound specifier) and should not be confused with the **dereference operator** seen earlier.

When declaring multiple pointers on the same line, it is important to remember the asterisk (*) for each pointer definitions, e.g.

```C++
int * p1, * p2;
```

This is required due to the precedence rules. Note that if, instead, the code was,

```C++
int * p1, p2;
```

`p1` would indeed be of type `int *` but `p2` would be of type `int`. 

## Pointers and Arrays

The concept of arrays is related to that of pointers. In fact, arrays work very much like pointers to their first elements, an array can always be implicitly converted to the pointer of the proper type.

```C++
int myarray [20];
int * mypointer;
```

The following assignment operation would be valid,

```
mypointer = myarray;
```

After that, `mypointer` and `myarray` would be equivalent and would have very similar properties. The main difference being that `mypointer` can be assigned a different address, whereas `myarray` can never be assigned anything, and will always represent a block of 20 elements of type `int`. Therefore, the following assignment would not be valid,

```C++
myarray = mypointer;
```

## Pointer Arithmatic

Inside `arrays.md`, the brackets ([]) were explained as specifying the index of an element. Well, infact these brackets are a dereferencing operator known as **offset operator**. They dereference the variable they follow just as *, but they also add the number between the brackets to the address being deferenced.

```C++
a[5] = 0;      // a [offset by 5] = 0
*(a + 5) = 0;  // pointed to by (a + 5) = 0
```

These two expressions are equivalent and valid, not only if `a`, but also if `a` is an array, its name can be used just like a pointer to its first element.

Adding 3, will increase the memory address location by `3 * sizeof(type)` not by exactly 3.

## Void pointers

The `void` type of pointer is a special type of pointer. In C++, `void` represents the absence of type. Therefore, `void` pointers are pointers that pointer to a value that has no type (and thus also an undetermined length and undetermined dereferencing properties).

This gives `void` pointers a great flexibility, by being able to point to any data type, from an integer value or a float to a string of characters. In exchange, they have great limitation. The data pointed to by them cannot be directly dereferenced (which is logical, since we have no type to dereference to), and for that reason, any address in a `void` pointer needs to be transformed into some other pointer type that points to a concrete data type before being dereferenced. An example usage could be,

```
#include <iostream>

int main()
{
    int a = 5;
    
    void * void_pointer = &a;
    int * int_pointer = (int *) void_pointer;

    std::cout << *int_pointer << std::endl;
    return 0;
}
```

`void *` is often used in places where you need to be able to work with different pointer types in the same code.

## Invalid pointers and null pointers

In principle, pointers are meant to point to valid addresses, such as the addresses of a variable or the address of an element in an array. But pointers can actually point to any address, including addresses that do not refer to any valid element. Typical examples of this are **uninitialized pointers** and pointers to nonexistent elements of an array.

```C++
int * p;                 // Uninitialized pointer (local variable)

int myarray[10];
int * q = myarray + 20;  // Element out of bounds
```

Neither `p` or `q` point to addresses known to container a value, but none of the above statements cause an error. In C++, pointers are allowed to take any address value, no matter whether there actually is something at that address or not. What can cause an error is to dereference such a pointer (i.e. actually the value they point to). Accessing such a pointer causes undefined behaviour, ranging from an error during runtime to accessing some random value.

However, sometimes, a pointer really needs to explicitly point to nowhere, and not just an invalid address. For such cases, there exists a special value that any pointer type can take, the **null pointer value**. This value can be expressed in C++ in two ways; either with an integer value of 0, or with the `nullptr` keyword.

```C++
int * p = 0;
int * q = nullptr;
```

Here, both `p` and `q` are **null pointers**, meaning that they explicitly pointer to nowhere and they both actually compare equal. All **null pointers** compare equal to other **null pointers**. It isalso quite usual to see the defined constant `NULL` be used in older code to the **null pointer** value,

```C++
int * r = NULL;
```

## Pointers to a function

C++ allows operations with pointers to functions. The typical use of this is for passing a function as an argument to another function. Pointers to functions are declared with the same syntax as a regular function declaration, except that the name of the function is enclosed between parentheses `()` and an asterisk `(*)` is inserted before the name. The act of calling it performs the dereference, therefore we do not need to dereference it to call the function.

```C++
#include <iostream>

int add(int a, int b)
{
    return a + b;
}

int main()
{
    int x = 100;
    int y = 200;
    
    int (* add_pointer)(int, int) = add;
    std::cout << add_pointer(x, y) << std::endl;
    return 0;
}
```

## Passing a pointer to a function

Pointers are stored on the heap, not the stack. This means if we dereference the passed pointer to a function we change the value in the memory, i.e. if we change the value inside a function, it will change it to any variable that points to the same memory location that is outside of the local stack.

```C++
int change_to_5(int *p)
{
    return *p = 5;
}

int main()
{
    int a = 100;
    cout << a << endl;
    change_to_5(&a);
    cout << a << endl;
    return 0;
}
```

Hence, the value of `a` is changed to `5` after passing the memory address location to `change_to_5`.

# References

C++ introduces a new kind of variable known as the **reference variable**. A reference variable provides an alias (alternative name) for a previously defined variable. A reference is not a variable as a variable is only introduced by the declaration of an object. An *object* is a region of storage and in C++ references do not (necessarily) take up any storage.

When a variable is declared as a reference, it becomes an alternative name for an existing variable. A variable can be declared as a reference by putting ‘&’ in the declaration type. Because a reference variable is an alias to another variable, it is important to know that changing the reference will change the value of the variable too.

```C++
#include <iostream>

int main()
{
    int x = 10;

    int& ref = x; // ref is a reference to x
    
    ref = 20;     // Value of x is now changed to 20
    std::cout << "x = " << x << '\n';
    return 0;
}
```


## Modifying the parameter of a function as a reference

Similar to pointers, if the parameter to the function is passed as a reference, changing the parameter will change the value outside of the function, **it is not a change to the local stack**. When passing a variable to the function that is receiving it as a reference variable, you do not need to do anything specific, for example if it was a pointer you may need to utilize the address-of operator (&).


```C++
#include <iostream>

void set_value_to(int& param, int to)
{
    param = to;
}

int main()
{
    int x = 10;
    std::cout << "x = " << x << std::endl;
    set_value_to(x, 50);
    std::cout << "x = " << x << std::endl;
    return 0;
}
```
## Function returning a reference

A function can also return a reference.

```C++
int & max(int &x, int &y)
{
    if (x > y)
        return x;
    else
        return y;
}
```

Since the return type of `max()` is `int &`, the function returns a reference to `x` or `y` (and **NOT the values**). Then a function call such as `max(a, b)` will yield a reference to either `a` or `b` depending on their values. This means that this function call can appear on the left-hand side of an assignment statement, e.g. `max(a, b) = -1;` is legal and assigns `-1` to `a` if it is larger, otherwise `-1` to `b`.



# Key Differences

1. A pointer **can be re-assigned**

```C++
int x = 5;
int y = 6;
int *p;
p = &x;
p = &y;
*p = 10;
assert(x == 5);
assert(y == 10);
```

A reference **cannot be re-bound** and must be **bound at initialization**.

```C++
int x = 5;
int y = 6;
int &q; // error
int &r = x;
```

2. A pointer variable has its own identity. A pointer has a distinct, visible memory address that can be taken with the unary `&` operator and a certain amount of space that can be measured with the `sizeof` operator. Using those operators on a reference returns a value corresponding to whatever the reference is bound to; the references own address and size are invisible. Since the reference assumes the identity of the original variable in this way, it is convenient to think of a reference as another name for the same variable.

```C++
int x = 0;
int &r = x;
int *p = &x;
int *p2 = &r;

assert(p == p2); // &x == &r
assert(&p != &p2);
```

3. You can have arbitrarily nested pointers to pointers offering extra levels of indirection. References only offer one level of indirection.

```C++
int x = 0;
int y = 0;
int *p = &x;
int *q = &y;
int **pp = &p;

**pp = 2;
pp = &q; // *pp is now q
**pp = 4;

assert(x == 2);
assert(y == 4);
```

4. A pointer can be assigned `nullptr`, whereas a reference must be bound to an existing object. If you try hard enough, you can bind a reference to a `nullptr`, but this is undefined and will not behave consistently. You can, however, have a reference to a pointer whose value is `nullptr`.

5. Pointers can iterate over an array, you can use `++` to go to the next item that a pointer is pointing to, and `+4` to go to the 5th element. This is no matter what size the object is that the pointer points to.

6. A pointer needs to be dereferenced with `*` to access the memory location it points to, whereas a reference can be used directly. A pointer to class/struct uses `->` to access its members whereas a reference uses a `.`.

7. References cannot be put into an array, whereas points can be.

8. Const references can be bound to temporaries. Pointers cannot (not without some indirection):

```C++
const int &x = int(12); // legal C++
int *y = &int(12); // illegal to take the address of a temporary.
``` 
This makes `const &` more convenient to use in argument lists and so forth.


# Using Pointerss with Arrays and Strings

Pointers are one of the efficient tools to access elements of an array. Pointers are useful to allocate arrays dynamically, i.e. we can decide the array size at run time. To achieve this, we can use functions, namely `malloc()` and `calloc()`.

In general, there are some differences between pointers and arrays. **Arrays refer to a block of memory space, whereas pointers do not refer to any sectin of memory**. The memory addresses of arrays cannot be changed, whereas the content of the pointers variable, such as the memory addresses that it refers to, can be changed.

Note: There is no error checking of array bounds in C++ Suppose we declare an array of size 25. The compiler issues no warnings if we attempt to access the 26th element. It is the programmers task to check the array limits.


We can declare the pointers to arrays as follows:

```C++
int* nptr;
nptr = numbers[0]
```

or 

```C++
nptr = number;
```

Keep in mind that `nptr` is an implicit conversion and equivalent to,

```C++
nptr = &number[0]
```

A pointer does not point to an array, it will always point to an element in the array, not the array itself.


# Pointer Expressions and Pointer Arithmatic

There are a substantial number of arithmatic operators that can be performed with pointers. C++ allows poiinters to perform the following arithmatic operations,

- A pointer can be incremented with `++` and decremented with `--`
- Any integer can be added to or subtracted from a pointer
- One pointer can be subtracted from another

Here, the pointer `aptr` refers to the base address of the variable `a`.

```C++
int a[6];
int* aptr = &a[0];
```

We can increment the pointer variable from here, e.g.

```C++
aptr++;
aptr--;
```

This statement moves the pointer to the next memory address and then subsequentally brings it back.

We cannot perform pointer arithmatic on variables which are not stored in contiguous memory locations.