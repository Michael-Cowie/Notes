<div align="center">
  <h1> Files Types </h1>
</div>

When programming in Python, we will be exposted to multiple file types. Some common file types are `.py`, `.pyc` and `.pyd`, other more uncommon file types could be `.pyi` and `.pyw`. I will define a series
of common file types that I have been exposted to the most when developing with Python.

## .py

`.py` files are the standard Python source code files. They contain the actual Python code written in plain text. You write your Python code in `.py` files and execute them using the Python interpreter. An example
code snippet could be, 

```Python
print("Hello World")
```

## .pyc

`.pyc` files are compiled bytecode files created by the Python interpreter. When a `.py` file is executed, the interpreter compiles the source code into bytecode, which is a lower-level representation of the code. The bytecode is then stored in `.pyc` files for faster execution in subsequent runs. The presence of `.pyc` files helps improve the startup time of Python scripts. If you import a module, python will build a `.pyc` file that contains the bytecode to make importing it again later easier (and faster). It contains the compiled version of Python source code, which is platform-independent and can be executed directly by the Python interpreter without the need for further compilation.

It is important to note that the contents of a `.pyc` file are not intended to be human-readable. They are binary files that store the bytecode representation of the corresponding `.py` file. The contents will
then not open up nicely in a text editor as they do not follow a text based encoding. Opening it will show jumbled text such as ` d dlmZmZ d `.



## .pyd

These are Windows-specific dynamic-link library (DLL) files containing compiled Python code written in C/C++. They are binary extensions used to provide performance optimizations or access to external libraries. `.pyd` files are similar to `.pyc` files in that they contain compiled code, but they are specific to Windows and serve as dynamic libraries. Python provides a mechanism to create extension modules, which are modules written in C or C++ that can be imported and used in Python code. These extension modules can be compiled into binary files with the extension `.pyd` on Windows.

An example small code snippet could be,

```C
#include <Python.h>

// Function that adds two numbers
static PyObject* add_numbers(PyObject* self, PyObject* args)
{
    int num1, num2;
    if (!PyArg_ParseTuple(args, "ii", &num1, &num2))
        return NULL;
    
    int result = num1 + num2;
    return Py_BuildValue("i", result);
}
```
When this C/C++ code is compiled into a `.pyd` file (on Windows), it can be imported and used as a Python module. For example:

```Python
import my_module

result = my_module.add_numbers(5, 10)
print(result)  # Output: 15
```
Thus, a `.pyd` file does not contain code written in Python syntax like a `.py` file does. Instead, it contains compiled C or C++ code that can be imported and used as a module within Python. The Python/C API is utilized to interface between the Python interpreter and the compiled code in the `.pyd` file. It was a file format used before Python 3.5 for `.pyc` files that were created with optimizations (-O) flag.

## .pyo

`.pyo` files are optimized bytecode files generated by certain versions of the Python interpreter. The optimization process includes removing unnecessary details and performing various optimizations to improve runtime performance. However, `.pyo` files are not commonly used or generated in modern Python versions.

## Wheels (`.egg`, `.whl`, ...)

Python wheels will typically contain the extension `.egg` and `.whl`. This is explained further inside of [my existing notes for them](https://github.com/Michael-Cowie/Notes/blob/main/Python/Notes/PyPI_PIP_Wheel.md).
