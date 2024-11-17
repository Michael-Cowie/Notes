<div align="center">
  <h1>  Integer Overflow </h1>
</div>

We will use the following code to demonstrate an integer overflow:

```C++
int main(){
    signed int max_int = 2147483647;
    cout << int(max_int + 1) << "\n";
    return 0;
}
```

Running the following code will print `-2147483648`. Notice here the `-` infront, although it is 1 higher if it was not negative.

# Explanation (signed)

Numbers are represented using **two's complement** where the most significant bit is negative and the others are positive, i.e.

| Bit Sequence | Number |
|--------------|--------|
| 1000         |   -8   |
| 1001         |   -7   |
| ...          |   ...  |
| 1111         |   -1   |
| 0001         |    1   |
| 0010         |    2   |
| ...          |   ...  |
| 0111         |    7   |

Therefore, since I had the maximum positive integer value which would be a `0` followed by remaining `1`s, adding a single `1` will turn this number into the bit representation of a `1` followed by `0`s, in this example would create `-2147483648`. This would explain why the `max_int + 1 + max_int` is `-1`, because it would be all `1`s, i.e.

`max_int + 1` + `max_int`
- `1000 0000 0000 0000 0000 0000 0000 0000` (`-2147483468`)
- \+
- `0111 1111 1111 1111 1111 1111 1111 1111` (`2147483467`)
- =
- `1111 1111 1111 1111 1111 1111 1111 1111` (`-1`)

# Explanation (unsigned)

If I were to instead use 

```C++
int main(){
    unsigned int zero = 0;
    cout << zero - 1; 
    return 0;
}
```

The following above will print `4294967295`

This is because `0` is represented as a series of `0`s, from here if we perform `-1` it will wrap around to all `1`s. Due to the number being unsigned and all `1`s it will print a larger number that is double the maximum positive signed number.

Likewise we we were to change it to `signed`, it will print a `-1`. This is because, as above, it is a series of all `1`s which has a value of `-1`.