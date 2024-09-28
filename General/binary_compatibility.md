# Binary Compatibility

Binary compatibility between files refers to the ability of compiled code (binaries) to work together without causing errors or crashes. Simply running on the same CPU architecture (e.g. x86, x86_64, ARM) is **necessary**, but **not sufficient** to ensure binary compatibility. The reason is that binary compatibilty depends on more than just the CPU architecture; it also involves:

1. Application Binary Interface (ABI) differences
2. Linking mechanisms
3. Memory Layout
4. Calling conventions
5. Runtime libraries

## CPU Architecture vs ABI

The CPU architecture defines the **instruction set** that the processor can execute. If binaries are compiled for the same architecture, they contain instructions that the CPU can understand. However, beyond the instruction set, there's the **ABI**, which is the contract between binaries that determines how data is passed between them, how function calls are made, and how system resources (.e.g memory and registers) are used.

### Application Binary Interface (ABI)

An ABI defines **how functions are called, how parameters are passed, how memory is managed, and how different data types are represented**. Even if two compilers generate code for the same CPU, their ABIs can differ, causing binaries from different compilers to be incompatible. These differences arise in,

1. **Calling conventions** - How function arguments are passed and return values are handled.
2. **Name mangling** - How C++ symbol names are transformed into binary labels.
3. **Memory layout and alignment** - How data is stored in memory.
4. **Exception handling** - How exceptions are propagated across the program.

### Example: MSVC and GCC (MinGW)

Microsofts MSVC compiler and GCC (often used with MinGW for Windows) generate binaries that target the same architecture, but they use **different ABIs**, key differences include

1. MSVC use a different calling convention than GCC (e.g., `__cdecl` vs `__stdcall`), which determines whether the caller or callee is 
responsible for cleaning the stack
2. Different data type sizes - For example, [GCC](https://stackoverflow.com/questions/7134547/gcc-printf-and-long-double-leads-to-wrong-output-c-type-conversion-messes-u) uses 16 bytes for a `long double`, while MSVC aliases it to `double` (8 bytes).
3. MSVC and GCC mangle C++ function names differently due to their distinct approaches to object-oriented features. This is probably the most known issue. C++ compilers need to decorate symbols so that (among many things) function overloading is possible. There is no standard name mangling scheme, so compilers choose their own, which causes incompatibility. This occurs because code compiled with MSVC might not recognize the names in a library compiled with GCC.
4. They also have different exception handling mechanisms (SEH for MSVC vs DWARF for GCC)

This is why mixing MSVC and MinGW binaries (e.g., Qt compiled with MinGW and linking it in MSVC) will cause linking errors or runtime failures.

## Linking Mechanisms

When a program is compiled, it often depends on external libraries (e.g., system libraries or third-party libraries). The compiled binary is linked with these libraries at either **compile time** (static linking) or **run time** (dynamic linking). The format of these libraries must be compatible with the programs binarys, or the binary will fail to execute or behave incorrectly.

Even if two binaries are compiled for the same architecture, if they are linked to libraries in different formats, they are incompatible. For example, binaries compiled on Linux (Using ELF) will not run on Windows (Which uses PE) even if they target the same CPU architecture.

## Memory Layout and Data Representation

Different compilers may handle the layout of objects and data types in memory differently. This involves,

1. **Padding** - The insertion of unused bytes to align data in memory for performance reasons.
2. **Endianness** - The byte order in which data is stored (although most modern architectures are little-endian).
3. **Struct Packing** - How structs (complex data types made up of smaller types) are laid out in memory. Some compilers may add padding between fileds to ensure efficient memory access.

If two compilers do not agree on the memory layout, accessing data in memory from one binary in another way may lead to errors or corrupted data.

Consider a `struct` like this in C,

```C
struct Example {
    char a;
    int b;
};
```

One compiler may add padding after `a` to align `b` on a 4-byte boundary (since `int` is typically 4 bytes). Another compiler might use a different padding straghety. If two binaries compiled with different compilers try to access this struct, they could read incorrect values.

## Calling Conventions

The calling convention defines how functions receive arguments and return values at the assembly level, as well as how the stack is cleaned up after a function call. Different compilers and even different settings within the same compiler can use different calling conventions.

Common calling conventions include,

1. **cdecl** - The caller cleans up the stack (used by GCC).
2. **stdcall** - The callee cleans up the stack (used by MSVC for certain Windows API functions).
3. **fastcall** - Some arguments are passed via registers for efficiency.

If one binary uses `cdel` and another uses `stdcall`, a function call between them will likely result in a crash or corrupted data, as the wrong party will attempt to clean up the stack.

## Runtime Libraries

Different compilers rely on different runtime libraries to provide essential functionality, such as memory allocation, file I/O and threading. Even if two binaries target the same architecture, if they link against different runtime libraries, they may not work together.

MSVC uses the Microsoft Visual C++ Runtime (`msvcrt.dll`) to handle things like heap memory management and I/O operations. MinGW on the other hand, links against its own runtime (`libgcc` and `libstdc++`). If an MSVC-compiled program tries to link dynamically against a MinGW-compiled library, there could be conflicts in runtime behaviour, leading to crashes or unexpected behaviour.

# Conclusion

For binaries to be compatible,

1. They must target the same CPU architecture
2. They must follow the same ABI (same calling conventions, symbol name mangling, etc...)
3. They must use compatible runtime libraries
4. They should handle memory layouts and object alignment consistently
5. They must use the same linking format.

If any of these requirements are not met, the binaries will not be compatible, even if they are for the same CPU architecture.

In practice, this means that binaries compiled with different compilers (e.g. MSVC and MinGW) are often incompatible and trying to mix them will lead to errors. For smooth integration, ensure that all components of a project are compiled with the same toolchain.
