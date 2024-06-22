# Generator Expressions

Generator expressions are evaluated during build system generation to produce information specific to each build configuration. They have the form `$<...>` and can be broken down into three main categories `Logical Expressions`, `Informational Expressions` and `Output Expressions`. This is a quick reference for generators and for more indepth explanation of each method [the main documentation](https://cmake.org/cmake/help/latest/manual/cmake-generator-expressions.7.html) is required.

Generator expressions are allowed in the context of many target properties, such as LINK_LIBRARIES, INCLUDE_DIRECTORIES, COMPILE_DEFINITIONS and others. They may also be used when using commands to populate those properties, such as `target_link_libraries()`, `target_include_directories()`, `target_compile_definitions()` and others.

This means that they enable conditional linking, conditional definitions used when compiling, and conditional include directories and more. The conditions may be based on the build configuration, target properties, platform information or any other queryable information.

# Logical Expressions

Logical expressions are used to create conditional output. The basic expressions are the 0 and 1 expressions. A `$<0:...>` results in the empty string, and `<1:...>` results in the content of `...`. They can also be nested.

For example,

- `$<0:...>`
  - Empty string (ignores `...`)
- `<$<1:...>` 
  - Content of `...` 

Keep in mind this is not entirely true for some string comparison expressions, for example.

- `$<STREQUAL:a,b>`
  - `1` if `a` is STREQUAL `b`, else `0` 

likewise with

- `$<CXX_COMPILER_ID:comp>`
  - `1` if the CMake-id of the CXX compiler matches `comp`, otherwise `0`.

Other logical expressions exist, such as OR,

- `$<OR:condition1, condition2, ..., conditionN>` - These are the conditions that are evaluated. If any one of these conditions is true, the OR expression returns true.

As an example, I will break down the following command,

```CMake
$<$<OR:$<CONFIG:Release>,$<CONFIG:RelWithDebInfo>>:/Gw>
```

1. `$<...>` - This syntax indicates a generator expression
2. `$<OR:...>` - This expression is a logical OR operator. It returns true if any of its arguments are true. This allows for combining multiple conditions.
3. `$<CONFIG:Release>` - This expression checks if the current build configuration is `Release`. It evaluates to true if the build configuration is `Release`.
4. `$<CONFIG:RelWithDebInfo>` - This expression checks if the current build configuration is `RelWithDebInfo`. It evaluates to true if the build configuration is `RelWithDebInfo`.
5. Combining to `$<OR:$<CONFIG:Release>,$<CONFIG:RelWithDebInfo>>` - This expression combines the two previous configuration checks using the OR operator. It evaluates to true if either the `Release` or `RelWithDebInfo` configuration is active.
6. Now, let's pretend OR was evaluated to `true`, this means it will be combined to - `$<1:/Gw>`, which means the string `/Gw` will be passed. It is did not, it will be evaluated to `$<0:/Gw>`, which fails the original logical expression and an empty string is passed.

Therefore, this is interpreted as "For a `Release` or `RelWithDebInfo` build, pass the flag `/Gw`"

# Informational Expressions

These expressions expand to some information. The information may be used directly, eg:

```CMake
include_directories(/usr/include/$<CXX_COMPILER_ID>/)
```

expands to `/usr/include/GNU/` or `/usr/include/Clang/` etc, depending on the Id of the compiler.

These variables used inside the generator are CMake variables and cannot be custom made. Therefore, the list of variables are available on the online documentation.

# Output Expressions

These expressions generate output, in some cases depending on an input. These expressions may be combined with other expressions for information or logical comparison:

- `$<JOIN:list,...>`
  - Joins the list with the content of `...` 
- `$<BUILD_INTERFACE:...>`
  - Content of `...` when the property is exported using `export()`, or when the target is used by another target in the same buildsystem. Expands to the empty string otherwise. 
- `$<UPPER_CASE:...>`
  - Content of `...` converted to upper case. 