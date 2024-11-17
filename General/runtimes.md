# Table of Contents

1. [Runtimes](#runtimes)
2. [Compiled Languages (C, C++, ...)](#compiled-languages-c-c)
3. [Managed/Bytecode Languages (Java, ...)](#managedbytecode-languages-java)
4. [Interpreted Languages (Python, JavaScript, ...)](#interpreted-languages-python-javascript)
5. [Virtualized/Containerized Runtimes (Docker, ...)](#virtualizedcontainerized-runtimes-docker)


<div align="center">
  <h1>  Runtimes </h1>
</div>

A runtime environment **provides the necessary infrastructure for executing code, managing resources, and handling system calls**. It is used for various types of code, including interpreted languages (like Python or JavaScript), managed code (like Java or .NET), and compiled binaries. **Runtimes ensure that the code runs correctly** and efficiently on the target platform, regardless of how the code was originally written or compiled.

## **Compiled Languages (C, C++, ...)**

For compiled languages, a runtime environment often includes libraries, memory management and other system services that support the execution of binaries. This may be mimimal (e.g., C standard libraries) or extensive (e.g., the .NET runtime for .NET applications), depending on your language and application requirements.

At first glance, compiled executables (`.exe` files) seem "self-contained" because they consist of machine code instructions directly understood by the processor. Despite being "ready-to-run," executables rely on the runtime to ensure they function as intended within the larger software ecosystem. 

If you have an `.exe` and all required `.dll` files but no runtime installed, the program may fail to run because runtimes provide essential functionality. Even if the `.dll` files are present, they might depend on the runtime for initialization or other system-level tasks. Without the runtime, the program could crash, fail to start, or behave unpredictably, as critical dependencies and environment setups would be missing.

However, `.exe` files often make references to external libraries and rely on the runtime environment for them following reasons,

##### Dynamic Linking

When an `.exe` is dynamically linked, it doesn't include the complete implementation of every function it uses. Instead,

- The executable references symbols (e.g., `printf`) that are resolved by the runtime loader at execution time

- The loader finds the necessary shared libraries and maps them into memory

- Without the appropiate runtime or library versions, these dependencies cannot be resolved and the program fails.

##### Compiler-Specific Runtimes

**Different compilers generate binaries that depend on their specific runtime libraries**. An `.exe` compiled with MSVC might require the `MSVCR.dll` runtime for memory allocation, exception handling and standard C++ functions. Whereas, an `.exe` compiled with the intel compiler might depend on runtime libraries optimized for numerical computations or threading. These runtimes provide the concrete implementations of the abstracted functionality referenced in the binary.

##### Standard Library and System Abstractions

Even simple programs, such as `Hello, World` in C++ require runtime support. The program calls `std::cout` to output text, which is implemented in the C++ runtime library. File I/O, threading and other system-level features are delegated to the runtime or the operating system. Many compilers rely on

## Managed/Bytecode Languages (Java, ...)

Languages like Java compile to intermediate bytecode rather than machine code. These languages rely on runtime environments such as the Java Virtual Machine (JVM) to interpret and execute the bytecode, manage memory and perform tasks like garbage collection and just-in-time (JIT) compilation.

## Interpreted Languages (Python, JavaScript, ...)

In languages like Python and JavaScript, the runtime environment includes the interpreter and essential libraries that allow the code to be executed directly, rather than being compiled into a standalone binary. Here, the runtime is often the language interpreter. This is often Pythons CPython runtime or Node.js for JavaScript, which interprets and executes the code on the fly.

## Virtualized/Containerized Runtimes (Docker, ...)

In cloud-native or containized environments, a runtime may also refer to the minimal environment provided by containers provided by Docker to run applications. Containers package the runtime dependencies alongside the application, ensuring consistent behaviour across different environments.