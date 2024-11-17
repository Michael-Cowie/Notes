<div align="center">
  <h1> Lambda Functions </h1>
</div>

C++ Lambda expression allows us to define anonymous function objects which can either be used inline or passed as an argument.

A basic lambda expression can look like,

```C++
auto helloWorld = []() {
  std::cout << "Hello World";
};
```

Here,

- `[]` - is called the **lambda introducer** which denotes the start of the lambda expression. You will pass variables into here that are defined outside the lambda function to allow access to them, otherwise the lambda function will not have access.
- `()` - is called the **parameter list** which is similar to the `()` operator of a normal function.

The following is an example passing a string,

```C++
    auto helloWorld = [](const std::string& name) {
        std::cout << "Hello " << name; // Output the string
    };

    helloWorld("Michael"); // Call the lambda with a string literal
```

#### Return Types

Like with normal functions, C++ lambda expressions can also have a return type. The compiler can implicitly deduce the return type of the lambda expression based on the `return` statement(s). But for multiple `return` statements of different types, we have to explicitly define the type. For example,

```C++
auto operation = [](int a, int b,  string op) -> double {
  if (op == "sum") {
    // returns integer value
    return a + b;
  } 
  else {
    // returns double value
    return (a + b) / 2.0;
  }
};
```

Notice the code `-> double` above. This explicitly defines the return type as `double`, since there are multiple statements which return different types based on the value of `op`. So no matter what type of value is returned by the various return statements, they are all explicitly converted to `double` type.

#### Lambda Clause `[]`

By default, lambda functions cannot access variables of the enclosing function. In order to access those variables, we use the capture clause.

In this example, I allow my lambda function to access the variable `my_name`,

```C++
const std::string& my_name = "Michael";

auto helloWorld = [my_name]() {
    cout << "Hello " << my_name;
};

helloWorld();
```

Here, `[my_name]` allows the lambda to access the `my_name` variable. If we remove `my_name` from the capture clause, we will get an error since `my_name` cannot be accessed from the lambda body.

Lambda clauses can also use pass by reference, 

```C++
std::string my_name = "Michael";

auto helloWorld = [&my_name]() {
    cout << "Hello " << my_name << endl;
    my_name = "A new name";
};

helloWorld();
helloWorld();
```

Will output,

```
Hello Michael
Hello A new name
```