<div align='center'>
    <h1> Multiple Rule Usage </h1>
</div>

Differentiation is founded upon a collection of fundamental rules, each designed to describe a particular structural relationship within a function.

- The constant rules applies to constants.
- The power rule to powers of a variable.
- The product rule to products of functions.
- The chain rule to composite functions.

As functions become more sophisticated, it is common for several of these structures to appear simultaneously within a single expression. Consequently, successful differentiation requires not only knowledge of the individual rules, but also the ability to recognise how they interact and the order in which they should be applied.

<div align='center'>
    <h1> Identification </h1>
</div>

When several rules appear applicable, it is useful to **identify the outmost structure of the function first**. For example,

```math
\sin(x^2)e^x
```

has an outer multiplication structure. Therefore, the product rule must be applied first. In contrast,

```math
(\sin(x) \cdot e^x)^3
```

has an outer power structure. Therefore, the chain rule must be applied first. The outermost structure determines the first rule used.

<div align='center'>
    <h1> Product Rule with Chain Rules Inside </h1>
</div>

A common situation occurs when the function is a product, but each factor is itself a composite function.

#### Example 1

```math
y = \sin(x^2) \cdot e^{3x}
```

The outer structure is,

```math
(\text{function}) \cdot (\text{function})
```

We begin by identifying,

```math
\begin{aligned}
f(x) &= \sin(x^2) \\
g(x) &= e^{3x}
\end{aligned}
```

Therefore,

```math
\frac{dy}{dx} = f'(x)g(x) + f(x)g'(x)
```

For $f(x)$, we introduce an intermediate variable.

```math
\begin{aligned}
t &= x^2 \\
f &= \sin(t) \quad \text{or} \quad f(t) = \sin(t)
\end{aligned}
```

so,

```math
\begin{aligned}
\frac{dt}{dx} &= 2x \\
\frac{df}{dt} &= \cos(t)
\end{aligned}
```

Which follows,

```math
\frac{df}{dx} = f'(x) = \frac{df}{dt} \frac{dt}{dx} = 2x \cos(x^2)
```

Similarily,

```math
g = e^{3x}
```

Let,

```math
s = 3x
```

Which follows,

```math
g = e^s
```

Therefore,

```math
\begin{aligned}
\frac{ds}{dx} &= 3 \\
\frac{dg}{ds} &= e^s \\
\frac{dg}{dx} &= 3e^{3x}
\end{aligned}
```

Putting everything together,

```math
\frac{dy}{dx} = \frac{d}{dx}(f(x)g(x)) = \frac{d}{dx}(fg) = \frac{df}{dx}g + f\frac{dg}{dx}
```

Illustration of the chain rule behaviour here,

```math
\begin{aligned}
\frac{dy}{dx}
&= \left(\frac{df}{dt}\frac{dt}{dx}\right)e^{3x}
+ \sin(x^2)\left(\frac{dg}{ds}\frac{ds}{dx}\right) \\
&= (\cos(x^2)\cdot 2x)e^{3x}
+ \sin(x^2)(e^{3x}\cdot 3) \\
&= 2x\cos(x^2)e^{3x} + 3\sin(x^2)e^{3x}
\end{aligned}
```

#### Example 2

Consider

```math
y = (x^2 + 1)^5 \cdot \cos(3x)
```

The outer structure is again a product. Let,

```math
\begin{aligned}
f(x) &= (x^2 + 1)^5 \\
g(x) &= \cos( 3x) \\
\frac{dy}{dx} &= f'(x) \cdot g(x) + f(x) + g'(x)
\end{aligned}
```

Now for $f(x) = (x^2 +1)^5$, let

```math
\begin{aligned}
u &= x^2 + 1 \\
\frac{du}{dx} &= 2x
\end{aligned}
```

and

```math
\begin{aligned}
f(x) &= u^5 \\
\frac{df}{du} &= 5u^4
\end{aligned}
```

Therefore,

```math
f'(x) = \frac{df}{dx} = 10x(x^2 + 1)^4
```

Now,

```math
g(x) = \cos(3x)
```

This follows,

```math
\begin{aligned}
u &= 3x \\
\frac{du}{dx} &= 3 \\
g(x) &= \cos(u) \\
\frac{dg}{du} &= -\sin(u) \\
\frac{dg}{dx} &= -3\sin(3x)
\end{aligned}
```

Because,

```math
\frac{dy}{dx} = f'(x) \cdot g(x) + f(x) + g'(x)
```

Where,

```math
\begin{aligned}
f(x) &= (x^2 + 1)^5 \\
g(x) &= \cos( 3x) \\
f'(x) &= 10x(x^2 + 1)^4 \\
g'(x) &= -3\sin(3x)
\end{aligned}
```

It follows,

```math
\frac{dy}{dx} = 10x(x^2 + 1)^4 \cdot \cos(3x) - 3(x^2 + 1)^5 \cdot \sin(3x)
```

<div align='center'>
    <h1> Chain Rule with Product Rules Inside </h1>
</div>

Another possibility is that the overall function is composite, but the inner function contains a product. In these cases, the chain rule is applied first, and the product rule appears when differentiating the inner function.

#### Example 1

Consider

```math
y = \sin(xe^{x})
```

Let,

```math
\begin{aligned}
f(x) &= \sin(x) \\
g(x) &= xe^{x}
\end{aligned}
```

Hence,

```math
y = f(g(x)) = \sin(xe^{x})
```

Because 

```math
\frac{dy}{dx} = f'(g(x)) \cdot g'(x)
```

Now,

```math
\begin{aligned}
f'(x) &= \cos(x) \\
g'(x) &= e^{x} + xe^{x} \quad (\text{Using the product rule}) \\
f'(g(x)) &= f'(xe^x) = \cos(xe^x)
\end{aligned}
```

Therefore,

```math
\frac{dy}{dx} = f'(g(x)) \cdot g'(x) = \cos(xe^x) \cdot (e^x + xe^x)
```

#### Example 2

Consider

```math
y = (x \sin(x))^4
```

The outer structure is a power. Let,

```math
\begin{aligned}
f(x) &= x^4 \\
g(x) &= x\sin(x) \\
f(g(x)) &= f(x\sin(x)) = (x \sin(x))^4
\end{aligned}
```

Now,

```math
\begin{aligned}
f'(x) &= 4x^3 \\
g'(x) &= \sin(x) + x\cos(x) \quad (\text{Using the product rule}) \\
f'(g(x)) &= f'(x\sin(x)) = 4(x\sin(x))^3
\end{aligned}
```

Therefore,

```math
\frac{dy}{dx} = f'(g(x)) \cdot g'(x) = 4(x\sin(x))^3 \cdot (\sin(x) + x\cos(x))
```