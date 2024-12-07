<div align="center">
  <h1> Pandas </h1>
</div>

Pandas is a powerful open-source data manipulation and analysis library for Python. It was created to address the need for a flexible and efficient tool to handle structured data, particularly for data cleaning, transformation, and analysis tasks. Pandas provides data structures and functions that make it easier to work with structured data, such as tables or spreadsheets, and perform various operations on them.

The main purpose of Pandas is to provide an intuitive and high-performance data manipulation toolkit for Python, enabling users to work with structured data effectively. Some of the key problems that Pandas solves include:

##### Data Cleaning

 Pandas provides functions to handle missing data, duplicate data, and inconsistent data. It offers flexible tools for data imputation, data type conversion, and data validation, allowing users to clean and preprocess datasets efficiently.

 ##### Data Transformation

 Pandas offers powerful tools for reshaping, merging, and joining datasets. It allows users to pivot, melt, and stack data, facilitating various transformations to suit different analysis requirements. With Pandas, you can aggregate data, apply functions across groups, and perform complex data manipulations easily.

 #### Data Analysis

 Pandas provides a wide range of statistical and mathematical functions for data analysis. It supports descriptive statistics, filtering, sorting, and ranking operations. Additionally, Pandas integrates well with other popular libraries in the scientific Python ecosystem, such as NumPy, Matplotlib, and scikit-learn, making it a comprehensive tool for data analysis and exploration.

 #### Time Series Analysis

 Pandas has robust support for working with time series data. It offers specialized data structures and functions for handling time-based data, such as indexing by time, resampling, time shifting, and rolling window operations. This makes Pandas a popular choice for analyzing financial, economic, and sensor data.

 #### Data I/O

 Pandas provides functions to read and write data in various formats, including CSV, Excel, SQL databases, and more. It simplifies the process of loading data into memory for analysis and enables seamless integration with external data sources.

 # Data Structures

 The two primary data structures in Pandas are **Series** and **DataFrame**. A Series is a one-dimensional labeled array that can hold any data type, while a DataFrame is a two-dimensional table with labeled rows and columns. Understanding how to create, access, and manipulate these data structures is crucial for working with Pandas effectively.

 ## Pandas vs NumPy

Pandas and NumPy are both popular libraries in the Python ecosystem and offer powerful data manipulation capabilities. While there are some similarities between the two, they serve different purposes and have distinct features.

#### Pandas

- Pandas is built on top of NumPy and provides higher-level data structures, namely Series and DataFrame, that are more suitable for working with structured and labeled data.
- Pandas offers powerful data manipulation, data analysis, and data cleaning capabilities.
- It provides flexible and efficient handling of heterogeneous, labeled, and missing data. Handling of missing data is achieved via `NaN` and utilizing methods such as `isna()` or `isnull()`.
- Pandas is particularly useful for data preprocessing, data exploration, data transformation, and data analysis tasks.
- Series and DataFrame in Pandas allow for easy indexing, handling missing values, grouping, merging, reshaping, and aggregating data.
- Pandas supports both numerical and non-numerical data types.
- It integrates well with other data analysis and visualization libraries in Python, such as Matplotlib, Seaborn, and Scikit-learn.

Choose Pandas,

- When working with structured, labeled, or tabular data, such as CSV or Excel files, SQL databases, or data obtained from web scraping.
- When dealing with heterogeneous data that may have missing values or require complex data transformations.
- When performing data exploration, analysis, or cleaning tasks.
- When you need to perform operations like grouping, aggregating, or reshaping data.
- When working with time series data.

#### NumPy

- NumPy is primarily focused on numerical computing and provides support for multidimensional arrays called ndarrays.
- It offers efficient storage and operations on homogeneous numerical data.
- NumPy is well-suited for numerical computations, scientific computing, and mathematical operations such as linear algebra, Fourier transforms, and random number generation.
- It provides low-level, high-performance array operations and functions.
- NumPy arrays have a fixed size and a homogeneous data type.

