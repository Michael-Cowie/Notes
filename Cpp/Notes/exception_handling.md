<div align="center">
  <h1>  Exception Handling </h1>
</div>

The general syntax for C++ exception handling is,

```C++
try {
    ...
    throw exception; // Throw Exception
} catch (ExceptionType e1) {
    ...             // Catch Block
}
```

When an exception that is desired to be handled is detected, it is thrown using the `throw` statement in one of the following forms.

```C++
throw (exception);
throw exception;
throw; // Used for rethrowing an exception.
```

The operand object `exception` may be of any type, including constants. It is also possible to throw objects not intended for error handling.

# Catch All

In such situations where we cannot anticipate the correct exception type, we can use a mechanism to catch all exceptions. This can be achieved by defining the `catch` statement using ellipsies (`...`) as follows,

```C++
catch (...) {
    
}
```

# Specifying Exceptions in Functions

It is possible to restrict a function to `throw` only certain specified exceptions. This is achieved by adding a `throw` list clause to the function definition. The general form of using an exception specification is,

```C++
type function(arg list) throw (type list)
{

}
```