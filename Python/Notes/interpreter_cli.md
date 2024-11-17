<div align="center">
  <h1> Executing Python using a CLI </h1>
</div>

Let us begin from the beginning. When we type inside the console `python hello_world.py`, where is the `python` executeable found to run `hello_world.py`? Well, your "default" version is the **first one appearing in your path**. The so-called path is a list of directories your system searches for executeables. When you type a command, like `python`, this list is traversed from the first directory to the last, searching for a filename that matches the command you typed. If the filename/command is found, the matched file gets executed **without** taking into account potential later matches. This behaviour is by design. On UNIX systems the path environment variable is called `$PATH`, while on Windows system it's referred to as `%PATH%`

![](./images/environment_variables.png)

To find the *path* search for "environment variables" in Windows and click "Edit environment variables". The *path* variable will contain a list of directories, here we can add rows, where each row is a directory location. In my example, I have a `python.exe` inside of `%USERPROFILE\AppData\Local\Microsoft\WindowsApps`, this means when I run `python hello_world.py`, I am using the `python.exe` found in that directory.

# File locations using Windows CLI

The alternative approach (and much easier) to find where the interpreter is you're using is to use the Windows CLI command `where` and simply type `where python`. This will return the path to the `python.exe` that you're using.

When we install packages using `pip` it is also very helpful to find the locations of where we are placing the packages, i.e. the location of `site-packages`. This is also done using the command `pip list -v`. If multiple versions of Python are installed to the machine make sure the `pip` you're using is fetching packages and placing them inside the correct location, i.e. `where pip` is in the same zone a `where python`.

# Removing ambiguity when using multiple Python versions

It is not uncommon to have multiple Python versions installed on a single machine. For example, I have had *Python 2.7*, *Python 3.6*, *Python 3.9* and *Python 3.10* installed on a single machine and have had to switch versions to run older software source code. Now, this can become confusing when running from the CLI and typing `python hello_world.py`, we will almost certainly enter a scenario where we are executing mismatched versions and running into problems.

Suppose we then start a new project, where we want to use Python 3.9. We create a virtual environment called `.env` and activiate it. Typing `python` in a shell starts the 3.9 interpreter, **BUT** if you type `pip install <some-package>`, then, what version of `pip` is used? Is it the pip for the default version, i.e. the one in my `WindowsApps` directory from before, or the Python version within the virtual environment?

# The `-m` flag

An easy way to get around that ambiguity is simply to use `python -m pip install <some-package>`. The `-m` flag makes sure that you are using the `pip` **that is tied to the active Python executeable**. It is good practice to **always** use `-m`, even if you have just one global version of Python installed from which you create virtual environments.

The `python -help` will tell us that the `-m` flag `-m mod : run library module as a script`. However, what does it mean to run a library module as a script?

Let's compare the commands,

```Python
python -m pip install numpy
```

and

```Python
pip install numpy
```

First, let's go over `python -m pip install numpy` and understand what it means to "run a module as a script". In Python, a module `some_module` is typically imported into another Python file with a `import some_module` statement at the top of the importing file. This enables the use of functions, classes, and variables defined in `some_module` inside the importing file. To execute `some_module` as a script instead of importing it, you would define a `if __name__ == "__main__"` block inside the file. This block gets executed when running `python some_module.py` on the command line. This is useful because you **do not** want this code block to run when importing into other files, but you **do** want it run when invoked from the command line.

We can also create a directory or zipfile full of code and include a `__main__.py`. Then you can simply name the directory or zipfile on the command line and it will execute the `__main__.py` automatically. Hence, when inspecting our Python interpreter location and look at the `pip` inside of `site-packages`, this is what is being ran when using `python -m pip install numpy`. It is executing the `pip` Python source code.


![](./images/pip_1.png)

However, when using `pip install numpy` it is instead using `pip.exe`. This is instead found under `Scripts`. Remember that these locations can be found on which `pip` you will be using the bash command `where pip`. We do not want to accidentally use a `pip` and install to the wrong Python interpreter location and ideally want to use `pip -m pip` to know what we are using the module tied to our interpreter.

![](./images/pip_2.png)


# Site-packages

`site-packages` is the *target directory* of manually built Python packages. When you build and install Python packages from source, you will find the installed modules in `site-packages` by default. It is frequently a child directory of `Lib`. Packages are retrieved from the default PyPi server unless a custom PyPi server has been configured.

`site-packages` is by default part of the Python *search path*, so modules installed there can be imported easily afterwards. For example, if I were to perform `pip install numpy`, it will place `numpy` into the `site-packages` directory and because it is inside the Python *path* it can be imported as `import numpy`. The installed location can be shown using `pip list -v`.

If multiple Python versions are installed on the computer, to remove any ambiguity when executing commands from the CLI, it is worth finding the location of `python.exe` for the Python version you want to fetch the package for, open the CLI in that target directory and execute the command `python.exe -m pip install <some-package>` as stated above.
