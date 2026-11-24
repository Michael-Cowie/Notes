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