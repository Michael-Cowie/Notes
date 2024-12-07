# Impliciation Conversions With `{}`

When a return type is specified in a function, it is now possible to implicitly create that type inside the `return` statement,

```C++
#include <iostream>

class Point {
    int x;
    int y;
    
    public:
        Point(int x, int y) : x(x), y(y) {
            
        };
    
        void print_point(){
            std::cout << "X: " << x << "  Y: " << y;
        }
};

Point create_point(int x, int y) {
  return {x, y};  
};

int main() {
    Point p = create_point(10, 20);
    p.print_point();
    return 0;
}
```

The magic is primarily inside of,

```C++
Point create_point(int x, int y) {
  return {x, y};  
};
```

Here, we have specified the return type as `Point`. Therefore, during the line `return {x, y};` we are returning a `Point(x, y)`.
