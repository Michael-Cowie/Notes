# Argument Parsing from the CLI

When we execute a script from the command line it is possible to enter command line argument. This is not related to Python, it is related to scripting languages. However, in this tutorial I will be focusing on the Python library `argparse` in order to create command line arguments for a script.

The following code snippet creates a file called `arg_parser.py` and accepts
the arguments created by `add_argument`.

```Python
"""
The argparse is used to get command line arguments when executing a script.

Example usages:

python arg_parser.py -h

python arg_parser.py -w 5 --height 10

python arg_parser.py --width 10 --height 10 -v

python arg_parser.py -w 10 -H 10 -q

python3.exe arg_parser.py -w 10 -H 10 -a cats -l dogs dogs2 -a cats2
"""


import math
import argparse

"""
-w is the shorthand version
--width is the long version (required)

Without required=True, the argument will be defauted to `None`
"""
parser = argparse.ArgumentParser(description='Calculate area of the rectangle')
parser.add_argument('-w', '--width', 
                    type=int, 
                    required=True, 
                    help='Width of rectangle')
# -h is required for help, therefore -H is used..
parser.add_argument('-H', '--height', 
                    type=int, 
                    required=True, 
                    help='Height of rectangle')

"""
action=store_store automatically creates a default value of `False`

With mutually exclusive groups, only one can be specified at a time,
i.e. `python arg_parser.py -w 10 -H 10 -q -v` will throw an error.
"""
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='Print quietly')
group.add_argument('-v', '--verbose', action='store_true', help='Print verbose')

"""
To give an undetermined amount of parameters for a single variable you need
to utilize the `nargs` option or the `append` setting of the `action` option,
depending on how you want the user interface to behave.
"""
parser.add_argument(
    '-l', '--list',
    nargs='+', # '+' takes 1 or more arguments, '*' takes zero or more.
    help='Test variable that takes 1 or more values using nargs'
)

parser.add_argument(
    '-a', '--append',
    action='append', # '+' takes 1 or more arguments, '*' takes zero or more.
    help='Test variable that takes 1 or more values using nargs'
)

# With `append` you provide the option multiple times to build up the list.
# e.g. # python arg.py -a 1234 -a 2345 -a 3456 -a 4567
args = parser.parse_args()

def area_of_rectangle(width, height):
    return width * height

if __name__ == '__main__':
    area = area_of_rectangle(args.width, args.height)
    if args.quiet:
        print(area)
    elif args.verbose:
        print(f"The area of the rectangle with width: {args.width} and " \
        f"height: {args.height} is {area}")
    else:
        print(f"Area of rectangle = {area}")
        
    print("Values using -l", args.list)
    print("Values using -a", args.append)
```

# Syntax for arguments

The following file `input_file.py` takes one input,

```Python
import argparse

parser = argparse.ArgumentParser('Retrieve an input file')
parser.add_argument('-I', '--input_file',
                    type=str,
                    required=True)

args = parser.parse_args()

# If both a single dash and a double dash exist, argparse will always use the double dash into the parse_args()
print(args.input_file)
```

When executing the script from the command line, their are multiple variations in which we can specify the input file,

```Bash
python input_file.py -I input.txt

python input_file.py -I=input.txt

python input_file.py -Iinput.txt

python input_file.py -I"input.txt"

python input_file.py "-Iinput.txt"
```

It's not uncommon for command line arguments to accept no spaces but still be valid, for example the common CMake parameter `-D` is used often as,

```
cmake .. -G "Visual Studio 19 2022" -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake
```

This is using the `-D` argument and setting it to `CMAKE_TOOLCHAIN_FILE` and is equivalent to,

```
cmake .. -G "Visual Studio 19 2022" -D CMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake
```