<div align="center">
  <h1> Installers </h1>
</div>

Installation (or setup) of a computer program (including device drivers and plugins) is the act of making the program ready for execution. Installation refers to the particular configuration of a software or hardware with a view to making it usable with the computer. A soft or digital copy of the piece of software (program) is needed to install it. There are different processes of installing a piece of software. Because the process varies for each program and each computer, programs (including operating systems) often come with an installer, which is a specialised program responsible for doing whatever is needed (see below) for the installation. Installation may be part of a larger software deployment process.

Installation typically involves code (program) being copied/generated from the installation files to new files on the local computer for easier access by the operating system, creating necessary directories, registering environment variables, providing separate program for un-installation etc. Because code is generally copied/generated in multiple locations, uninstallation usually involves more than just erasing the program folder. For example, registry files and other system code may need to be modified or deleted for a complete uninstallation.

It is important to understand the distinction by the term **build** and **install**. Typically, building refers to the process of creating the `.exe`, which allows execution of the software to run the program. However, this does not organize the files into a complete file structure and setup the program files on a users computer. Installation does not create the `.exe`, but the installation benefits and differences can be explain below.

# Example Installation

Let us take an example of what is happening by installing the [Intel oneAPI runtime](https://www.intel.com/content/www/us/en/developer/articles/tool/compilers-redistributable-libraries-by-version.html). Downloading the 2022 version we obtain the file `w_dpcpp_cpp_runtime_p_2022.2.0.9553.exe`. Running this will perform an installation process as shown below.

![](./images/intel_oneAPI.PNG)

Performing the installation process, the first thing might be to notice that we now have additional **environment variable**. Under System Variables, the key has the value of `INTEL_DEV_REDIST` and the value is `C:\Program Files (x86)\Common Files\Intel\Shared Libraries\`. Now, looking inside this directory we can find all of the files that were extracted and moved here during the installation process. This process only needs to be once and is shared, meaning other software will not reinstall the runtime again and instead simply check for the existing environment variable, therefore saving space.

![](./images/intel_oneAPI_installed.PNG)

# Building Software

When creating software and shipping it to users, the executeable (`w_dpcpp_cpp_runtime_p_2022.2.0.9553.exe`) is included and typically installed from configurations setup by an installer. One example installer could be [inno setup](https://jrsoftware.org/isinfo.php). It is our responsibility to correctly configuration it so that the executeable is ran so that the user has the correct files to execute to main software.

# Programming Utilization

When running from source, it is necessary to access the runtime redistributables. However, when running from source code instead of executing a `.exe` the build and installation process is not done for you to immediately find and utilize the necessary files. Therefore, the files must be correctly added to the path. For example, when writing software in Python, if my software required the intel oneAPI redistributables previously installed to find and utilize them when running from source they must be added to the environment path. A "path" are a series of directories where our software will search for files.

A very simplified example, with no error handling can be shown as;

```python
intel_runtime = os.environ.get('INTEL_DEV_REDIST') # System Variable
intel_runtime = os.path.join(os.path.normpath(intel_runtime), 'intel64')
os_path = os.environ['PATH'].split(os.pathsep)
os_path.insert(0, intel_runtime)
os.add_dll_directory(intel_runtime)
os.environ['PATH'] = os.pathsep.join(os_path)

```

# Benefits of Installation VS Stand-alone executeable file

On Windows, at least, you can download a direct statically-linked executeable file and launch it directly or write your own program and execute it (even dynamically) without having to install it. One might then ask, what purpose does the installation process serve apart from setting up the Windows Registry as mentioned above. Here we will dive deeper into additional benefits for the reason many downloaded software come with installers rather than giving a standalone executeable.

## File size concerns

Programs with many large dependencies can bundle Web-based installers that download the dependencies and place them in a common location, so that they can be shared by multiple programs. For example, DirectX is a very large library. If every single program on your system that depends on DirectX just bundled the entire DirectX runtime with it, it would consume a lot of space.

Programs that are both very large and continuously updated are best distributed as a collection of many small files, along with a launcher or updater program that checks the internet for an updatem and if any update exists, only download the required changes. If all large programs were shipped as a single monolithic executeable, it is very likely that the patch process would require re-downloading the entire executeable, as patching the running executeable file on disk is near impossible due to file locks. Also, because the update needs to know where its files are, it often stores that directory path in a well-known location in the registry.

## User convenience concerns

Installers for very large programs, such as Visual Studio and Microsoft Office, allow the user to de-select the installation of certain features, if the user knows they will never need them. This has 3 potential benefits.

1. Reduce disk space consumption
2. Reduce download time and bandwidth consumption if the installer is a web downloader.
3. Reduce "clutter" and "bloat" on the users machine, e.g. fewer start menu/desktop shortcuts, fewer startup programs, etc...

Installers for complicated programs often come with configuration options that the user can set up using a user-friendly graphical interface as part of the installer, e.g. MySQL or SQL Servers installers, which can take you through the entire process of getting your database server up and running before you even click "Finish" on the installer.

Installers can prompt the user for required information, such as license keys, which only need to be entered once. This can simplify the design of the program itself and reduce the number of things it has to do and check when it starts up. This also results in the user having confidence that 'once' the program is successfully installed it should "just work", i.e. there are no more "gotchas" within the program that may hold them up from using it.

## Compatibility concerns

Some programs conflict with other programs, this is a simple and unfortunate fact of Software Engineering. Before installing a program that has known conflicts with other programs it is often helpful to first check the system to see whether an incompatible program is installed. The user can then be alerted if so, e.g. there is a very dangerous incompatibility potential in older versions of VMWare and VirtualBox that resulted in a Blue Screen of Death, because one program would try to use a special virtualization processor instruction after it was already reserved for the user by the other product. If you were to simply provide the end product to the user without an installer, you would have to check for the presence of incompatible products at 'every' start of your program, which could slow down the startup of the program.

Programs may have dependencies on other system components that can that can only be installed at a system-wide level, not at a per-user level. In order to install these special system components, administrative privilages are usually required and an installer usually has to be run.

## Limitation

Many programs, even those that are only available for download as an installer that requires admin priviledges, can be forcibly "unpacked" from their installers and run directly without installing them. Other programs, especially open source ones, are repacked into self-contained executeables by PortableApps It is noteworthy that *some* programs, when unpacked from their installer will have reduced functionality, exhibit errors or other problems.

On Operating Systems other than Windows, it is almost always possible to simply download (or compile) programs and run them as a regular user, without obtaining root. There are a few exceptions with respect to packages that are a core part of the OS, but for most user applications, you can run it in your home directory without installing it system-wide using the package manager. Windows is a bit of a special case in that desktop programs on Windows have an installer and can usually not be instaled any other way.


## Conclusion

In the end of it all, we do not "need" installers, strictly speaking. There are vanishingly few examples of applications that cannot, in princuple, be bundled into a single self-contained executeable with no resources, no installer etc. Even something as complicated as VMware Workstation could automatically obtain admin privileges, write the hypervisor kernel module out to a file on a disk and install it dynamically on program start up and ship all of its resources (images, sound, etc...) bundled inside the data section of an executeable.

Using an installer or not is a choice that Software Developers have to make. There are advantages and disadvantages for using an installer. Many vendors choose to distribute their software 'both' as an installer and as a standalone binary, or atleast as a ZIP file that can simply be unpacked and run. For software that does not absolutely require an installer, this is a very pragmatic way to go and makes everyone happy. Usually, software that does not ship in any other form than with an installer is softwar that requires administrative privileges to install some component of itself, since the installer is the most elegant way to obtain the needed privilges.
