<div align='center'>
    <h1> Logarithms </h1>
</div>

Logarithms are among the most significant developments in mathematics because they provide a way to understand powers, growth and relationships involving repeated multiplication. They are the inverse of exponents, meaning they answer the question **"To what power must a base be raised to produce a given number?"**. In other terms, logarithms solve for the exponent. Here, logarithms are used to solve for $x$.

```math
2^x = 256
```

The logarithm function is defined for **positive real numbers**. By definition, a logarithm is the power to which a number a must be raised to get some other number. Since a negative number cannot be expressed as a power of a positive base, **the logarithm of a negative number is undefined**. 

While logarithms are often as a technical algebraic tool, their historic purpose was practical and transformative. They simplified difficult calculations long before calculators existed and today they remain essential in science, engineering, finance and computer science.

Logarithms were first developed in the early seventeenth century by John Napier. At the time, astronomers, navigators and scientists needed to perform large numerical calculations by hand. Multiplication, division, powers and roots were slow and highly susceptible to human error. Napier's invention offered a brilliant solution. **If multiplication could be converted into addition, calculations would become dramatically easier**.

Soon after, Henry Briggs refined the idea into the base-10 system, producing tables that were used throughout science and engineering for centuries. Before electronic calculators, logarithm tables and slide rules were standard for professionals.

The original intent of logarithms, therefore, was **computational efficiency**. Their deeper mathematical significance emerged later, logarithms reveal the hidden structure of exponential relationships.


<div align='center'>
    <h1> Understanding What a Logarithm Means </h1>
</div>


A logarithm **reverses exponentiation**. If

```math
2^5 = 32
```

then the corresponding logarithmic statement is

```math
\log _2(32) = 5 
```

This means that 5 is the exponent required to raise 2 to obtain 32. More generally,

```math
\log _b(x) = y \Leftrightarrow b^y = x
```

This definition shows that logarithms and exponents are inverse operations. Just as subtraction reverses addition, logarithms reverse powers.

Several bases are especially important. Base 10 logarithms are common in science, base 2 logarithms are central to computing and the natural logarithm uses the number $e$, which appears frequently in calculus and growth models.

Logarithms turn multiplication into addition and division into subtraction. Multiplication and division are hard, addition and subtraction are easy.

Using base 5 logarithms, the following will turn multiplication into addition.

1. $\log_5(5) = 1$
2. $\log_5(25) = 2$ because $5^2 = 25$
3. $\log_5(125) = 3$ because $5^3 = 125$

Now multiply,

```math
25 \times 125
```

Normally multiplication is harder. Rewrite them as powers of $5$.

```math
\begin{aligned}
25 &= 5^2 \\
125 &= 5^3
\end{aligned}
```

so,

```math
25 \times 125 = 5^2 \times 5^3 = 5^{2 + 3} = 5^5
```

Instead of multiplying numbers, we **added exponents**.

```math
2 + 3 = 5
```

Now convert back,

```math
5^5 = 3125
```

In the modern world, where we already know how to multiply directly, it can seem pointless. Historically, logarithms were valuable because you **did not multiply** $25 \times 125$ directly. **You used log tables**. The process was to,

Compute,

```math
25 \times 125
```

You must carry out multiplication manually. However using logarithms you look up each numbers logarithm in a table,

```math
\begin{aligned}
\log_{5}\left(25\right) &= 2 \\
\log_{5}\left(125\right) &= 3
\end{aligned}
```

Then add,

```math
2 + 3 = 5
```

Now **look up** number whose base-5 log is 5.

```math
5^5 = 3125
```

So the multiplication was replaced by,

1. Table lookup
2. Addition
3. Reverse table lookup

For easy numbers like 25 and 125, logs seems unnecessary. But for awkward numbers such as,

```math
37.42 \times 918.6
```

manual multiplication is slow and error-prone. With logarithm tables,

1. Look up $\log(37.42)$
2. Look up $\log(918.6)$
3. Add them
4. Look up the antilog

Much faster before calculators existed.

<div align='center'>
    <h1> Why Logarithms Matter in Practical Life </h1>
</div>

Although logarithms were born from hand calculation, their usefulness remains highly relevant.

In computer science, logarithms describe algorithm efficiency. Binary search repeatedly halves a data set, so searching $n$ items take approximately $\log_2 n$ steps. This explains why enormous sorted lists can be searched quickly.

In finance, logarithms are used when solving compound interest equations If money grows exponentially, logs help determine how long it takes for an investment to reach a target value. For example, "Given \$5, at an interest rate of 2% a year, how many years to reach \$500?".

```math
\begin{aligned}
5 \times \left(1.02\right)^x &= 500 \\
\left(1.02\right)^x &= 100 \\
\log_{1.02}\left(100\right) &= x \\
x &= 232
\end{aligned}
```

Therefore, it will take 232 years.

