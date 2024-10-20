# Why use Conan

Conan is a popular open-source C++ dependency manager. Its primary purpose is to simplify the process of managing dependencies in C++ projects. Dependency management is crucial in software development, especially in large-scale projects where codebase can quickly become complex and rely on numerous external libraries.

1. **Dependency Management** - Conan helps developers specify and manage the libraries and dependencies their C++ projects rely on. It allows developers to easily declare the dependencies their projects need and automatically handles the downloading, building and integration of those dependencies into the project.

2. **Build System Integration** - Conan is designed to integrate seamlessly with various build systems commonly used in C++ development, such as CMake, Makefiles, and others. This integration ensures that the dependencies managed by Conan can be easily incorporated into the build process of the project.

 3. **Package Management** - Conan operates on the concept of packages, which are pre-built and packaged versions of C++ libraries and dependencies. These packages can be shared and reused across projects, reducing the need to rebuild dependencies for each project and improving build times.

 4. **Cross-Platform Support** - Conan is designed to be cross-platform, meaning it can be used on different operating systems such as Windows, macOS, and Linux. This ensures consistency in dependency management across different development environments and platforms. This is entirely determined by the profile configuration.

 5. **Scalability and Flexibility** - Conan is suitable for projects of all sizes, from small personal projects to large enterprise-level applications. It offers flexibility in managing dependencies, allowing developers to specify precise versions and configurations for each dependency.

 The primary reason for the creation of Conan was to address the challenges and complexities associated with managing dependencies in C++ projects. Before tools like Conan, C++ developers often had to manually download, build, and configure dependencies, which could be time-consuming and error-prone. Conan streamlines this process, making dependency management more efficient and less error-prone, thereby improving productivity and reliability in C++ development.

 # Key Concepts of Conan

## Conan Center Index

The first thing to understand about Conan is where it retrieves from. When performing a command to install packages such as `conan install`, it will attempt to retrieve the binaries from the list of remotes specified under `conan remote list`. The default remote is called `conan` and points to the location `https://center.conan.io`. This means, `conan install` attempts to pull the binaries and recipe from this remote.

The main site https://conan.io/center is where you can traverse and see the currently available packages and versions to install.

 ## Packages

Packages are pre-built units containing libraries or dependencies managed by Conan. These packages are fetched from repositories, primarily the Conan Center Index, which hosts a vast collection of C++ packages. Packages (aka, dependencies) required for a project are specified inside a `conanfile.txt` file. For example,

```INI
[requires]
zlib/1.2.11
```

Will tell Conan to fetch `zlib` version `1.2.11` from the specified remote (Default being `conancenter`) with the matching profile. This will be done when using the command `conan install`.

## Conanfile

The Conanfile serves as the blueprint for defining dependencies, settings, and actions required to build a project. It can be in either `.txt` or `.py` format, detailing the project's requirements and build instructions.

A `conanfile.txt` will take on the format of an INI format.

```INI
[requires]
zlib/1.2.11

[options]
zlib:shared=True
```

Key flags to understand for a `conanfile.txt` are `[requires]`, `[generators]` and `[options]`.

- `[requires]` - This specifies the dependencies to be installed when running `conan install`. It supports versioning with the format `<Dependency>/<version>` and also supports ranges with `<dependency>/[>X,<Y]`.