Choose NumPy,

- When you need to perform numerical computations or mathematical operations on homogeneous numerical data.
- When dealing with large numerical arrays or multidimensional arrays.
- When implementing algorithms that require high-performance array operations.
- When working with linear algebra, Fourier transforms, or random number generation.

In summary, Pandas is ideal for working with structured, labeled, and heterogeneous data, while NumPy is well-suited for numerical computations and operations on homogeneous numerical data. Choosing between them depends on the specific requirements of your data analysis or scientific computing tasks. In many cases, you may find it beneficial to use both Pandas and NumPy together, as they complement each other and can be used in conjunction to address a wide range of data processing and analysis needs.

## `loc` and `iloc`

 The two main methods to understand and manipulate DataFrames and Series are **iloc** and **loc**. The main distinction is the idea of a **Label** vs a **Location**.

 - `loc` stands for "location" and it primarily used for accessing data based and label-based indexing. It gets rows (and/or columns) **with particular labels**.
 - `iloc` stands for "integer location" and is primarily used for accessing data based on **integer-based indexing**. `iloc` gets rows (and/or columns) at integer locations.

 `loc` and `iloc` use **square brackets for the indexing, not curved brackets**. This means that `loc` and `iloc` are not "typical" functions, infact, they're not functions at all.

 ```Python
 import pandas as pd
df = pd.DataFrame()
print(df.loc.__class__)
 ```

Will give us,

```Python
<class 'pandas.core.indexing._LocIndexer'>
```

This tells us that `loc` is an instance of the `_LocIndexer` class. The syntax `loc[]` derives from the fact that `_LocIndexer` defines `__getitem__` and `__setitem__`, which are the methods python calls whenever you use the square brackets syntax.

 To demonstrate, consider a series `s` of characters

 ```Python
 >>> s = pd.Series(list("abcdef"), index=[49, 48, 47, 0, 1, 2]) 
49    a
48    b
47    c
0     d
1     e
2     f

>>> s.loc[0]    # value at index label 0
'd'

>>> s.iloc[0]   # value at index location 0
'a'

>>> s.loc[0:1]  # rows at index labels between 0 and 1 (inclusive)
0    d
1    e

>>> s.iloc[0:1] # rows at index location between 0 and 1 (exclusive)
49    a
 ```


## Pandas Indexing Syntax for Row and Column

`loc` and `iloc` work the same way with DataFrames as they do with Series. It's useful to note that **both methods can address columns and rows together**.

When given a tuple, the first element is used to index the rows and, if it exists, the second element is used to index the columns.

Consider the DataFrame defined below:

```Python
>>> import numpy as np 
>>> df = pd.DataFrame(np.arange(25).reshape(5, 5),  
                      index=list('abcde'), 
                      columns=['x','y','z', 8, 9])
>>> df
    x   y   z   8   9
a   0   1   2   3   4
b   5   6   7   8   9
c  10  11  12  13  14
d  15  16  17  18  19
e  20  21  22  23  24
```

Then for example,

```Python
>>> df.loc['c': , :'z']  # rows 'c' and onwards AND columns up to 'z'
    x   y   z
c  10  11  12
d  15  16  17
e  20  21  22

>>> df.iloc[:, 3]        # all rows, but only the column at index location 3
a     3
b     8
c    13
d    18
e    23
```

Pandas support the use of a comma when indexing to allow for multi-dimensional indexing, which is not supported in traditional Python indexing. This means we can index for rows AND columns. The general indexing for a Python list is `[start:stop[:step]]`. However Pandas essentially allows the use of this twice, seperated by a comma where the left is representing the row and the right is representing the columns. Pandas achieves this via polymorphism and implementing their own `__getitem__()` and `__setitem__()`.

As a quick reminder with Python indexing, the format is `[start:stop[:step]]`, hence

