# What is a Pointer?

A pointer is a variable that **stores the memory address** of another variable. Pointers are declared using the `*` symbol, and they must be initialized before use.

```C++
int x = 10;
int* ptr = &x;  // ptr points to the address of x
```

In this example:

- `x` is an integer variable
- `&` gives the memory address of `x`
- `int* ptr` declares `ptr` as a pointer to an integer

# Pointer Operators

- `&` (Address-of operator) - Returns the memory address of a variable.
- `*` (Dereference operator) - Accesses the value at the address held by the pointer.

```C++
int y = 20;
int* ptr = &y; // Address of y
int value = *ptr; // Dereferences ptr to get the value at that address (20)
```

# Common Types of Pointers

- **Null Pointer (`nullptr`)** - Points to no valid memory location, used to indicate a pointer that is intentionally not pointing to any object. 

```C++
int* ptr = nullptr;
```

- **Void Pointer(`void*`)** - A pointer that can point to any data type. It must be cast to the appropiate type before dereferencing.

```C++
void* ptr;
int x = 10;
ptr = &x;  // Can point to any data type

// Cast ptr to int* and then dereference it
std::cout << *static_cast<int*>(ptr) << std::endl;
```

1. `void* ptr;` can point to any data type, but it cannot be directly dereferenced.
2. To use `ptr`, we cast it to the appropiate type, `int`, and then dereference it.
3. `*static_cast<int*>(ptr)` converts `ptr` to `int*` and then dereferences it to get the integer value.

- **Dangling Pointer** - A pointer that refers to a memory location that has already freed or deleted. Accessing it leads to undefined behaviour.

# Dynamic Memory Allocation

C++ allows you to dynamically allocate memory using `new` and `delete`.

```C++
int* ptr = new int(5);  // Dynamically allocate an integer with value 5
delete ptr;             // Free the allocated memory
ptr = nullptr;          // Avoid dangling pointer by resetting to nullptr
```

and for Arrays,

```C++
int* arr = new int[10]; // Allocate array of 10 integers
delete[] arr;           // Free memory for array
arr = nullptr;
```

# Pointer Arithetic

You can perform arithmetic on pointers to navigate through memory, but this is only useful within arrays and should be done with caution.

```C++
int arr[5] = {10, 20, 30, 40, 50};
int* ptr = arr;  // Points to arr[0]
*(ptr + 1);      // Accesses arr[1]
```

# Error-Prone Mistakes with Pointers

### **Dangling Pointers**

A dangling pointer occurs when an object is deleted or goes out of scope, but a pointer still points to the memory it occupied.

```C++
int* ptr = new int(10);
delete ptr;      // ptr is now dangling
```

In this example, `ptr` still holds the address, but the memory is invalid. To resolve this issue, reset the pointer to `nullptr` after deleting it.

### Memory Leaks

Memory leaks occur when dynamically allocated memory is not freed but lose the ability to free it. This happens if you lose all pointers to an allocated memory block.

```C++
void leak() {
    int* ptr = new int(10);
}
```

In the example above, when we leave the local stack for `leak`, we lose the reference to `ptr` and cannot call `delete`. Therefore, the memory was not freed and cannot be deleted. This means, memory is continually being occupied when `leak` is cannot and resulting in filled RAM.

### Double Delete

Deleting the same pointer twice results in undefined behaviour.

```C++
int* ptr = new int(10);
delete ptr;
delete ptr; // Undefined behavior, can crash the program
```

### Uninitialized Pointers

An uninitialized pointer points to a random memory location, which can lead to crashes or unexpected behaviour.

```C++
int* ptr;   // Not initialized, contains garbage address
*ptr = 10;  // May cause a crash or undefined behavior
```

Always initializer pointers, even if it's to a `nullptr`.

# Smart Pointers

Smart pointers in C++ are advanced pointers that help manage the memory of dynamically allocated objects by automatically controlling the objects lifetime. Unlike raw pointers, which require explicit `delete` calls to free memory, smart pointers ensure that the memory is released as soon as the pointer is no longer in use. This approach reduces the risk of memory leaks and other errors such as dangling pointers and double deletion.

Smart pointers are part of the C++ Standard Library (Since C++11) and include,

