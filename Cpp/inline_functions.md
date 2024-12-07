<div align="center">
  <h1>  Inline Functions </h1>
</div>

One of the objectives of using functions in a program is to save some memory space, which becomes appreciable when a function is likely to be called many times. However, every time a function is called, it takes a lot of extra time in executing a series of instructions for tasks such as jumping to the function, saving registers, pushing arguments into the stack and returning to the calling function. **When a function is small, a substantial percentage of execution time maybe spent in such overheads.**

One solution to this problem is to use macro definitions, popularly known as macros. Preprocessor macros are popular in C. The major drawback with macros is that they are not really functions and therefore, the usual error checking does not occuring during compilation.

C++ has a different solution to this problem. To eliminate the cost of calls to small functions, C++ proposes a new feature called inline functions. **An inline function is a function that is expanded in line when it is invoked.** That is, the compiler replaces the function code (Something similar to macro expansions). The inline functions are defined as fllows,

```C++
inline function-header
{
    function body
}
```

e.g.

```C++
inline double cube(double a)
{
    return (a * a * a)
}
```

The above inline function can be invoked by statements such as,

```C++
a = cube(3.0);
b = cube(2.5 + 1.5);
```

Usually, the functions are made inline when they are small enough to be defined in one or two lines, e.g.

```C++
inline double cube(double a){return (a * a * a);}
```

# When to NOT use inline functions

Some situations where inline expansion may not work are:

- For functions returning values, if a loop, switch or a goto exist.
- For functions not returning values, if a return statement exists.
- If functions contain static variables.
- Inline function is recursive.

# Note

Inline expansion makes a program run faster because the overhead of a function call and return is eliminated. However, it makes the program to take up more memory because the statements that define the inline function are reproduced at each point where the function is called. So, a trade-off becomes necessary.