```Python
a[start:stop]
a[start:]       # Start through rest of array
a[:stop]        # Beginning through to stop -1
a[:]            # Shallow copy of array

a[::-1]         # All items in the array, reversed
a[1::-1]        # The first two items, reversed. (Start index 1, go backwards until completion)
a[:-3:-1]       # The last two items, reversed. (Start index -1, go backwards, upto index -3)
a[-3::-1]       # Everything except the last two items, reversed.
```

If we were to create own our exampe of using `__getitem__` it would be as follows,

```Python
class GetItem:

    def __getitem__(self, item):
        print(f'Attempting to get: ', item)
        return self


x = GetItem()

"""
The following will call __getitem__ twice!

Attempting to get:  1
Attempting to get:  2
"""
x[1][2]

"""
The following will call __getitem__ once!

Attempting to get:  (1, 2)
"""
x[1, 2]
```

 ## Series

 A Pandas Series is a one-dimensional labeled array that can hold any data type (integer, float, string, etc.). It consists of two main components, the data itself and the index that labels each data point.

 ## Creating a Series

```Python
import pandas as pd

# Creating a Series from a list
data = [10, 20, 30]
s = pd.Series(data)
print(s)
```

Will output,

```
0    10
1    20
2    30
dtype: int64
```

## Accessing and Manipulating a Series

### Accesing values using index

```Python
print(s[2]) 
```

```
30
```

### Accessing Elements by Position

```Python
import pandas as pd

# Creating a Series
data = [10, 20, 30, 40]
series = pd.Series(data)

# Accessing an element by position
element = series.iloc[1]
print(element)
```

```
20
```

### Accessing Multiple Elements by Position or Index Label

```Python
import pandas as pd

# Creating a Series
data = [10, 20, 30, 40]
series = pd.Series(data, index=['A', 'B', 'C', 'D'])

# Accessing multiple elements by position or index label
subset = series.iloc[1:3]  # By position
print(subset)

subset = series.loc['B':'C']  # By index label
print(subset)
```

```
B    20
C    30
dtype: int64

B    20
C    30
dtype: int64
```

### Accessing Elements by Index Level

```Python
import pandas as pd

# Creating a Series
data = [10, 20, 30, 40]
series = pd.Series(data, index=['A', 'B', 'C', 'D'])

# Accessing an element by index label
element = series.loc['B']
print(element)
```

```
20
```

### Slicing the Series

```Python
print(s[1:3])
```

```
1    20
2    30
dtype: int64
```

### Performing operations on the Series

```Python
s = s * 2
print(s)
```

```
0    20
1    40
2    60
dtype: int64
```

## DataFrame

A DataFrame is a two-dimensional labeled data structure, similar to a table or spreadsheet, with rows and columns. It allows for easy handling of structured and heterogeneous data. Each column in a DataFrame is a Pandas Series.

## Creating a DataFrame

### From a Dictionary

```Python
import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)
print(df)
```

Will output,

```
      Name  Age      City
0    Alice   25  New York
1      Bob   30    London
2  Charlie   35     Paris
```

Notice here how the Keys of the `dict` is the column name, and the Value is a list where each index will correspond to the row.

### From a List of Lists

```Python
import pandas as pd

df = pd.DataFrame(
    [[2, 3],           # <--- Each index is a Row
     [5, 6],
     [8, 9]],
    index=['cobra', 'viper', 'sidewinder'],  # <--- Renaming index from integers
    columns=['max_speed', 'shield']          # <--- Renaming column from integers
)

print(df)
```

```
            max_speed  shield
cobra               2       3
viper               5       6
sidewinder          8       9
```

With this example, we also provide an example of renaming the indexes and columns to our custom names, so that they are no longer integers.

### From a List of Dictionaries

```Python
import pandas as pd

data = [{'Name': 'Alice', 'Age': 25, 'City': 'New York'},
        {'Name': 'Bob', 'Age': 30, 'City': 'London'},
        {'Name': 'Charlie', 'Age': 35, 'City': 'Paris'}]

df = pd.DataFrame(data)
print(df)
```

