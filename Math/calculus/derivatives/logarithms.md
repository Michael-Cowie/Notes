<div align='center'>
    <h1> Logarithms </h1>
</div>
Logarithmic functions are an important class of functions in calculus. They are commonly used to describe relationships involving exponential growth, decay, and proportional change. To differentiate logarithmic functions, we first need to establish the derivative of the natural logarithm, $\ln(x)$, which provides the foundation for differentiating logarithms of any positive base.  The derivative of the natural logarithm is,

```math
\frac{d}{dx}\ln(x)=\frac{1}{x}
```

This result can be established using the first principles of differentiation, specifically the difference quotient. Once this relationship has been proven, we can extend it to logarithms with arbitrary bases using the laws of logarithms and the chain rule.

## Proof of the Derivative of $\ln(x)$

Before differentiating logarithmic functions, we must establish why the derivative of the natural logarithm is equal to $\frac{1}{x}$. The derivative of a function $f(x)$ can be defined using the difference quotient,

```math
f'(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}
```

This definition measures the average rate of change between two points on a function. As the horizontal distance between these points, $h$, approaches zero, the average rate of change approaches the instantaneous rate of change, which is the derivative.

<p>
&nbsp;&nbsp;&nbsp;&nbsp; <strong> Step 1: Apply the difference quotient </strong>
</p>

Let,

```math
f(x)=\ln(x)
```

Substituting this function into the difference quotient gives,

```math
f'(x)=\lim_{h\to 0}\frac{\ln(x+h)-\ln(x)}{h}
```

<p>
&nbsp;&nbsp;&nbsp;&nbsp; <strong> Step 2: Apply the laws of logarithms </strong>
</p>

One of the fundamental logarithmic identities states,

```math
\log_b(a)-\log_b(c)=\log_b\left(\frac{a}{c}\right)
```

Applying this identity allows us to combine the two logarithms,

```math
f'(x)=\lim_{h\to 0}\frac{\ln\left(\frac{x+h}{x}\right)}{h}
```

We can then simplify the fraction inside the logarithm,

```math
f'(x)=\lim_{h\to 0}\frac{\ln\left(1+\frac{h}{x}\right)}{h}
```

<p>
&nbsp;&nbsp;&nbsp;&nbsp; <strong> Step 3: Introduce a substitution </strong>
</p>

To simplify the expression further, we introduce a substitution,

```math
u=\frac{h}{x}
```

Rearranging gives,

```math
h=ux
```

We can now substitute these expressions into our original difference quotient. However, we must also account for the change in the limiting variable. Originally, our limit was defined as $h\to0$. Since $h=ux$, we must initially express this as,

```math
h=ux\to0
```

Therefore, substituting $u=\frac{h}{x}$ and $h=ux$ into the difference quotient gives,

```math
f'(x)=\lim_{ux\to0}\frac{\ln(1+u)}{ux}
```

Since $x$ is treated as a fixed, nonzero constant, $ux\to0$ is equivalent to $u\to0$. We can therefore rewrite the limit as,

```math
f'(x)=\lim_{u\to0}\frac{\ln(1+u)}{ux}
```

Since $x$ is independent of the limit, we can take it outside,

```math
f'(x)=\frac{1}{x}\lim_{u\to0}\frac{\ln(1+u)}{u}
```

<p>
&nbsp;&nbsp;&nbsp;&nbsp; <strong> Step 4: Evaluate the limit and substitute it back into the derivative </strong>
</p>

We have now reduced the original difference quotient to a simpler limit,

```math
\lim_{u\to0}\frac{\ln(1+u)}{u}
```

This limit evaluates to 1. Keep in mind, this limit is for $\ln$ only, not any logarith function with base $b$. Substituting this result back into our expression,

```math
f'(x)=\frac{1}{x}(1)
```

Therefore,

```math
\boxed{\frac{d}{dx}\ln(x)=\frac{1}{x}}
```

**What does this result mean?**

The derivative of $\ln(x)$ describes how quickly the natural logarithm changes as $x$ increases. The result $\frac{1}{x}$ tells us that its rate of change is inversely proportional to its input.

For example,

- $x=1$, the gradient of the function is 1. 
- $x=2$, the gradient is $\frac{1}{2}$
- ...

This demonstrates that although the natural logarithm continues to increase as $x$ increases, its rate of increase becomes progressively smaller.

## Introduction to Logarithms

A logarithm is the inverse operation of exponentiation. It determines the exponent to which a particular base must be raised to produce a given number. The general definition of a logarithm is, if

```math
b^x=y
```

Then,

```math
\log_b(y)=x
```

Where,
- $b$ is the base of the logarithm.
- $x$ is the exponent.
- $y$ is the resulting value.

For example,

```math
2^3=8
```

Can be rewritten as,

```math
\log_2(8)=3
```

