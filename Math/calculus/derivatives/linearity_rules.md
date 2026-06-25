<div align='center'>
    <h1> Linearity Rules — Addition and Constant Multiplication </h1>
</div>

Differentiation also respects basic algebraic structure. Two key properties are linearity rules.

```math
\frac{d}{dx}[f(x) + g(x)] = f'(x) + g'(x)
```

and

```math
\frac{d}{dx}[c \cdot f(x)] = c \cdot f'(x)
```

where $c$ is a constant.

These rules state that differentiation distributes across addition and factors through constants. In other words, each part of a function can be differentiated independently before being combined. For example

```math
\frac{d}{dx} (x^2 + x^3) = 2x + 3x^2
```

These properties are essential because they allow complex espressions to be broken into simpler components. Without linearity, differentiation would require full limit expansion for every expression, making calculus far less practical. We can try to visualize this by observing the behaviour in

```math
\begin{aligned}

\frac{d}{dx}(g(x) + h(x))
&= \frac{dg}{dx} + \frac{dh}{dx}

\\

\frac{d}{dx}(\sin(x) + x^2)
&= \cos(x) + 2x
\end{aligned}
```

<div align='center'>
    <img src='../images/15.png' width='600'>
</div>

Now, if we zoom in and take the point at $x = 0.5$, we create a new variable $df$ where

```math
df = d(\sin(x)) + d(x^2)
```

In this example $d$ means "differential" or "the tiny change". So $d(\sin(x))$ means "the tiny change in the quantity $\sin(x)$". Because $y = \sin(x)$, this is exactly the same as writing $dy$. Therefore,

```math
\begin{aligned}
dy &= d(\sin(x)) = \cos(x) \ dx
\\

dy &= d(x^2) = 2x \ dx
\end{aligned}
```

<div align='center'>
    <img src='../images/16.png' width='600'>
</div>

We know that,

```math
\begin{aligned}
y &= \sin(x)
\\

\frac{dy}{dx} &= \cos(x)
\\

dy &= \cos(x)\,dx
\end{aligned}
```
Additionally,

```math
\begin{aligned}
y &= x^2
\\

\frac{dy}{dx} &= 2x
\\

dy &= 2x\,dx
\end{aligned}
```

It therefores follows,

```math
\begin{aligned}
df &= \cos(x)\,dx + 2x\,dx
\\

\frac{df}{dx} &= \cos(x) + 2x
\end{aligned}
```

This now suggests

```math
\frac{d}{dx} (g(x) + h(x)) = \frac{dg}{dx} + \frac{dh}{dx}
```

which the sum of derivatives of its part. This is also called the sum rule.