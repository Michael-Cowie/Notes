#include "main.hpp"

#include <iostream>

void hello_world(){
    std::cout << "Hello, from my_pybind11!\n";
}

int add(int i, int j) {
    return i + j;
}

void MyData::print()
{
    printf("%f, %f\n", x, y);
}