This means that the logarithm of 8 with base 2 is 3 because 2 must be raised to the power of 3 to produce 8.

**The natural logarithm**

The natural logarithm is a special type of logarithm that uses the mathematical constant $e$ as its base. The constant $e$ is an irrational number approximately equal to,

```math
e\approx 2.71828
```

The natural logarithm is conventionally written as,

```math
\ln(x)=\log_e(x)
```

Therefore, the natural logarithm asks the question, to what power must $e$ be raised to produce $x$? For example, raising $e$ to the power of 2 gives approximately 7.389,

```math
e^2\approx 7.389
```

So the natural logarithm of 7.389 must be 2,

```math
\ln(7.389)\approx 2
```

Two special cases follow from the same idea. Since $e$ raised to the power of 1 is $e$, and $e$ raised to the power of 0 is 1,

```math
\ln(e)=1
\qquad
\ln(1)=0
```

In general, $\ln$ and $e^x$ undo each other,

```math
\ln(e^x)=x
```

The natural logarithm is particularly important in calculus because the exponential function $e^x$ and its inverse, $\ln(x)$, have especially useful differentiation properties.

**Important logarithmic identities**

Several logarithmic identities are particularly useful when differentiating logarithmic functions.

The product rule,

```math
\log_b(xy)=\log_b(x)+\log_b(y)
```

The quotient rule,

```math
\log_b\left(\frac{x}{y}\right)=\log_b(x)-\log_b(y)
```

The power rule,

```math
\log_b(x^n)=n\log_b(x)
```

These identities allow logarithmic expressions to be expanded, combined, and simplified before or during differentiation.

## Differentiation of Logarithms

Having established that the derivative of the natural logarithm is $\frac{1}{x}$, we can now extend this result to logarithms with any positive base.

**Differentiating logarithms with different bases**

Consider the general logarithmic function,

```math
y=\log_b(x)
```

Using the change-of-base formula, we can rewrite this expression in terms of natural logarithms,

```math
y=\frac{\ln(x)}{\ln(b)}
```

Since $b$ is a constant, $\ln(b)$ is also a constant. We can therefore differentiate using the constant multiple rule,

```math
\frac{dy}{dx}=\frac{1}{\ln(b)}\frac{d}{dx}\ln(x)
```

Using the derivative established in the previous section,

```math
\frac{dy}{dx}=\frac{1}{\ln(b)}\cdot\frac{1}{x}
```

Therefore, the general derivative of a logarithm is,

```math
\boxed{\frac{d}{dx}\log_b(x)=\frac{1}{x\ln(b)}}
```

This formula applies to logarithms with any positive base, provided that the base is not equal to 1.

### Differentiating logarithms using the chain rule

The previous proof established that the derivative of the natural logarithm is,

```math
\frac{d}{dx}\ln(x)=\frac{1}{x}
```

However, this proof specifically considered the natural logarithm of $x$. When the expression inside the logarithm is a function of $x$, we must apply the chain rule to account for the rate of change of that inner function.

Consider,

```math
y=\ln(u)
```

Where $u$ is a function of $x$. To differentiate this expression, we can separate it into an inner function and an outer function,

```math
x \xrightarrow{\frac{du}{dx}} u \xrightarrow{\frac{dy}{du}} y \\
\frac{dy}{dx} = \frac{du}{dx} \cdot \frac{dy}{du}
```

We already established that the derivative of the natural logarithm is the reciprocal of its input. Therefore,

```math
\frac{dy}{du}=\frac{1}{u}
```

Substituting this into the chain rule,

```math
\frac{dy}{dx}=\frac{du}{dx}\cdot\frac{1}{u}
```

Rearranging gives,

```math
\boxed{\frac{dy}{dx}=\frac{u'}{u}}
```

Therefore, the general derivative of a natural logarithm containing a function of $x$ is,

```math
\boxed{\frac{d}{dx}\ln(u)=\frac{u'}{u}}
```

This result can be extended to logarithms with an arbitrary base using the change-of-base formula,

```math
\log_b(u)=\frac{\ln(u)}{\ln(b)}
```

Since the base $b$ is constant, differentiating gives,

```math
\frac{d}{dx}\log_b(u)=\frac{1}{\ln(b)}\cdot\frac{d}{dx}\ln(u)
```

Substituting the chain rule result,

```math
\boxed{\frac{d}{dx}\log_b(u)=\frac{u'}{u\ln(b)}}
```

