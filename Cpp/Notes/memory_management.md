<div align="center">
  <h1> Memory Management </h1>
</div>

C uses `malloc()` and `calloc()` functions to allocate memory dynamically at run time. Similarily it uses the function `free()` to free dynamically allocated memory. We use dynamic allocation techniques when it is not known in advance how much of memory space is needed. Although C++ supports these functions, it also defines two unary operators `new` and `delete` that perform the task of allocating and freeing the memory in a better and easier way. Since these operators manipulate memory on the free store, they are also known as free store operators.

An object can be created  by using `new` and destroyed by using `delete` as when required. A data object created inside a block with `new` will remain in existence until it is explicitly destroyed by using `delete`. Thus, the lifetime of an object is directly under our control and is unrelated to the block structure of the program. In C++, when you use the `new` operator to allocate memory, this memory is allocated in the application's heap segment. Hence, because `new` adds object onto the heap it is important to remember to `delete` it or memory leaks will occur.


## Creating

The `new` operator can be used to create objects of any type. It takes the following general form: `pointer_variable = new data_type`.

Here, `pointer_variable` is a pointer of type `data_type`. The `new` operator allocates sufficient memory to hold a data object of type `data_type` and returns the address of the object. The data_type may be any valid data type. The `pointer_variable` holds the address of the memory space allocated. For example, `int *p = new int`, following by `*p = 25`;

We can also initialize the memory using the `new` operators. This is done as follows, 

`pointer_variable = new data_type(value);`

`int *p = new int(25);`

As mentioned earlier, `new` can be used to create a memory space for any data type including user-defined types such as arrays, structures and classes. The general form for a one-dimensional array is: `pointer_variable = new data_type[size]`. Here, size specifies the number of elements in the array. `int *p = new int[10]` creates a memory space for an array of 10 integers.

When creating multi-dimensional arrays with `new`, the first dimension must be a variable whose value is supplied at runtime. All others must be constants. `array_ptr = new int[10][19][3];`.

What happens if sufficient memory is not available for allocation? In such cases, like `malloc()`, `new` returns a `null` pointers. Therefore, it may be good idea to check for the pointer produced by `new` before using it, e.g.

```C++
    int *p  = new int;
    if (!p) 
    {
        cout << "allocation for p failed \n";
    }
```

The `new` operator offers the following advantages over the function `malloc()`

- It automatically computes the size of the data object. We do not need to use the operator `sizeof`
- It automatically returns the correct pointer type, so that there is no need to use a type cast
- It is possible to initialize the object while creating the memory space
- Like any other operator, `new` and `delete` can be overloaded

## Destroying

When a data object is no longer needed, it is destroyed to release the memory space for reuse. The general form of its use it `delete pointer_variable`. If we want to free a dynamically allocated array, we must use the following form of `delete`, `delete [size]pointer_variable;`. The size specifies the number of elements in the array to be freed. The problem with this form is that the programmer should remember the size of the array. Recent versions of C++ do not require the size to be specified, e.g. `delete []p;` will delete the entire array pointed to by p.

