cmake_minimum_required(VERSION 3.27)

project(my_pybind VERSION 1.0)

find_package(pybind11 REQUIRED)

set(PROJECT_SOURCE_DIR "src")
set(PROJECT_INCLUDE_DIR "include")

# The library I have created that I want exposed

set(SOURCE_FILES
    ${PROJECT_INCLUDE_DIR}/main.hpp
    ${PROJECT_SOURCE_DIR}/main.cpp
)

add_library(my_math STATIC ${SOURCE_FILES})

target_include_directories(my_math PRIVATE ${PROJECT_INCLUDE_DIR})


# pybind11, exposing my library

pybind11_add_module(my_pybind11_module src/binder.cpp)

target_link_libraries(my_pybind11_module PRIVATE my_math)

target_include_directories(my_pybind11_module PRIVATE ${PROJECT_INCLUDE_DIR})
