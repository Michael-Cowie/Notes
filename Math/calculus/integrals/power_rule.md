<div align='center'>
<h1>Integration Using the Power Rule</h1>
</div>

Integration is the inverse operation of differentiation. While differentiation reduces the power of a variable by one and multiplies by the original exponent, integration increases the power by one and divides by the new exponent.

The power rule for integration provides a systematic method for finding the antiderivative of polynomial expressions and expressions involving negative exponents. It is derived by reversing the power rule for differentiation.

## The Power Rule for Integration

Recall the power rule for differentiation,

```math
\frac{d}{dx}(x^n)=nx^{n-1}
```

To reverse this operation, we increase the exponent by one and divide by the resulting exponent. This gives the power rule for integration,

```math
\boxed{\int x^n\,dx=\frac{x^{n+1}}{n+1}+C}
```

where $n\neq -1$, and $C$ represents the arbitrary constant of integration. The arbitrary constant is necessary because differentiating a constant produces zero. Consequently, multiple functions that differ only by a constant have the same derivative.

For example, consider integrating $x^3$,

```math
\begin{aligned}
\int x^3\,dx
&=
\frac{x^{3+1}}{3+1}+C \\
&=\frac{1}{4}x^4+C
\end{aligned}
```

We can verify this result by differentiating the antiderivative,

```math
\begin{aligned}
\frac{d}{dx}\left(\frac{1}{4}x^4+C\right)
&=
\frac{4}{4}x^3 \\
&=x^3
\end{aligned}
```

This confirms that the integration has successfully reversed the differentiation.

## Integration of Negative and Zero Exponents

The power rule also applies to expressions containing zero and negative exponents, **provided the exponent is not $-1$**.

**Zero exponent**

```math
\int x^0\,dx
=
\frac{x^{0+1}}{0+1}+C
```

```math
=x+C
```

Since $x^0=1$, this is equivalent to integrating a constant,

```math
\int 1\,dx=x+C
```

**Negative exponent**

Consider integrating $x^{-3}$,

```math
\int x^{-3}\,dx
=
\frac{x^{-3+1}}{-3+1}+C
```

```math
=-\frac{1}{2}x^{-2}+C
```

Using the laws of indices, this can also be expressed as,

```math
=-\frac{1}{2x^2}+C
```

These examples demonstrate that the power rule is not restricted to positive exponents. It can also be used with zero and negative exponents, provided the exponent is not $-1$.

## The Special Case, When n = -1

An important exception to the power rule occurs when the exponent is $-1$. Substituting $n=-1$ into the general power rule produces,

```math
\int x^{-1}\,dx
=
\frac{x^{-1+1}}{-1+1}+C
```

This results in division by zero, meaning the power rule cannot be applied. Instead, we use the natural logarithm rule,

```math
\boxed{\int x^{-1}\,dx=\ln|x|+C}
```

This can be verified through differentiation,

```math
\frac{d}{dx}\left(\ln|x|+C\right)
=
\frac{1}{x}
```

Therefore, the natural logarithm provides the antiderivative when integrating a variable raised to the power of $-1$. The vertical bars in $\ln |x|$ denote the absolute value of $x$. Absolute value ensures that the logarithm's input is positive, since the natural logarithm is only defined for positive real numbers.

<div align='center'>
    <h1> Examples </h1>
</div>

#### Example 1 - Integrating a positive exponent

Evaluate,

```math
\int x^5\,dx
```

<p>
&nbsp;&nbsp;&nbsp;&nbsp; <strong> Step 1 - Add one to the exponent </strong>
</p>

```math
5+1=6
```

<p>
&nbsp;&nbsp;&nbsp;&nbsp; <strong> Step 2 - Divide by the new exponent </strong>
</p>

```math
\frac{x^6}{6}+C
```

Final answer,

```math
\boxed{\frac{x^6}{6}+C}
```

#### Example 2 - Integrating a coefficient

Evaluate,

```math
\int 6x^3\,dx
```

The coefficient $6$ remains as a constant multiplier while applying the power rule.

<p>
&nbsp;&nbsp;&nbsp;&nbsp; <strong> Step 1 - Add one to the exponent </strong>
</p>

```math
3+1=4
```

<p>
&nbsp;&nbsp;&nbsp;&nbsp; <strong> Step 2 - Divide by the new exponent </strong>
</p>

```math
=6\left(\frac{x^4}{4}\right)+C
```

Simplifying,

```math
=\frac{6x^4}{4}+C
```

Final answer,

```math
\boxed{\frac{3}{2}x^4+C}
```

#### Example 3 - Integrating a negative exponent

Evaluate,

```math
\int x^{-3}\,dx
```

<p>
&nbsp;&nbsp;&nbsp;&nbsp; <strong> Step 1 - Add one to the exponent </strong>
</p>

```math
-3+1=-2
```

<p>
&nbsp;&nbsp;&nbsp;&nbsp; <strong> Step 2 - Divide by the new exponent </strong>
</p>

```math
=\frac{x^{-2}}{-2}+C
```

Simplifying,

```math
=-\frac{1}{2}x^{-2}+C
```

Using the laws of indices,

```math
\boxed{-\frac{1}{2x^2}+C}
```

#### Example 4 - Integrating a constant

Evaluate,

```math
\int 7\,dx
```

A constant can be rewritten using a zero exponent,

```math
\int 7x^0\,dx
```

<p>
&nbsp;&nbsp;&nbsp;&nbsp; <strong> Step 1 - Add one to the exponent </strong>
</p>

```math
0+1=1
```

<p>
&nbsp;&nbsp;&nbsp;&nbsp; <strong> Step 2 - Divide by the new exponent </strong>
</p>

```math
=7\left(\frac{x^1}{1}\right)+C
```

Final answer,

```math
\boxed{7x+C}
```

#### Example 5 - The special case of exponent -1

Evaluate,

```math
\int x^{-1}\,dx
```

The power rule cannot be applied because adding one to the exponent produces zero, resulting in division by zero.

Instead, we use the natural logarithm integration rule,

```math
\int x^{-1}\,dx=\ln|x|+C
```

The absolute value ensures that the logarithm's input is positive, allowing the expression to be defined for both positive and negative values of $x$, excluding zero.

```math
\boxed{\ln|x|+C}
```