#pragma once

void hello_world();

int add(int i, int j);

struct MyData
{
    float x, y;

    MyData() : x(0), y(0) {};

    MyData(float x, float y) : x(x), y(y) {};

    void print();
};