```
      Name  Age      City
0    Alice   25  New York
1      Bob   30    London
2  Charlie   35     Paris

```

### From a NumPy Array

```Python
import pandas as pd
import numpy as np

data = np.array([['Alice', 25, 'New York'],
                 ['Bob', 30, 'London'],
                 ['Charlie', 35, 'Paris']])

df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print(df)
```

```
      Name Age      City
0    Alice  25  New York
1      Bob  30    London
2  Charlie  35     Paris
```

### From a CSV File

```Python
import pandas as pd

df = pd.read_csv('data.csv')
print(df)
```


## Accessing and Manipulating a DataFrame

### Accessing Columns

```Python
print(df['Name'])
```

```
0      Alice
1        Bob
2    Charlie
Name: Name, dtype: object
```

### Accessing rows using iloc

```Python
print(df.iloc[1])
```

```
Name       Bob
Age         30
City    London
Name: 1, dtype: object
```

### Accessing specific values

```Python
print(df.at[0, 'Age'])
```

```
25
```

### Adding a new column

```Python
df['Country'] = ['USA', 'UK', 'France']
print(df)
```

```
      Name  Age      City Country
0    Alice   25  New York     USA
1      Bob   30    London      UK
2  Charlie   35     Paris  France
```

### Accessing and Manipulating Subsets with Conditions

Conditional indexing, also known as boolean indexing, is a powerful feature in Pandas that allows you to select subsets of data from a DataFrame based on specified conditions. It involves using a boolean mask, which is a series or array of boolean values, to filter the rows or elements that satisfy the condition.

1. Creating a Boolean Mask
\
      You define a condition that evaluates to a boolean value (`True` or `False`) for each element in the DataFrame.This condition can involve comparisons (`>`, `<`, `==`, etc.), logical operators (`&`, `|`, `~`), or functions that return boolean values. Applying the condition to the DataFrame generates a boolean mask, which is a series or array of boolean values with the same shape as the original DataFrame.

2. Applying the Boolean Mask
\
      You use the boolean mask to index the DataFrame and select the rows or elements that correspond to True values in the mask. When the boolean mask is used for indexing, **only the rows or elements with corresponding `True` values are included in the resulting subset**.

```Python
import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Accessing a subset based on a condition
subset = df[df['Age'] > 25]
print(subset)
```

```
      Name  Age    City
1      Bob   30  London
2  Charlie   35   Paris
```

In this example, we are passing `df['Age'] > 25`. The result of `df['Age'] > 25` is the following,

```
0    False
1     True
2     True
Name: Age, dtype: bool
```

We use these `True` and `False` values to filter **which rows we want**.

#### Accessing Data

`df[condition]` or `df[(condition1) & (condition2)]` will returns a subset of the DataFrame that meets the specified condition. In this example, `condition` is a boolean array, which is a series or array of boolean values with the **same length as the DataFrame**.

#### Changing Data

`df.loc[condition, 'column_name'] = new_value` will assign a new value to a specific column where the condition is `True`. The following example will change the ages of everyone over 25 to 100.

```Python
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

df.loc[df['Age'] > 25, 'Age'] = 100
print(df)
```

```
      Name  Age      City
0    Alice   25  New York
1      Bob  100    London
2  Charlie  100     Paris
```

To perform the same operation on multiple columns, the syntax will be changed to `df.loc[condition, ['col1', 'col2']] = new_values`. Likewise, it is not mandatory to manipulate the data here, to simply have it returned and not altered based on the condition, `df.loc[condition, ['col1', 'col2']]` can be used.

Another method to change data could be the following, `df['column'] = df['column'].where(condition, new_value)`. In this example the `where` method is used to change the data in the specific column for each `False` index to the new value. Hence, the right side changes the column, but does not perform an in-place change and hence an assignment is further required.