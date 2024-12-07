# Understanding the `auto` keyword

Firstly, let's try to understand what `auto` does by analyzing an example use,

```C++
auto const & x;
```

The keyword `auto` is a typename that represents an automatically-deduced type. We reccomend that you use the `auto` keyword for most situations unless you really want a conversion because it provides the following beneifts,

1. **Robustness:** If the expressions type is changed, such as a function return type is changed, it still works fine.
2. **Performance:** You're guaranteed that there will be no conversion
3. **Usability:** You don't have to worry about type name spelling difficulties and typo's. It is a simple way to declare a variable that has a complicated type. You can use `auto` to declare a variable where the initialization expressions involves templates, pointers to functions or pointers to members. 

4. **Efficiency:** Your coding can be more efficient
The `auto` initialization expression can take several forms,

  - Universal initialization syntax, such as `auto a{42};`
  - Assignment syntax, such as `auto b = 0;`
  - Universal assignment syntax, which combines the previous forms, such as `auto c = {3.14156};`
  - Direct initialization, or constructor-style syntax, such as `auto d(1.414f);`

When `auto` is used to declare the loop parameter in a range-based `for` statement, it uses a different initialization syntax,

```C++
`for (auto & i : iterable) {
    do_action(i);
}`
```

The `auto` keyword is a placeholder for a type, but it is not itself a type. Therefore, the `auto` keyword cannot be used in casts or operators such as `sizeof` and `typeid`.

# References and cv-qualifiers

Note that using `auto` drops references, `const` qualifiers and volatile qualifiers, 

```C++
#include <iostream>

using namespace std;


int main(){
    int count = 10;
    int& countRef = count;
    auto myAuto = countRef;
    
    countRef = 11;
    cout << count << endl; // 11
    
    myAuto = 12;
    cout << count << endl;  // 11 - NOT 12
    return 0;
}
```

In this example, `auto myAuto = counterRef;` does not change the value of `count` when setting `myAuto = 12;`. However if this was instead `int& myAuto = countRef;`, it would work as originally intended. This is happening because `myAuto` is an `int` not an `int &`, therefore `count` is not changed to `12`.

# Further Examples

The following declarations are equivalent, but the second declaration is simpler than the first. One of the compeling reasons to use the `auto` keyword is simplicity.

```
map<int, list<string>>::iterator i = m.begin();
auto i = m.begin();
```

The following code fragment declares the type of variables `iter` and `elem` when the `for` and range `for` loop start.

```C++
#include <iostream>
#include <deque>

using namespace std;


int main(){

    deque<double> dq{10, 11, 12, 13};
    
    for (auto iter = dq.begin(); iter != dq.end(); ++iter) {
        /*
        COPIES elements, when iterating over
        */
    }
    
    for (auto elem : dq) {
        /*
        COPIES elements, not much better than the example above
        */
    }
    
    for (auto & elem : dq) {
        /*
        Observes and/or modifies elements IN-PLACE

        e.g. elemn = 0, will set all elements to 0
        */
    }
    
    for (auto & elem : dq) {
        /*
        Observes elements IN-PLACE

        e.g. any attempts to modify elem will result
        in compiler errors
        */
    }
    return 0;
}
```