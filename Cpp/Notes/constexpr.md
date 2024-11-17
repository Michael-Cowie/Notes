<div align="center">
  <h1> constexpr </h1>
</div>

`constexpr` is a keyword used to declare a variable or a function as "constant expression." A constant expression is an expression whose value can be **computed at compile time, rather than at runtime**. This feature allows the compiler to evaluate the expression during compilation, which can lead to performance improvements and more opportunities for optimizations. For example, if we were performing a calculation with a series of `constexpr`, the value will be calculated at compile time and not runtime.

When you declare a variable with `constexpr`, you are telling the compiler that the value of the variable can be determined at compile time. This means the variable's value is constant and cannot change during the program's execution. It's important to note that only certain types and expressions are allowed in `constexpr` variables.

You can also declare functions as `constexpr`, indicating that they can be evaluated at compile time when their arguments are known at compile time. Like `constexpr` variables, `constexpr` functions should have a deterministic behavior and operate on constant expressions.

```C++
constexpr int square(int x) {
    return x * x;
}

int main() {
    constexpr int side = 5;            // side will be evaluated at compile time
    constexpr int area = square(side); // square(side) will also be evaluated at compile time

    // Other code...
    return 0;
}

```

Keep in mind that there are some limitations when using `constexpr`. For example, `constexpr` functions must have a body that can be evaluated at compile time, which means they cannot contain certain constructs like loops or non-constexpr function calls. Additionally, `constexpr` variables and functions must have a deterministic value that can be determined at compile time.