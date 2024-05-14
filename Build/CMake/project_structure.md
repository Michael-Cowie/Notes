# CMake Project Structure

## Libraries (With optional executables)

A standard CMake project structure would contain,

- **CMakeLists.txt** - The top-level CMake file defines the project and sets up global configurations. It also includes options to build the library.

- **cmake/** - Contains CMake modules like `FindLibrary.cmake` to locate and configure **external libraries** and scripts like `CompilerFlags.cmake` to manage compiler options.

- **include/library_name/** - Holds the public headers for the library. The `library_name` directory should match the namespace or logical grouping of the library.

- **src/** - Contains the source files for the library. `library_source.cpp` is an example source file. The `CMakeLists.txt` file here defines the library target using `add_library`.

- **apps/** - If the project includes executables, this directory will contain their source files. This is conditionally included based on a CMake option. Here, the `CMakeLists.txt` will be responsible for calling `add_executable`.

- **tests/** - Include the test suite for the library. The `CMakeLists.txt` file sets up the testing framework and test targets.

- **docs/** - For the libraries documentation.

- **extern/** - Houses external dependencies, which can be included as Git submodules or other means.

The `apps/` directory is included conditionally, based on a CMake option that can be set by the user to determine whether they want to build the executables alongside the library. This makes the project flexible for users who might only need the library or those who also want to build and use the executables provided. 

A visual representation would be,

```
Library_Project/
│
├── CMakeLists.txt          # Top-level CMake configuration
│
├── cmake/                  # CMake modules and scripts
│   ├── FindLibrary.cmake   # Custom CMake module to find external libraries
│   └── CompilerFlags.cmake # Scripts to set compiler flags
│
├── include/             # Public header files
│   └── library_name/    # Directory for public headers
│       └── example.h    # An example header file
│
├── src/                   # Library source files
│   ├── CMakeLists.txt     # CMake configuration for the library
│   └── library_source.cpp # Source file for the library
│
├── apps/                # Optional executables (conditional inclusion)
│   ├── CMakeLists.txt   # CMake configuration for executables
│   └── app_source.cpp   # Source file for the executable
│
├── tests/               # Test code
│   ├── CMakeLists.txt   # CMake configuration for tests
│   └── test_source.cpp  # Source file for the tests
│
├── docs/                # Documentation sources
│
└── extern/              # External dependencies
    └── libexternal      # External library included as a submodule
```

## A Main Project

The structure described above is for a library, which includes the source code and headers necessary to build the library itself. For a typical C++ project that uses libraries rather than creating one, the structure would be slightly different and typically contain the follow directories,

- **CMakeLists.txt** - A top-level `CMakeLists.txt` file that would define the project and include global settings. It would also handle the inclusion of the libraries the project depends on.

- **include/** - This directory might not be necessary if the project doesn't export any headers, such as building a pure executable. If it does, it would contain those headers.

- **src/** - Contains the source files for the projects executables. The `CMakeLists.txt` in this directory would define the executable targets with `add_executable()`. The `src/` directory is focused on the project’s own source code, which is used to build the executables.

- **libs/** - This directory would contain them, each possibly with its own `CMakeLists.txt`. The `libs/` directory is optional and would only be present if the project includes its own libraries.

- **tests/** - Contains the test cases for the projects executables.

- **docs/** - For the projects documentation.

- **extern/** - External dependencies, often included as Git submodules. he `extern/` directory would contain the external libraries that the project uses, which could be included via `add_subdirectory()` commands in the `CMakeLists.txt` files.

A visual representation would be,

```
C++_Project/
│
├── CMakeLists.txt       # Top-level CMake configuration
│
├── cmake/               # CMake modules and scripts
│
├── src/                 # Project source files
│   ├── CMakeLists.txt   # CMake configuration for the project
│   └── main.cpp         # Main source file for the project's executable
│
├── libs/                # Optional internal libraries or modules
│   ├── CMakeLists.txt   # CMake configuration for libraries
│   └── lib/             # A directory for an internal library
│       ├── CMakeLists.txt # CMake configuration for this library
│       └── ...          # Source files and directories for the library
│
├── tests/               # Test code
│   ├── CMakeLists.txt   # CMake configuration for tests
│   └── test_main.cpp    # Source file for the tests
│
├── docs/                # Documentation sources
│
└── extern/              # External dependencies
```

## Key Differences

#### Purpose


- **Library Project** - Designed to create a reusable library that other projects can include and link against.

- **C++ Project** - Intended to create executables, possibly linking against external libraries.

#### Directory Structure

- **Library Project** - Includes an `include/` directory for public headers and a `src/` directory for source files that compile into the library.

- **C++ Project** - The `src/` directory contains source files for the projects executables. It may not need an `include/` directory if it doesn't provide headers for other projects to use.

#### `CMakeLists.txt`

- **Library Project** - The `CMakeLists.txt` will directives like `add_library()` to build the library and install targets for the headers. The library may optionally use `add_executable()` if the library

- **C++ Project** - The `CMakeLists.txt` will focus on `add_executable()` to build the projects executables and `find_package` or `add_subdirectory` to include external libraries.

#### Optional Components

- **Library Project** - May include an `apps/` directory if the library also provides executables, but this is optional and controlled by a CMake option.

- **C++ Project** - May include a `lib/` directory if the project contains its own libraries or modules, in addition to the main executables.

#### Build Options

- **Library Project** - Often includes options to build shared or static versions of the library, and to toggle the building of any provided executables.

- **C++ Project** - Focuses on build options related to the executables, such as selecting which ones to build ot setting application-specific configurations.

#### Usage of External Libraries

- **Library Project** - External libraries are usually linked privately, as they are dependencies of the library itself.

- **C++ Project** - External libraries are linked as needed by the executables and can be included in various ways depending on the projects requirements.

In summary, a library project is centered around creating a library, with a structure that supports the distribution of headers and the building of library files. A typical C++ project is more focused on creating executables, potentially using various libraries, and may not distribute headers at all unless it also includes library-like components. The CMake configurations reflect these purposes, with the library project emphasizing library creation and installation, and the C++ project emphasizing executable creation and linking against libraries.