In science, many natural processes such as radioactive decay, bacterial growth and cooling occur exponentially. Logarithms help convert these models into solvable linear relationships.

In measurement systems, logarithmic scales are common.

- Sound intensity uses decibels.
- Acidity uses pH.
- Earthquake strength has historically used Richter scale.

In each case, equal increases on the scale represent multiplicative changes rather than additive ones.

<div align='center'>
    <h1> The Laws of Logarithms </h1>
</div>

The laws of logarithms are not arbitrary rules. They arise directly from the laws of exponents.

## Product Law

Let,

```math
\log_b(xy) = \log_b(x) + \log_b(y)
```

This law states that multiplying numbers inside a logarithm becomes addition outside it.

Let,

```math
\begin{aligned}
x &= b^m \\
y &= b^n
\end{aligned}
```

Then,

```math
xy = b^m \cdot b^n = b^{m + n}
```

Taking logarithm base $b$,

```math
\log_b(xy) = m + n
```

But,

```math
\begin{aligned}
m &= \log_{b}\left(x\right) \\
n &= \log_{b}\left(y\right)
\end{aligned}
```

$\therefore$

```math
\log_b(xy) = \log_b(x) + \log_b(y)
```

As an example,

```math
\log_2(8 \cdot 4) = \log_2(32) = 5
```

Therefore,

```math
\log_2(8) + \log_2(4) = 3 + 2 = 5
```

## Quotient Law

Let,

```math
\log_b \left(\frac{x}{y}\right) = \log_b(x) - \log_b(y)
```

This law states that dividing numbers inside a logarithm becomes subtraction outside it, however this is implicitly a form of addition due to nature of fractions.


Let,

```math
\begin{aligned}
x &= b^m \\
y &= b^n
\end{aligned}
```

Then,

```math
\frac{x}{y} = \frac{b^m}{b^n} = b^{m-n}
```

$\therefore$

```math
\begin{aligned}
\log_{b}\left(\frac{x}{y}\right) &= m - n \\
\log_{b}\left(\frac{x}{y}\right) &= \log_{b}\left(x\right) - \log_{b}\left(y\right)
\end{aligned}
```

As an example,

```math
\begin{aligned}
\log_{2}\left(16\right) &= 4 \\
\log_{2}\left(4\right) &= 2
\end{aligned}
```

Then,

```math
\log_2 \left(\frac{16}{4}\right) = 4 - 2 = 2
```

## Power Law

Let,

```math
\log_b (x^n) = n \log_b (x)
```

This law is especially useful in algebra, calculus and data modelling because exponents can be brought forward as coefficients.

Because,

```math
\log_b (x) = m
```

It follows,

```math
b^m = x
```

Then,

```math
\begin{aligned}
\left(b^m\right)^n &= x^n \\
b^{m \cdot n} &= x^n \\
\log_{b}\left(x^n\right) &= m \cdot n
\end{aligned}
```

Therefore,

```math
\begin{aligned}
\log_{b}\left(x^n\right) &= \log_{b}\left(x\right)\cdot n \\
\log_{b}\left(x^n\right) &= n\log_{b}\left(x\right)
\end{aligned}
```

If we have an example,

```math
\log_3(9^2) = 2 \log_3 (9) = 2(2) = 4
```

## Changing Log Bases

We can change the bases,

```math
\log_b (x) = \frac{\log_k (x)}{\log_k (b)}
```

Natural log is a frequent and common conversion.

Let,

```math
y = \log_b (x)
```

By definition,

```math
b^y = x
```

So $y$ is the exponent that turns $b$ into $x$.

First, take the logarithm of both sides and applying the power law.

```math
\begin{aligned}
\log_{k}\left(b^y\right) &= \log_{k}\left(x\right) \\
y\log_{k}\left(b\right) &= \log_{k}\left(x\right) \\
y &= \frac{\log_{k}\left(x\right)}{\log_{k}\left(b\right)}
\end{aligned}
```

## Solving Exponential Functions

One of the most practical uses of logarithms is solving equations where the unknown is in the exponent.

Consider,

```math
3^x = 20
```

Now we have two methods for solving this problem. The first is to solve it directly uusing the definition of logarithms.

```math
\log_3 (20) = x
```

Alternatively, you can apply the common logarithm function of base $10$ to each side and then apply the power law.

```math
\begin{aligned}
3^x &= 20 \\
\log\left(3^x\right) &= \log (20) \\
x\log\left(3\right) &= \log\left(20\right) \\
x &= \frac{\log\left(20\right)}{\log\left(3\right)}
\end{aligned}
```

Without logarithms, such equations would be extremely difficult to solve exactly.

Similarily, while the common logarithm $\log$ is for base $10$, $ln$ is used for base $e$.

Therefore,

```math
e^{2x} = 7
```

Gives,

```math
2x = \ln 7
```