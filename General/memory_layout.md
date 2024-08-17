# Memory Layout

When a program is executed, it is loaded into the memory with a specific structure, which includes the following segments,

```
+-------------------------+ High Memory Address
|       Command Line      |  <-- Command-line arguments
|       Environment        | <-- Environment variables
+-------------------------+
|          Stack          |  <-- Local variables, function call information
|           |             |
|           v             |
|     (grows downward)    |  <-- As new frames are added, stack grows downward
+-------------------------+
|           ^             |
|           |             |
|          Heap           |  <-- Dynamic memory allocation
|     (grows upward)      |  <-- As new objects are allocated, heap grows upward
+-------------------------+
|    Uninitialized Data   |  (BSS) <-- Uninitialized global and static variables
+-------------------------+
|     Initialized Data    |  <-- Initialized global and static variables
+-------------------------+
|          Code           |  <-- Program instructions
+-------------------------+ Low Memory Address

```

This memory layout represents the virtual memory layout for a single process (a running program). Each process is given its own virtual address space by the operating system. The memory layout described is part of the virtual address space for a single process. 

When you run multiple programs, each has its own virtual memory layout, but all these virtual layouts are mapped to the shared physical memory (RAM). The OS uses page tables to map [virtual address](https://github.com/Michael-Cowie/Notes/blob/main/General/virtual_memory_addresses.md) to physical addresses. Virtual memory pages from different processes can be mapped to different physical memory pages.

```
+------------------------------------------+
|   Process A Virtual Address Space        |
|                                          |
| Stack, Heap, Data, ...                   |
+------------------------------------------+

+------------------------------------------+
|   Process B Virtual Address Space        |
|                                          |
| Stack, Heap, Data, ...                   |
+------------------------------------------+

+------------------------+
|    Physical Memory     |
|                        |
| [RAM] 32GB Total       |
|                        |
| +--------------------+ |
| | OS and Kernel      | |
| +--------------------+ |
| | Process A Pages    | |
| +--------------------+ |
| | Process B Pages    | |
| +--------------------+ |
| | Free Memory        | |
+------------------------+
```

The virtual address space of a process encompasses all these segments and is the conceptual view of memory that the process sees. Each segment exists within this virtual address space.



# Command Line Arguments and Environment Varibales

#### Command Line Arguments

When a program is executed, it can receive command-line arguments. These arguments are stored in memory and for C they're accessible through the `argc` (argument count) and `argv` (argument vector) parameters of the `main` function.

```C
int main(int argc, char* argv[]) {
    // argc: number of arguments
    // argv: array of argument strings
}
```

#### Environment Variables

Environment variables provide a way to affect the behaviour of running processes. They are stored in memory and can be accessed using functions like `getenv`.

```C
#include <cstdlib>
#include <iostream>

int main() {
    const char* path = std::getenv("PATH");
    if (path != nullptr) {
        std::cout << "PATH: " << path << std::endl;
    }
}
```

# Stack

The stack is a region of memory that stores local variables, function parameters, return addresses, and control flow information. The stack operates in a Last In, First Out (LIFO) manner. 

#### Structure

When a function is called, a stack frame is created and pushed onto the stack. The stack frame contains the functions local variables, parameters, return addresses and possibly other bookkeeping information.

When a function returns, the stack frame is popped off the stack and the control is transferred back to the calling function.

#### Growth Direction

The stack grows downwards, this means that as new stack frames are added (pushed), they occupy lower memory addresses. Conversely, as stack frames are removed (popped), the stack "shrinks" back towards higher memory addresses.

```
+-----------------------+ High Memory Address
|      Older Frames     |  (Higher part of the stack)
+-----------------------+
|     Current Frame     |
+-----------------------+
|     Newer Frames      |  (Lower part of the stack)
+-----------------------+ Low Memory Address

```

# Heap

The heap is a region of memory used for dynamic memory allocation. Memory in the heap must be manually managed by the programmer using `new` and `delete` in C++.

#### Structure

When you allocate memory dynamically using `new`, it is taken from the heap. When you deallocate memory using `delete`, it is returned to the heap and can be reused.

#### Growth Direction

The heap grows upwards. This means that as new memory is allocated, it occupies higher memory addresses. Conversely, as memory is deallocated, the heap can shrink back towards lower memory addresses.

```
+-----------------------+ High Memory Address
|      Free Space       |  (Available for future allocations)
+-----------------------+
|     Newer Objects     |  (Allocated later, toward higher addresses)
+-----------------------+
|     Older Objects     |  (Allocated earlier, toward lower addresses)
+-----------------------+ Low Memory Address


```

Heap space is managed manually. Failure to deallocate memory can lead to memory leaks. More flexible than stack memory but can lead to fragmentation if not managed properly.

# Data Segment

The data segment is divided into two parts, Initialized Data Segment and Uninitialized Data Segment (BSS).

#### Initialized Data Segment

Stores global and static variables that are initialized, e.g.

```C++
int globalVar = 10;
```

#### Uninitialized Data Segment (BSS)

Stores global and static variables that are uninitialized. The BSS (Block Started by Symbol) segment contains variables that are declared but not initialized in the source code. These variables are zero-initialized by the runtime environment before the program starts executing.

```C++
int globalVar; // Stored in BSS segment
static int staticVar; // Stored in BSS segment
```

The BSS segment is typically larger in embedded systems or older systems, where memory efficiency is crucial.


# Text Segment (Code Segment)

This section contains the compiled machione code of the program. This segment is generally read-only to prevent accidental modification of the instructions.

# Processes

Each process has its own independent memory space. The code, data, heap and stack are all isolated from other processes. This isolationm provides security and stability but comes at the cost of higher memory usage and slower inter-process communication.

# Threads

Threads within the same process share the same memory space. This includes sharing the code, data and heap segments. Threads have **their own stack segment but share the address space for the heap and global variables**.

Each threads has its own stack. This allows threads to execute independently with their own local variables and function call information.

Since threads share the same memory space, communication between threads is more efficient than between processes. However, this also means that threads must synchronize access to shared resources to prevent race conditions and data corruption.