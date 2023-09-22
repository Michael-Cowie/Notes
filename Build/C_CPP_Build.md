# Compilation Process

We write our Code as simple text, but we need some way to transform this text into an application that our computer can actually understand and run. When going from text form to an actual executeable binary we basically have two main operations that need to happen. 

The compilation of a C++ program involves three steps.

1. **Preprocessing:** The preprocessor takes a C++ source code file and deals with the `#include`s, `#define`s and other preprocessor directives. The output of this step is a *pure* C++ file without pre-processor directives.
2. **Compilation:** The compiler takes the pre-processor's output and produces an object file from it. What the compiler actually needs to do is take our text file and convert them into an intermediate format called an **object file**.
3. **Linking:** The linker takes the object files produced by the compiler and produces either a library or an executeable.

# Preprocessing

The preprocessor handles the *preprocessor directives*, like `#include` and `#define`. It is agnostic of the syntax of C++, which is why it must be used with care.

It works on one C++ source file at a time by replacing `#include` directives with the content of the respective files (which is usually just declarations), doing replacement of macros (`#define`), and selecting different portions of text depending of `#if`, `#ifdef` and `ifndef` dirctives. When we have something like `#define <iostream>` the contents of `iostream.h` are **literally** being copied from `iostream.h` and being placed directly into your file, which is why the file size of the file increases considerably after the preprocessing stage, it is being the contents inside of `iostream.h` are so large.

For example, if we have a `EndBrace.h` with the only contents being
```
}
```
and use it as,

```C++
int Multiply(int a, int b){
    return a * b
#include "EndBrace.h"
```
This would compile successfully, because all the compiler did it take the `}` from `EndBrace.h` and place it directly where we had `#include "EndBrace.h"`

The preprocessor works on a stream of preprocessing tokens. Macro substitution is defined as replacing tokens with other tokens (the operator `##` enables merging two tokens when it makes sense).

After all this, the preprocessor produces a single output that is a stream of tokens resulting from the transformations described above. It also adds some special markers that tell the compiler where each line came from so that it can use those to produce sensible error messages.

Some errors can be produced at this stage with clever use of `#if` and `#error` directives.

If you wish to see the preprocessed files, they can be viewed using `cpp hello.c > hello.i`

# Compilation

The compilation step is performed on each output of the preprocessor. The compiler parses the pure C++ source code (now without any preprocessor directives) and converts it into **assembly code**. Then invokes underlying back-end (assembler in toolchain) that assembles that code into **machine code** producing actual binary file in some format (ELF, COFF, a.out, ...). This object file contains the compiled code (in binary form) of the symbols defined in the input. Symbols in object files are referred to by name.

Object files can refer to symbols that are not defined. This is the case when you use a declaration, and don't provide a definition for it. The compiler doesn't mind this and will happily produce the object file as long as the source code is well-formed.

Compilers usually let you stop compilation at this point. This is very useful because with it you can compile each source code file separately. The advantage this provides is that you don't need to recompile *everything* if you only change a single file.

The produced object files can be put in special archives called static libraries, for easier reusing later on.

It's at this stage that *regular* compiler errors occur, like syntax errors or failed resolution errors are reported.

If you wish to see the assembly code, this can be done using the previous output of the preprocessed files via `gcc -S hello.i`. The contents of `hello.s` **contain assembly code**.

The assembler (`as.exe`) converts the **assembly code into machine code**. The machine code will be inside of `hello.o`. This can be come from the command `as -o hello.o hello.s`. Therefore an object file is a computer file containing object code, that is, machine code output of an assembler or compiler.

Because object files are machine code, they have therefore been targeted for a specific CPU and a specific Operating System, but are **not a complete executeable**.

# Linking

The linker is what produces the final compilation output from the object files the compiler produced. This output can be either a static, shared (or dynamic) library or an executeable.

 Linking refers to the process of combining multiple compiled object files or libraries into a single executable or shared library. When you write a C++ program, you typically divide it into multiple source files (`.cpp` files). Each source file is separately compiled into an object file (`.o` or `.obj` file), which contains machine code instructions for that specific part of the program. These object files may also reference functions or symbols defined in other object files or libraries. It checks that all functions and symbols referenced in one file are defined in another, and it resolves these references by including the necessary code from other object files or libraries into the final binary.

![](./images/linking.png)