1. `std::unique_ptr`
2. `std::shared_ptr`
3. `std::weak_ptr`

### `std::unique_ptr`

`std::unique_ptr` is a smart pointer that maintains unique ownership of a dynamically allocated object. No two `std::unique_ptr` instances can manage the same object simultaneously. Once a `std::unique_ptr` goes out of scope, **the object it points to is automatically deleted**.

Ownership can be transferred to another `std::unique_ptr` using `std::move`, but copying is not allowed.

```C++
#include <iostream>
#include <memory>

int main() {
    std::unique_ptr<int> ptr = std::make_unique<int>(42); // initializes to 42
    
    std::cout << "Value: " << *ptr << std::endl;

    std::unique_ptr<int> newPtr = std::move(ptr); // Transferring ownership to another unique_ptr
    if (!ptr) {
        std::cout << "ptr is now nullptr after move." << std::endl;
    }

    std::cout << "New pointer value: " << *newPtr << std::endl; // newPtr now owns the resource

    return 0;
}
```

In the example above,

- `ptr` initially owns the integer with a value of `42`.
- Ownership is transferred from `ptr` to `newPtr` using `std::move`, and `ptr` is set to `nullptr`.
- The managed resource is automatically deleted when `newPtr` goes out of scope.
- No need to call `delete` on `newPtr`, memory is automatically released when `newPtr` goes out of scope. This happens because the destructor is called implicitly when leaving scope.

### `std::shared_ptr`

`std::shared_ptr` is a smart pointer that provides shared ownership of a dynamically allocated object. Multiple `std::shared_ptr` instances can manage the same object, and the object will only be deleted when the last `std::shared_ptr` owning it is destroyed.

Key features include,

1. **Reference Counting**  - `std::shared_ptr` maintains a count of how many `shared_ptr` instances are managing the object.

2. **Automatic Deletion** - When the reference count reaches zero, the managed object is automatically deleted.

```C++
#include <iostream>
#include <memory>

int main() {
    std::shared_ptr<int> ptr1 = std::make_shared<int>(100);

    {
        // Create `ptr2` in a scope
        std::shared_ptr<int> ptr2 = ptr1;
        std::cout << "ptr1 and ptr2 are sharing the value: " << *ptr1 << std::endl;
        std::cout << "Reference count: " << ptr1.use_count() << std::endl; // Outputs 2
    } // `ptr2` goes out of scope; only `ptr1` remains

    std::cout << "Reference count after ptr2 is out of scope: " << ptr1.use_count() << std::endl; // Outputs 1
    return 0;
}
```

- `ptr1` is a `shared_ptr` managing an integer with the value `100`.
- `ptr2` is created as a copy of `ptr1` using the copy constructor, sharing ownership of the same integer.
- When `ptr2` goes out of scope, the reference count decreases.
- When `ptr1` goes out of scope, the reference count reaches zero, and the memory is automatically freed.

### `std::weak_ptr`

`std::weak_ptr` is a non-owning smart pointer that references an object managed by a `std::shared_ptr`. It does not increase the reference count, which prevents cyclic references that could lead to memory leaks when using `shared_ptr`s together.

Because `std::weak_ptr` does not contribute to the reference count, it will not prevent the resource from being deleted.

```C++
#include <iostream>
#include <memory>

int main() {
    std::shared_ptr<int> ptr1 = std::make_shared<int>(200);

    // Create a weak_ptr from shared_ptr
    std::weak_ptr<int> weakPtr = ptr1;

    std::cout << "Reference count (with weakPtr): " << ptr1.use_count() << std::endl; // Outputs 1, weakPtr doesn't increase count
    return 0;
}
```

# Best Practices

1. **Use Smart Pointers** - Prefer `std::unique_ptr` and `std::shared_ptr` over raw pointers to avoid manual memory management.

2. **Avoid Dangling Pointers** - After `delete`, set pointers to `nullptr`. Then at a later point, use `if (ptr) {` to avoid dereferencing a `nullptr`.

3. **Be Cautious with `new` and `delete`** - Always pair every `new` with a `delete`.

4. **Initialize Pointers** - Always initialize pointers, either to `nullptr` or a valid memory address.

5. **Use `nullptr` Over `NULL`** - `nullptr` is strongly typed and preferred over `NULL`.