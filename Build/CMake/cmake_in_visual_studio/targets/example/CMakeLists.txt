cmake_minimum_required(VERSION 3.10)
project(HelloWorldLibraries)

set(CMAKE_CXX_STANDARD 17)

# Add libraries
add_subdirectory(lib1)
add_subdirectory(lib2)

# Define main executable
add_executable(main main.cpp)

# Link the libraries to main
target_link_libraries(main PRIVATE lib1 lib2)