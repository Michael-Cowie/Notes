from os import getpid

from build.Debug import my_pybind11_module

print(getpid())

print(my_pybind11_module.add(1, 2))

my_pybind11_module.hello_world()

my_data = my_pybind11_module.MyData(x=10, y=20)
my_data.print()