- `[options]` - These are where we specify flags for the dependencies. It takes the format of `<dependency>:<option>=<flag>`. The list of options can be viewed inside the recipe file (`conanfile.py`) for the dependency within the conan-center-index. Here, we can see the options for [zlib](https://github.com/conan-io/conan-center-index/blob/master/recipes/zlib/all/conanfile.py#L22).

Generally speaking, the `conanfile.py` contains the instructions for taking raw source code, compiling it into a binary format, and then storing it in a compressed archive format (a “Conan Package”). Crucially, the `conanfile.py` also contains a list of other Conan Packages which are required for compilation, enabling authors to define a traditional “dependency tree” of Conan Packages. Thus, the Conan Package format and associated metadata are tailored for distribution and re-use as a dependencies in other Conan projects.

The `conanfile.py` will contain a single Class. Here, I will be observing the `zlib` `conanfile.py` [Class](https://github.com/conan-io/conan-center-index/blob/master/recipes/zlib/all/conanfile.py#L10).

```python
class ZlibConan(ConanFile):
    name = "zlib"
    package_type = "library"
    url = "https://github.com/conan-io/conan-center-index"
    homepage = "https://zlib.net"
    license = "Zlib"
    description = ("A Massively Spiffy Yet Delicately Unobtrusive Compression Library "
                   "(Also Free, Not to Mention Unencumbered by Patents)")
    topics = ("zlib", "compression")

    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
    }
    default_options = {
        "shared": False,
        "fPIC": True,
    }
```

Here, the Class contains the `options` that were specified inside the `conanfile.txt`. Additionally, some metadata. The methods inside the Class take the steps responsible to build the package. 

For each defined string in the `settings`, it must be an option and value defined inside the `settings.yml`.

- `requirements` - `zlib` is a library that does not need further dependencies, however the `requirements` method is used to define if a dependency is used via `self.require(<dependeyc>/<version>)`. An example can be seen in the `libtiff` [recipe](https://github.com/conan-io/conan-center-index/blob/master/recipes/libtiff/all/conanfile.py#L65).

```python
def requirements(self):
    if self.options.zlib:
        self.requires("zlib/[>=1.2.11 <2]")
```

- `source` - The `source` method is useful to override and customize the location of where you want the source code to be retrieved from. A useful override can be to retrieve a zipped copy of the source code from GitHub releases and unzip it using the Conan utility functions.

- `generate` - The `generate` method plays a crucial role of configuring CMake. Two crucial objects to understand that Conan utilizes within the `generate` method is both `CMakeToolChain` and `CMakeDeps`.

The `CMakeToolchain` is the toolchain generator for CMake. It will generate toolchain files that can be used in the command line invocation of CMake with the `-DCMAKE_TOOLCHAIN_FILE=<path>/conan_toolchain.cmake`. A toolchain refers to the tools used to perform a task. These tools can include the compiler, linker, etc... The `conan_toolchain.cmake` can be found in the  `build/generators` directory.

The `conan_toolchain.cmake` file is responsible for setting CMake variables (and many other tasks), such as,

```python
tc = CMakeToolchain(self)
tc.variables["variable"] = True
```

will have,

```cmake
set(variable "True" ...)
```

inside the generated `conan_toolchain.cmake`. Additional important toolchain information include,

```cmake
list(PREPEND CMAKE_PREPFIX_PATH ${CMAKE_CURRENT_LIST_DIR})
list(PREPEND CMAKE_PROGRAM_PATH C://.../.conan/data/<dependency>/.../bin)
list(PREPEND CMAKE_LIBRARY_PATH C://.../.conan/data/<dependency>/.../lib)
list(PREPEND CMAKE_INCLUDE_PATH C://.../.conan/data/<dependency>/.../include)
```

Inside these directories,

- The `bin` directory contains binary executables.
- The `lib` directory contains `.lib` files.
- The `include` directory contains header files.

It will always add `bin`, `lib` and `include` whether they are actually defined in the repository or not. Other notable variables are,

```cmake
set(CMAKE_INSTALL_PREFIX C://.../.conan/data/<dependency>/...)
```

Additionally, from the previous line

```cmake
list(PREPEND CMAKE_PREPFIX_PATH ${CMAKE_CURRENT_LIST_DIR})
```

The current working directory of the `conan_toolchain.cmake` is `build/generator`, i.e. the value of `CMAKE_CURRENT_LIST_DIR` is `build/generator`. `CMAKE_PREPFIX_PATH` is the directories to search for `find_package`, `find_program`, `find_library`, etc... This directory also contains the Conan generated `FindXXX.cmake` and config files. Conan generated `FindXXX.cmake` files are placed into the `build/generator` folder. The Conan generated `FindXXX.cmake` is used to specify the location to find the dependencies. Conan will install a dependency and place it inside of `.conan/data/<dependency>/...` and the generated Conan `FindXXX.cmake` will be added to the `build/generator` folder which is searchable because the location is added to the `CMAKE_PREPFIX_PATH` value.

The `CMakeDeps` generator produces the necessary files for each dependency to be able to use the CMake `find_package` function and locate the dependencies, e.g.

```python
self.requires("hello/0.1")
```

allows,

```cmake
find_package(hello REQUIRED)
```

The `CMakeDeps` is intended to run with the `CMakeToolchain` generator. It will set `CMAKE_PREFIX_PATH` and `CMAKE_MODULE_PATH` to the right folder (The generators folder) so CMake can locate the generated config/module files. Generated config/find files contain default target names which may not necessarily match the repository. For example,

Inside of the `libtiff` [repository](https://github.com/libsdl-org/libtiff/blob/master/libtiff/CMakeLists.txt#L165) it uses the target called `LERC::LERC`. When generating the `FindLERC.cmake`, it defaults the name to `lerc::lerc` and may necessary match the usages of it, such as `add_library(lerc::lerc)` . This means, it can be necessary to change it from `lerc::lerc` to `LERC::LERC`. This will be done using Conan utilies, primarily,

```python
deps.set_property("lerc", "cmake_target_name", "LERC::LERC")
```

will change,

```cmake
add_library(lerc::lerc ...)
```

to,

```cmake
add_library(LERC::LERC ...)
```

in this example it is necessary to match the usages of it. It should be noted when using Conan generated `FindXXX.cmake` files, you must remove the previous CMake files if they're located inside the repository to not cause a conflict, in the libtiff recipe [this can be seen](https://github.com/conan-io/conan-center-index/blob/master/recipes/libtiff/all/conanfile.py#L130) inside of `_patch_sources`,

```python
for module in ["LERC", ...]:
    rm(self, f"Find{module}.cmake", os.path.join(self.source_folder, "cmake"))
```

This is deleting the files inside the libtiff repository inside of the `cmake` repository, which can be [seen](https://github.com/libsdl-org/libtiff/blob/v4.6.0/cmake/FindLERC.cmake).

## Profiles

Conan profiles allow users to set a complete configuration set for **settings, options, environment variables** (for build time and runtime context), **tool requirements**, and **configuration variables** in a file. Profiles customize Conan's behavior for specific environments or configurations. They specify settings such as compiler versions, build types, and other options. The profile takes the same format as the `conanfile.txt`, an example would be,

```INI
[settings]
os=Windows
os_build=Windows
arch=x86_64
arch_build=x86_64
compiler=Visual Studio
compiler.version=17
build_type=Release

[options]
MyLib:shared=True

[buildenv]
VAR1=value

[runenv]
EnvironmentVar1=My Value
```

This is an example profile that specifies the requirements. In this example it is saying that the binaries must be for Windows, using Visual Studio 17 and configures the environment variables that will be set.

The profile is used when performing `conan` commands and it typically passed with the flag `-pr`. For example, `conan install . -pr <directory>`, `conan info -pr ...`. Keep in mind that configurating the profile is essential as the profile used when performing commands such as `conan install` much match the profile that was used to create the binaries for the library.

## Installing Dependencies

Use `conan install` to fetch and install dependencies specified in the `conanfile.txt`. Conan resolves dependencies and downloads packages from the configured remotes into the local cache. It is a requirement to set the profile when using conan2, however in conan it's best practice to use the `-pr` flag as to not use the default one. When running `conan install`, if the binaries exist on the remote, these will be installed and placed into `home/.conan/...`. The architecture is different between conan and conan2. The configurations of the dependencies and profile will result in a generated package id. It will search the remotes for this package id.

It is not expected to have every possible dependency and every possible combination of configuration on the conan center index. Therefore, if a package has not been built for a specific profile, the flag `--build` can be used when installing to built it ourselves. When doing this, it will essentially run `conan create` on the recipe and build it, placing it into the cache.

To download a particular dependency but not a dependency of a dependency, use the command `conan download`. This has additional flags such as `--recipe`. This will only download,

```
conanmanifes.txt
conanfile.py
conan_export.tgz
conan_sources.tgz
```

As of now in conan1 `conan download` will download all PackageID for the dependency, while conan2 allows to specify a PackageID.

## Development Environment Configuration


Maintainability of all configurations is important, especially in a shared environment. To manage this efficiently a directly structure such as,

```
📁 repository
    📁 config
        📁 profiles
            🗎 profile1
            🗎 profile2
        🗎 settings.yml
        🗎 remotes.json
```

can be very useful as the [command](https://docs.conan.io/1/reference/commands/consumer/config.html#conan-config-install) `conan config install <directory>` can be very useful as it will move all of the essential files within the specific directory into the `.conan` directory. This is essential in a shared environment. The command can take additional configurations such as storing the directory within GitHub repositories, `.zip` files or directly specifying the directory.

## PackageID

A PackageID uniquely identifies a binary package that is associated with a specific configuration. This ID is essential for Conan's package management system because it ensures that packages built under different settings (e.g. compiler version, operating system, architecture) can coexist in a repository without conflict.

Conan generates the PackageID by hashing several key components, including

1. **Settings** - Compiler, architecture, build type (e.g., Debug, Release), etc...
2. **Options** - Custom options defined for a package, such as feature flags or library versions.
3. **Requires** - Any dependencies the package has.
4. **Configuration Modifications** - Modifications in the recipe (`conanfile.py`) or applied `package_id()` method.

Each of these factors can influence the binary that is generated, which is why a unique ID is needed to differentiate between different configurations of the same package.

You can customize how conan computes the PackageID by overriding the `package_id()` method in the `conanfile.py` recipe. This can be useful in cases where some settings or options don't affect the final binary and shouldn't trigger a new PackageID, optimizing package reuse.

For example, if we want to have the same `package_id` for all the binaries compiled with gcc between versions `4.5` and `5.0`, we can do:

```python
def package_id(self):
    v = Version(str(self.info.settings.compiler.version))
    if self.info.settings.compiler == "gcc" and (v >= "4.5" and v < "5.0"):
        # The assigned string can be arbitrary
        self.info.settings.compiler.version = "GCC 4 between 4.5 and 5.0"
```

This works because the contents inside of `self.info` are involved in the `package_id` hashing for PackageID, by setting them to the same string value, they will hash identically. This approach is not recommended in the general case, and it would be better approached with the global `compatibility` plugin or the recipe `compatibility()` method.

The default `package_id()` uses the `settings` and `options` directly as defined, and assumes the semantic versioning for dependencies is defined in requires.

This `package_id()` method can be overridden to control the package ID generation. Within the `package_id()`, we have access to the `self.info` object, which is hashed to compute the binary ID and contains:


## Package ABI compatibility

Each package recipe can generate N binary packages from it, depending on these three items: `settings`, `options` and `requires`.

When any of the settings of a package recipe changes, it will reference a different binary.

```python
class MyLibConanPackage(ConanFile):
    name = "mylib"
    version = "1.0"
    settings = "os", "arch", "compiler", "build_type"
```

When this package is installed by a `conanfile.txt`, another package `conanfile.py`, or directly,

```shell
$ conan install mylib/1.0@user/channel -s arch=x86_64 -s ...
```

The process is,

1. Conan gets the user input settings and options. Those settings and options can come from the command line, profiles or from the values cached in the latest `conan install` execution.

2. Conan retrieves the `mylib/1.0@user/channel` recipe, reads the `settings` attribute, and assigns the necessary values.

3. With the current package values for `settings` (also `options` and `requires`), it will compute a SHA1 hash that will serve as the binary package ID, e.g. `c6d75a933080ca17eb7f076813e7fb21aaa740f2`.

4. Conan will try to find the `c6d75...` binary package. If it exists, it will be retrieved. If it cannot be found, it will fail and indicate that it can be built from sources using `conan install --build`.

If the package is installed again using different settings, for example, on a `32-bit` architecture

```shell
$ conan install mylib/1.0@user/channel -s arch=x86 -s ...
```

The process will be repeated with a different generated package ID, because the `arch` setting will have a different value.

When developers using the package use the same settings as one of those uploaded binaries, the computed package ID will be identical causing the binary to be retrieved and reused without the need of rebuilding it from the sources.


Note this simple scenario of a header-only library. The package does not need to be built, and it will not have any ABI issues at all. The recipe for such a package will be to generate a single binary package, no more. This is easily achieved by not declaring `settings` nor `options` in the recipe as follows:

```python
class MyLibConanPackage(ConanFile):
    name = "mylib"
    version = "1.0"
    # no settings defined!
```