Therefore, when differentiating a logarithm, we divide the derivative of its inner function by the original inner function. For natural logarithms, this is simply $\frac{u'}{u}$, while logarithms with an arbitrary base introduce the additional constant factor $\frac{1}{\ln(b)}$.

**An important distinction:** When the argument of the logarithm is simply $x$, its derivative is 1. Consequently, the original formula is a special case of the more general chain rule formula,

```math
\frac{d}{dx}\log_b(x)=\frac{1}{x\ln(b)}
```

When the argument is a more complicated function, we must also differentiate that function using the chain rule.

## Worked Examples

The following examples demonstrate how the differentiation rules can be applied to logarithmic functions with different bases and arguments.

#### Example 1: Differentiating a natural logarithm

Differentiate,

```math
y=\ln(x)
```

Using the derivative established earlier,

```math
\frac{d}{dx}\ln(x)=\frac{1}{x}
```

Therefore,

```math
\boxed{\frac{dy}{dx}=\frac{1}{x}}
```

This is the fundamental differentiation rule for natural logarithms.

#### Example 2: Differentiating a logarithm with a different base

Differentiate,

```math
y=\log_2(x)
```

<p>
&nbsp;&nbsp;&nbsp;&nbsp; <strong> Step 1: Apply the general logarithmic derivative rule </strong>
</p>

```math
\frac{d}{dx}\log_b(x)=\frac{1}{x\ln(b)}
```

<p>
&nbsp;&nbsp;&nbsp;&nbsp; <strong> Step 2: Substitute the base </strong>
</p>

Since the base is 2,

```math
\frac{dy}{dx}=\frac{1}{x\ln(2)}
```

Therefore,

```math
\boxed{\frac{dy}{dx}=\frac{1}{x\ln(2)}}
```


#### Example 3: Differentiating a natural logarithm using the chain rule


Differentiate,

```math
y=\ln(3x+2)
```

<p>
&nbsp;&nbsp;&nbsp;&nbsp; <strong> Step 1: Identify the inner function </strong>
</p>

Let,

```math
u=3x+2
```

Differentiating the inner function gives,

```math
\frac{du}{dx}=3
```

<p>
&nbsp;&nbsp;&nbsp;&nbsp; <strong> Step 2: Apply the chain rule </strong>
</p>

The general differentiation rule is,

```math
\frac{d}{dx}\ln(u)=\frac{u'}{u}
```

Substituting our inner function and its derivative,

```math
\frac{dy}{dx}=\frac{3}{3x+2}
```

Therefore,

```math
\boxed{\frac{dy}{dx}=\frac{3}{3x+2}}
```

The chain rule requires us to differentiate the inner expression and divide by the original inner expression.

#### Example 4: Differentiating a natural logarithm containing a polynomial

Differentiate,

```math
y=\ln(x^2+4)
```

<p>
&nbsp;&nbsp;&nbsp;&nbsp; <strong> Step 1: Identify the inner function </strong>
</p>

Let,

```math
u=x^2+4
```

Differentiating gives,

```math
\frac{du}{dx}=2x
```

<p>
&nbsp;&nbsp;&nbsp;&nbsp; <strong> Step 2: Apply the chain rule </strong>
</p>

Using,

```math
\frac{d}{dx}\ln(u)=\frac{u'}{u}
```

Substituting the inner function and its derivative,

```math
\frac{dy}{dx}=\frac{2x}{x^2+4}
```

Therefore,

```math
\boxed{\frac{dy}{dx}=\frac{2x}{x^2+4}}
```

Notice that the derivative of the inner function becomes the numerator, while the original inner function remains in the denominator.

#### Example 5: Differentiating a logarithm containing a fraction

Differentiate,

```math
y=\ln\left(\frac{x+1}{x-1}\right)
```

<p>
&nbsp;&nbsp;&nbsp;&nbsp; <strong> Step 1: Apply the quotient identity for logarithms </strong>
</p>

Using,

```math
\ln\left(\frac{a}{b}\right)=\ln(a)-\ln(b)
```

We can rewrite the original expression,

```math
y=\ln(x+1)-\ln(x-1)
```

<p>
&nbsp;&nbsp;&nbsp;&nbsp; <strong> Step 2: Differentiate each term </strong>
</p>

Applying the chain rule to both logarithms,

```math
\frac{dy}{dx}=\frac{1}{x+1}-\frac{1}{x-1}
```

<p>
&nbsp;&nbsp;&nbsp;&nbsp; <strong> Step 3: Find a common denominator </strong>
</p>

```math
\frac{dy}{dx}=\frac{x-1}{(x+1)(x-1)}-\frac{x+1}{(x+1)(x-1)}
```

Combining the numerators,

```math
\frac{dy}{dx}=\frac{x-1-x-1}{(x+1)(x-1)}
```

Simplifying,

```math
\frac{dy}{dx}=\frac{-2}{(x+1)(x-1)}
```

Expanding the denominator,

```math
\frac{dy}{dx}=\frac{-2}{x^2-1}
```

Therefore,

```math
\boxed{\frac{dy}{dx}=\frac{-2}{x^2-1}}
```

This example demonstrates how logarithmic identities can simplify an expression before differentiation, making the application of the chain rule more straightforward.