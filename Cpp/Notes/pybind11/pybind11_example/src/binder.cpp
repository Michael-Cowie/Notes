#include <pybind11/pybind11.h>

#include "main.hpp"

PYBIND11_MODULE(my_pybind11_module, module) {
    module.attr("__version__") = "1.0";
    module.doc() = "Hello from pybind11!";

    module.def("add", &add, "Adds two numbers");
    module.def("hello_world", &hello_world, "Hello World!");

    pybind11::class_<MyData>(module, "MyData")
        .def(pybind11::init<>())
        .def(pybind11::init<float, float>(), "double float constructor", pybind11::arg("x"), pybind11::arg("y"))
        .def("print", &MyData::print)
        .def_readwrite("x", &MyData::x)
        .def_readwrite("y", &MyData::y)
        ;
}
