<div align="center">
  <h1> __declspec </h1>
</div>

`__declspec` is a Microsoft-specific keyword used in C++ to apply specific attributes to a function or variable declaration. The most common use of `__declspec` is to specify how a function or variable should be exported or imported from a dynamic-link library (DLL).

The `__declspec(dllexport)` attribute specifies that a function or variable should be exported from a DLL, making it available to other programs that link to the DLL. This attribute is typically used in the header file of a library to declare the public interface of the library.

The `__declspec(dllimport)` attribute specifies that a function or variable should be imported from a DLL, rather than defined within the current program. This attribute is typically used in the header file of a program that links to a DLL.

Here's an example of how __declspec can be used in C++ taken from the CMake tutorial;

```cpp
#if defined(_WIN32)
#  if defined(EXPORTING_MYMATH)
#    define DECLSPEC __declspec(dllexport)
#  else
#    define DECLSPEC __declspec(dllimport)
#  endif
#else // non windows
#  define DECLSPEC
#endif

namespace mathfunctions {
    double DECLSPEC sqrt(double x);
}
```

In this example, the `DECLSPEC` macro is used to control the use of `__declspec(dllexport)` and `__declspec(dllimport)` based on whether the code is being built for Windows and whether the library is being built or used. The `sqrt `function is declared with the `DECLSPEC` macro, which ensures that the function is either exported or imported as appropriate.

In the CMake tutorial, `EXPORTING_MYMATH` was set via `target_compile_definitions(MathFunctions PRIVATE "EXPORTING_MYMATH")`. This means the `MathFunctions` library will have this variable set and export `sqrt`, however the libraries that link to it and import `MathFunctions.h` will not have this variable set and instead import `sqrt`.
