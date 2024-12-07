<div align="center">
  <h1> Class Templates </h1>
</div>
Templates are a new concept which enable you to define generic classes and functions and thus provides support for generic programming. Generic programming is an approach where generic types are used as parameters in algorithms so that they work for a variety of suitable data types and data structures.

A template can be used to create a family of classes or functions. For example, a class template for an `array` class would enable us to create arrays of various data types such as `int` array and `float` array. Similarly, we can define a template for a function, say `mul()` that would help us create various versions of `mul()` for multiplying `int`, `float` and `double` type values.

A template can be considered as a kind of macro. When an object of a specific type is defined for actual use, the template definition for that class is substituted with the request data type. Since a template is defined with a parameter that would be replaced by a specified data type at the time of actual use of the class or function, the templates are sometimes called parameterized classes or functions.

Let us consider a Vector.

```C++
#include <iostream>

using namespace std;


class Vector
{
    int* v;
    int size = 0;
    
    public:
        Vector(int size) // Creates a null vector
        {
            this->size = size;
            v = new int[size];
            for (int i = 0; i < size; i++) {
                v[i] = 0;
            }
        }
        
        Vector(int (&a)[3])
        {
            /*
            Can never accept 
            
            Vector(int* a)
            {
                ...
            }
            
            By passing any normal array and having it decay into an integer pointer,
            we lose information to know the size of the array and correctly set it.
            Thus, size will either be not known or incorrectly set to 0.
            */
            size = 3;
            v = new int[3];
            for (int i= 0; i < size; i++)
            {
                v[i] = a[i];
            }
        }
        
        int operator *(Vector &y)
        {
            int sum = 0;
            for (int i = 0; i < size; i++)
            {
                sum += this->v[i] * y.v[i];
            }
            return sum;
        }
};

int main()
{
    int x[3] = {1, 2, 3};
    int y[3] = {4, 5, 6};
    
    Vector v1(3); // Creates a Null vector of 3 integers using Vector(int size)
    Vector v2(3);
    
    v1 = x; // Reinitialize v1 to the values on the object from Vector(int (&a)[3])
    v2 = y;
    
    int r = v1 * v2;
    cout << "r = " << r;
    return 0;
}
```

Now suppose we want to define a `Vector` that can store an array of `float` values. We can do this by simply replacing the appropiate `int` declarations with `float` in the `Vector` class. This means that we have to redefine the entire class all over again.

Assume that we want to define a `Vector` class with the data type as a parameter and then use this class to create a `Vector` of any data type instead of defining a class every time. The template mechanism enables us to achieve this goal.

Templates allow us to define generic classes. It is a simple process to create a generic class using a template with an anonymous type. The general format of a class template is:

```C++
template <class T>
class className {
  private:
    T var;
    ...
  public:
    T functionName(T arg);
    ...
};
```

The format for creating the objects is,

```C++
className<dataType> classObject;
```

for example,

```C++
className<int> classObject;
className<float> classObject;
className<string> classObject;
```

The template definition of a `Vector` class below illustrates the syntax of a template:

```C++
#include <iostream>

using namespace std;

template <class T>
class Vector
{
    T* v;
    int size = 0;
    
    public:
        Vector(int size) // Creates a null vector
        {
            this->size = size;
            v = new T[size];
            for (int i = 0; i < size; i++) {
                v[i] = 0;
            }
        }
        
        Vector(T (&a)[3])
        {
            /*
            Can never accept 
            
            Vector(int* a)
            {
                ...
            }
            
            By passing any normal array and having it decay into an integer pointer,
            we lose information to know the size of the array and correctly set it.
            Thus, size will either be not known or incorrectly set to 0.
            */
            size = 3;
            v = new T[3];
            for (int i= 0; i < size; i++)
            {
                v[i] = a[i];
            }
        }
        
        T operator *(Vector y)
        {
            T sum = 0;
            for (int i = 0; i < size; i++)
            {
                sum += this->v[i] * y.v[i];
            }
            return sum;
        }
};

int main()
{
    int x[3] = {1, 2, 3};
    int y[3] = {4, 5, 6};
    
    Vector<int> v1(3); // Creates a Null vector of 3 integers using Vector(int size)
    Vector<int> v2(3); // Keep the data types the same for this simplistic example
    
    v1 = x; // Reinitialize v1 to the values on the object from Vector(int (&a)[3])
    v2 = y;
    
    int r = v1 * v2;
    cout << "r = " << r;
    return 0;
}
```

The class template definition is very similar to an ordinary class definition except the prefix `template <class T>` and the use of type `T`. This prefix tells the compiler that we are going to declare a template and use `T` as a type name in the declaration. Thus, `Vector` has become a parameterized class with the type `T` as its parameter. `T` may be substituted by any data type including a user-defined types. Now, we can create a `Vector` for holding different data types.

We can use more than one generic data type in a class template. They are declared as a comma-separated list within the template specification as shown,

```C++
template <class T1, class T2, ...>
class ClassName
{
    ...
}
```

and will be called as follows,

```C++
Example<float, int> e1(1.23, 123);
Example<int, char> e2(100, 'W');
```

Member function templates are defined in a slightly different way, if we were to write the template definition with the function defined outside of the class, it would have the following format,

```C++
template <class T>
returnType className <T>::functionName(T arg1, ...)
{
    ...
}
```

The following is a simplified example of the previous `Vector` class where I have made the constructor a templated function with the definition outside of the class declaration,

```C++
#include <iostream>

using namespace std;

template <class T>
class Vector
{
    T* v;
    int size = 0;
    
    public:
        Vector(int initialsSize);
};

template <class T>
Vector <T>::Vector(int initialSize)
{
    size = initialSize;
    v = new T[initialSize];
    for (int i = 0; i < initialSize; i++) {
        v[i] = 0;
    }
};

int main()
{
    Vector <int> v(3);
    return 0;
}
```

# Function Templates

Like class templates, we can also define function templates that could be used to create a family of functions with different argument types. The general format of a function template is,

```C++
template <class T>
returnType functionName(T arg1, ...)
{
    // Body of function with type T 
    // whenever appropiate
    ...
}
```

The function template syntax is similiar to that of the class template except that we are defining functions instead of classes, while still including the word `class`. We must use the template parameter `T as and when necessary in the function body and in its argument list.

The folowing is an example template function to swap two given numbers,

```C++
#include <iostream>

using namespace std;

template <class T>
void swap_numbers(T& x, T& y)
{
    T temp = x;
    x = y;
    y = temp;
}

int main()
{
    int a = 10;
    int b = 20;
    cout << "a = " << a << ", b = " << b << endl;
    swap_numbers(a, b);
    cout << "a = " << a << ", b = " << b << endl;
    return 0;
}
```

Like template classes, we can use more than one generic data type in the template statement, using a comma-separated list as shown below,

```C++
template <class T1, class T2, ...>
returnType functionName(T1 arg1, T2 arg2, ...)
{
    ...
}
```

The following is an example usage,

```C++
#include <iostream>

using namespace std;

template <class T1, class T2>
void display(T1 arg1, T2 arg2)
{
    cout << arg1 << " " << arg2 << endl;
}

int main()
{
    display("A integer", 1);
    display("A float", 1.5);
    return 0;
}
```