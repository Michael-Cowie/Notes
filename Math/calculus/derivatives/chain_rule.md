<div align='center'>
    <h1> Chain Rule — Differentiating Composite Functions </h1>
</div>

Many functions are not formed from a single operation, but instead contain multiple layers of functions nested insde one another. These are known as **composite functions**. A composite function occurs when the output of one function becomes the input of another function. The chain rule is used whenever one function is applied to the output of another function. A general composite function is written as

```math
f(g(x))
```

where,

- $g(x)$ is called the inner function
- $f(x)$ is called the outer function

Examples can include,

1. $f(x) = \sin(2x)$. Where $\sin$ is the outer function and $2x$ is the inner function.

2. $f(x) = (3x + 1^5$. Where $u^5$ is the outer function and $3x +1$ is the inner function.

3. $f(x) = \sqrt{1 + x^3}$. First rewrite as $f(x) = (1 + x^3)^{\frac{1}{2}}$. The outer function is now $u^{\frac{1}{2}}$ and the inner function is $1 + x^3$.

The chain rule describes how derivatives behave when functions are composted together. It is written as

```math
\frac{d}{dx} f(g(x)) = f'(g(x)) \cdot g'(x)
```

<div align='center'>
    <img src='../images/32.png' width='400'>
</div>

This multiplication may appear confusing because function composition itself is not multiplication. When functions are composed, the output of one function is substituted into another function. However, derivatives do not describe the functions themselves. Instead, derivatives describe how small changes propagate through the functions.

When performing the chain rule it is common to introduce an intermediate variable such as $u$. Suppose we have,

```math
y = (x^2 + 3x)^8
```

This means,

- $x$ is the horizontal axis
- $y$ is the vertical axis

The graph itself only contains these two axes. However, the internal structure of the function may be decomposed into stages by introducing an intermediate quantity.

Define,

```math
\begin{aligned}
u &= x^2 + 3x \\
y &= u^8
\end{aligned}
```

This decomposition creates the dependency chain,

```math
x \to u \to y
```

It is important to understand that $u$ is not a new graph axis. The graph is still entirely determined by the relationship between $x$ and $y$. The variable $u$ is an intermediate quantity used to describe how changes propagate internally through the composite function. Changing $x$ changes $u$, and changing $u$ then changes $y$. The chain rule therefore studies how change cascades through these intermediate changes.

Differentiating both stages gives,

```math
\begin{aligned}
\frac{du}{dx} &= 2x + 3 \\
\frac{dy}{du} &= 8u^7
\end{aligned}
```

Now suppose $x = 1$, then

```math
u = 1^2 + 3(1) = 4
```

This means that at the point where $x = 1$, the corresponding intermediate value is $u = 4$. Now evaluate the derivatives at this point. First,

```math
\frac{du}{dx} = 2(1) + 3 = 5
```

This means that near $x = 1$, a small change in $x$ produces a change in $u$ that is approximately $5$ times as large. Symbolically,

```math
du = 5 dx
```

Next,

```math
\frac{dy}{du} = 8u^7
```

At the point where $u=4$

```math
\frac{dy}{du} = 8(4)^7
```

This means that near $u=4$, a small change in $u$ produces a change in $y$ that is approximately $8(4)^7$ times as large. Symbolically,

```math
dy = 8(4)^7 du
```

The important conceptual step is that the change produced by the first stage becomes the input change for the second stage. Since,

```math
\begin{aligned}
du &= 5 \, dx \\
dy &= 8(4)^7 \, du \\
dy &= 8(4)^7 \cdot 5 \, dx
\end{aligned}
```

Therefore,

```math
\frac{dy}{dx} = 8(4)^7 \cdot 5
```

<div align='center'>
    <img src='../images/18.png' width='600'>
</div>

The first derivative,

```math
\frac{du}{dx}
```

describes how changes in $x$ cascades changes in $u$. The second derivative,

```math
\frac{dy}{du}
```

describes how changes in $u$ scale into changes in $y$.  Because the output change from the first derivative stage becomes the input for the second stage, the scaling factors multiply together. This produces the chain rule relationship.

```math
\frac{dy}{dx} = \frac{dy}{dy} \cdot \frac{du}{dx}
```

This relationship occurs because any small changes in $x$, increases $u$ which increases $y$.

## Understanding the Chain Rule

#### Example 1 — $y = (x + 1)^2$

When observing 

```math
y = (x + 1)^2
``` 

their are actually two operations happening.

1. Start with $x$
2. Add $1$ to get $x + 1$
3. Square the result

```math
x \xrightarrow{+1} x+1 \xrightarrow{\text{squared}} (x+1)^2
```

We can write this as,

```math
\begin{align*}
u &= x + 1 \\
y &= u^2
\end{align*}
```

Hence,

```math
x \xrightarrow{\frac{du}{dx}} u \xrightarrow{\frac{dy}{du}} y \\
\frac{dy}{dx} = \frac{du}{dx} \cdot \frac{dy}{du}
```

This means,

1. As $x$ changes, $u$ changes with respect so $x$ at a rate of $\frac{du}{dx}$
2. Moving forward, as $u$ changes, $y$ changes with respect to $u$ at a rate of $\frac{dy}{du}$

It therefore follows,

```math
\begin{align*}
\frac{du}{dx} &= 1 \\
\frac{dy}{du} &= 2(x+1) \\[6pt]
du &= 1 \cdot dx \\
dy &= 2(x+1)\,du \\
dy &= 2(x+1)\cdot 1 \cdot dx \\
dy &= 2(x+1)\,dx \\
\frac{dy}{dx} &= 2(x+1)
\end{align*}
```

#### Example 2 — $y = \sin(x^2)$

When observing

```math
y = \sin(x^2)
```

there are actually two operations happening

1. Start with $x$
2. Square it to get $x^2$
3. Take the sine of the result

```math
x \xrightarrow{\text{squared}} x^2 \xrightarrow{\sin} \sin(x^2)
```

We can write this as,

```math
\begin{aligned}
u &= x^2 \\
y &= \sin(u)
\end{aligned}
```

Hence,

```math
x \xrightarrow{\frac{du}{dx}} u \xrightarrow{\frac{dy}{du}} y \\
\frac{dy}{dx} = \frac{du}{dx} \cdot \frac{dy}{du}
```

This means,

1. As $x$ changes, $u$ changes with respect so $x$ at a rate of $\frac{du}{dx}$
2. Moving forward, as $u$ changes, $y$ changes with respect to $u$ at a rate of $\frac{dy}{du}$


It therefore follows,

```math
\begin{aligned}
\frac{du}{dx} &= 2x \\
\frac{dy}{du} &= \cos(u) \\
du &= 2x \, dx \\
dy &= \cos(u)\, du \\
dy &= \cos(u)\cdot 2x \, dx \\
\frac{dy}{dx} &= 2x \cos(u) \\
\frac{dy}{dx} &= 2x \cos(x^2)
\end{aligned}
```

#### Multiple Functions

This can also expand to more complicated scenarios where we get more terms, but the idea remains the same.

<div align='center'>
    <img src='../images/33.jpg' width='400'>
</div>

Consider the function

```math
y = \cos^2(4x)
```

Now, break it down into separate variables.

```math
\begin{aligned}
h(x) &= 4x \\
g(u) &= \cos(u) \\
f(v) &= v^2
\end{aligned}
```

which gives

```math
f(g(h(x))) = \cos^2(4x)
```

This notation explicitly separates the function into a sequence of individual operations. Beginning with an input $x$,

```math
h(x) = 4x
```

multiplies the input by $4$. The result is then passed into,

```math
g(u) = \cos(u)
```

which applies the cosine function. Finally,

```math
f(v) = v^2
```

squares the result. The complete process can therefore be visualized as,

```math
x \to u \to v \to y
```

where

```math
\begin{aligned}
u &= h(x) \\
v &= g(u) \\
y &= f(v)
\end{aligned}
```

The important observation is that each stage produces a new quantity which becomes the input of the next stage. This interpretation is often the most natural way to understand the chain rule because it exposes every intermediate step. Each quantity depends only on the quantity immediately before it. We may therefore ask three independent questions,

First,

```math
u = 4x
```

How rapidly does $u$ change with respect to $x$?

```math
\frac{du}{dx} = 4
```

Second,

```math
v = \cos(u)
```

How rapidly does $v$ change with respect to $u$?

```math
\frac{dv}{du} = -\sin(u)
```

Third,

```math
y = v^2
```

How rapidly does $y$ change with respect to $v$?

```math
\frac{dy}{dv} = 2v
```

Notice that these derivatives are not introduced arbitrarily. Each one simply measures the rate of change between two neighbouring stages of the composition. The chain rule states that the overall rate of change from $x$ to $y$ is obtained by multiplying the rates of change at each stage.

```math
\frac{dy}{dx} = \frac{dy}{dv} \cdot \frac{dv}{du} \cdot \frac{du}{dx}
```

Substituting the derivatives gives,

```math
\frac{dy}{dx} (2v)(-\sin(u))(4)
```

which produces

```math
\frac{dy}{dx} = 2\cos(4x)(-\sin(4x))(4) = -8\cos(4x)\sin(4x)
```

#### Example 1 - Function Composite View

Let,

```math
y = (x^2 + 1)^3
```

Observing the expression, it appears that the power rule could potentially be used because their is an exponent of $3$. But the subtle issue is that the thing being cubed is not simply $x$. This is where the chain rule is used.

This expression contains two nested functions. Define the inner function as

```math
g(x) = x^2 + 1
```

and define the outer function as

```math
f(u) = u^3
```

The original function can now be viewed as,

```math
y = f(g(x))
```

The chain rule now be easier to apply. First, differentiate both equations.

```math
\begin{aligned}
g'(x) &= 2x \\
f'(u) &= 3u^2
\end{aligned}
```

The chainrule therefore states,

```math
\begin{aligned}
\frac{d}{dx} f(g(x))
&= 3(x^2 + 1)^2 \cdot 2x \\
\\
\frac{d}{dx} f(g(x))
&= 6x(x^2 + 1)^2
\end{aligned}
```

#### Example 2 - Function Composite View with Leibniz Notation

Let,

```math
y = (x^2 + 3x)^8
```

First perform a substitution,

```math
\begin{aligned}
u &= x^2 + 3x
\\

\frac{du}{dx} &= 2x + 3
\end{aligned}
```

Which follows,

```math
\begin{aligned}
y &= u^8
\\

\frac{dy}{du} &= 8u^7
\end{aligned}
```

Therefore,

```math
\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} = 8u^7 \cdot (2x + 3) = 8(x^2 + 3x)^7 (2x + 3)
```

#### Example 3 - Substitution and the Power Rule

As an illustrative example, we can perform substitution to use the power rule and compare this to using the chain rule.

Given,

```math
y = (x^2 + 1)^3
```

we define a temporary variable,

```math
z = x^2 + 1
```

The function now becomes $y = z^3$. At this stage, the ordinary power rule can be applied directly.

```math
\begin{aligned}
y &= z^3 \\
\frac{dy}{dz} &= 3z^2
\end{aligned}
```

Differentiating $z = x^2 + 1$ gives

```math
\frac{dz}{dx} = 2x
```

The total rate of change of $y$ with respect to $x$ must therefore include both stages of change.

1. How $y$ changes with respect to $z$
2. How $z$ changes with respect to $x$

The chain rule combines these together.

```math
\frac{dy}{dx} = \frac{dy}{dz} \cdot \frac{dz}{dx}
```

It therefore follows,

```math
\begin{aligned}
3z^2 \cdot 2x \,
\frac{dy}{dz}
\cdot
\frac{dz}{dx}
\\

3z^2 \cdot 2x \,
\frac{dy}{\cancel{dz}}
\cdot
\frac{\cancel{dz}}{dx}
\\

3z^2 \cdot 2x \,
\frac{dy}{dx}
\\

3(x^2 + 1)^2 \cdot 2x \,
\frac{dy}{dx}
\\

6x(x^2 + 1)^2 \,
\frac{dy}{dx}
\end{aligned}
```

## Chain Rule Proof

Given $y = f(g(x))$

```math
\begin{aligned}
\frac{dy}{dx}

&= \lim_{h \rightarrow 0} \frac{f(x + h) - f(x)}{h} \\

&= \lim_{h \to 0} \frac{f(g(x + h)) - f(g(x))}{h} \\

&= \lim_{h \to 0}
\frac{f(g(x + h)) - f(g(x))}{h}
\cdot
\frac{g(x+h) - g(x)}{g(x+h) - g(x)} \\

&= \lim_{h \to 0}
\frac{f(g(x + h)) - f(g(x))}{g(x+h) - g(x)}
\cdot
\frac{g(x+h) - g(x)}{h} \\

&= \left(
\lim_{h \to 0}
\frac{f(g(x + h)) - f(g(x))}{g(x+h) - g(x)}
\right)
\cdot
\left(
\lim_{h \to 0}
\frac{g(x+h) - g(x)}{h}
\right) \\

&=
\lim_{h \to 0}
\frac{f(g(x + h)) - f(g(x))}{g(x+h) - g(x)}
\cdot g'(x)
\end{aligned}
```

Now, we introduce a new variable.

```math
\begin{aligned}
k &= g(x+h) - g(x) \\
g(x+h) &= g(x) + k
\end{aligned}
```

When I write $k = g(x + h) - g(x)$, the value of $k$ depends on whatever value of $h$ you choose (with $x$ fixed). So more formally, $k$ is not an independent variable. Instead, it is a function of $h$,

```math
k(h) = g(x + h) - g(x)
```

Because $g$ is differentiable, it is continuous, so as $h \to 0$, we have $k \to 0$. 

```math
\lim_{h \to 0} k = \lim_{h \to 0} g(x + h) - g(x) = 0
```

Because every value of $k$ near $0$ corresponds to some $h$ near $0$, the limit of $h$ approaches $0$ is the same limit as $k$ approaches $0$ of the new expression.

```math
\lim_{h \to 0} \frac{f(g(x+h)) - f(g(x))}{g(x+h)-g(x)} = \lim_{k \to 0} \frac{f(g(x)+k) - f(g(x))}{k}
```

It therefore follows,

```math
\begin{aligned}
\frac{dy}{dx}



&=
\lim_{h \to 0}
\frac{f(g(x + h)) - f(g(x))}{g(x+h) - g(x)}
\cdot g'(x) \\

&= \lim_{k \to 0} \frac{f(g(x) + k) - f(g(x))}{k} \cdot g'(x) \\

&= f'(g(x)) \cdot g'(x) \\

\end{aligned}
```

In a complete form this is written as,

```math
\frac{dy}{dx} = \lim_{k \to 0} \frac{f(g(x) + k) - f(g(x))}{k} \cdot \lim_{h \to 0}
\frac{g(x+h) - g(x)}{h}
```