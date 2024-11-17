<div align="center">
  <h1>  String and Byte Strings </h1>
</div>

The only thing that a computer can store is bytes. To store anything in a computer, you must first `encode` it, i.e. convert it to bytes. For example,

- If you want to store music, you must first encode it using `MP3`, `WAV`, etc.
- If you want to store a picture, you must first encode it using `PNG`, `JPEG`, etc.
- If you want to store text, you must first encode it using `ASCII`, `UTF-8`, etc.

`MP3`, `WAV`, `PNG`, `JPEG`, `ASCII` and `UTF-8` are examples of encoding. An encoding is a format to represent audio, images, text, etc in bytes. In Python, a byte string is just that, a sequence of bytes, **it is not human-readable**. Under the hood, everything must be converted to a byte string before it can be stored in a computer.

On the other hand, a character string, often just called a "string" is a sequence of characters. It is human readable. A character string can't be directly stored in a computer, it has to be encoded first (converted to a byte string). There are multiple encodings through which a character string can be converted into a byte string, such as `ASCII` and `UTF-8`. When we talk about encoding a string as a byte string, it means converting the string into a sequence of 1s and 0s, specifically binary data, where each unit of data is represented by a byte (8 bits).

For example, let's consider the string "Hello" encoded in `UTF-8`. The `UTF-8` encoding scheme represents characters using variable-length byte sequences. When we encode "Hello" in `UTF-8`, it would be represented as a byte string consisting of the following bytes:

```
01001000 01100101 01101100 01101100 01101111
```

In this binary representation, each sequence of 8 bits (1 byte) corresponds to a character in the string. The bytes can be stored, transmitted, or processed as binary data.

# Code Examples

```Python
'I am a string'.encode('ASCII')
'I am a string'.encode('UTF-8')
```

The above Python code will encode the string `I am a string` using the encoding `ASCII` and `UTF-8`. The result of the above code all be a byte string. If you print it, Python will represent it as `b'I am a string'`. Remember, however, that byte strings **aren't human readable**. What is happening here is that Python is decoding them from `ASCII` when you print them. In Python, a byte string is represented by a `b`, followed by the byte strings `ASCII` representation.

For example, if I encode something that is not `ASCII` or `UTF-8`, it will not print the original characters.

```Python
print('I am a string'.encode('UTF-16'))
```

Will give us,

```
b'\xff\xfeI\x00 \x00a\x00m\x00 \x00a\x00 \x00s\x00t\x00r\x00i\x00n\x00g\x00'
```

However, correctly knowing the encoding scheme, it can be correctly decoded.

```Python
b'I am a string'.decode('ASCII')
```

Will output,

```
'I am a string'
```

However, notice here, that the prefix `b` is missing. This is **not a byte string**. Encoding and decoding are inverse operations. Everything must be encoded before it can be written to disk, and it must be decoded before it can be read by a human. When a string is encoded, its characters are mapped to the corresponding binary representations according to the chosen encoding scheme. This encoded representation can be stored in a file, transmitted over a network, or used for various other purposes. To make use of the encoded string, it needs to be decoded, which involves reversing the process and converting the binary data back into its original character representation.

# Writing Text to a Binary File - What's the difference?

The most important definition of what the word "binary" means come from just a situation where a number can take on one of two values, e.g. `on/off`, `yes/no` and `1/0`. Keep that core definition in mind. We will find a large number of other idiomatic usages of the word "binary" in the computer world, depending on context. As an example, some people will refer to a file representin an executable image (Such as a `.exe`) as simply a "binary".

As an example, some people refer to a file representing an executable image (Such as a `.exe` as simply "a binary").

An often confusing distinction of how sometimes people will talk about a file format as being either "textual" or "binary". Yet, todays computers are based on systems that are always binary. So if "textual" files aren't stored ultimately  as binary bits somewhere, how else would they be stored?

So really what it means for a file format to be labeled as "textual" is to say that it is "stricter about what binary patterns it uses, such that it will only use those patterns which make sense in a certain textual encoding". That's why those files look readable when you load them up in text editors.

So a "textual file format" is a **subset of all file formats**, sometimes when people want to refer to something that is not in that subset of textual files, they will call it a "binary file format".

All you do when you open a file in "textual" vs "binary" mode in C++ is to tell the stream that you are not using only the bit patterns likely to look good in a text editor when loaded. Opening in binary asks for all the bytes to be sent to the file in exactly the same place as were used originally, instead of having it try and take care of cross-platform text-file differences in newline handling "under the hood" as convenience.

Therefore, use 'b' mode to read/write binary data as is without any transformations such as converting newlines to/form platform-specific values  or decoding/encoding text using a character encoding.