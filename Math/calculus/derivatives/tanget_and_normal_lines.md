<div align='center'>
    <h1> Finding the Tangent Line and Normal Line </h1>
</div>

When studying curves, two of the most important lines are the **tangent** and the **normal**. Below, we will explain the process for solving both for the curve

```math
y = x^2
```

at the point where

```math
x = 3
```

We will therefore be studying the behaviour at the point

```math
(3, 9)
```

#### Tangent Line

The tangent line touches the curve at a single point and has the **same gradient as the curve at that point**. To find the tangent line, we first need its gradient. The derivative of the function gives the gradient of the curve at every value of $x$

```math
\frac{dy}{dx} = 2x
```

At $x=3$,

```math
\frac{dy}{dx} = 2(3) = 6
```

Therefore, the tangent line has gradient

```math
m = 6
```

The equation of a straight line can be written as

```math
y - y_1 = m(x - x_1)
```

- The point $(x_1, y_1)$ is simply a known point on the line.
- The symbols $(x, y)$ represent any other point on the line.

For our equation,

```math
(x_1, y_1) = (3, 9)
```

The expression $y - y_1$ represents the vertical displacement from the known point to another point on the line. Likewise, $x - x_1$ represents the horizontal displacement. This means, we need to create an equation such that for every $x$ value, when comparing it to our point, it must have the same gradient value of $6$. Therefore, the equation becomes

```math
\begin{aligned}
y - y_1 &= m(x - x_1) \\
y - 9 &= 6(x - 3) \\
y - 9 &= 6x - 18 \\
y &= 6x - 9
\end{aligned}
```

<div align='center'>
    <img src='../images/34.png' width='400'>
</div>

#### Normal Line

The normal line is **perpendicular** to the tangent line and also passes through the same point on the curve. This occurs when the two lines meet and create a $90^\circ$ angle.

Suppose we have a linear graph with a $\Delta y = a$ and $\Delta x = b$, therefore $m = \frac{\Delta y}{\Delta x} = \frac{a}{b}.$

<div align='center'>
    <img src='../images/35.png' width='400'>
</div>

A perpendicular line is a line that meets at $90^\circ$. It's best to visualize this with an example, so we will simply rotate the current linear graph by $90^\circ$.

<div align='center'>
    <img src='../images/36.png' width='400'>
</div>

<div align='center'>
    <img src='../images/37.jpg' width='400'>
</div>

Now, we can observe the behaviour of both gradients. The tangent line has a gradient $\frac{a}{b}$ and our normal line has a gradient $\frac{-b}{a}$. It therefore follows,

```math
m_{\text{tan}} \cdot m_{\text{norm}} = \frac{a}{b} \cdot \frac{-b}{a} = \frac{-ab}{ba} = -1
```

<div align='center'>
    <img src='../images/38.png' width='400'>
</div>

This tells us crucial information. If we created a linear graph tangent to the curve with gradient $m$, the normal graph of our linear graph must have a gradient of $-\frac{1}{m} = -\frac{1}{6}$. Using the previous line equation at point $(3, 9)$,

```math
\begin{aligned}
y - y_1 &= m(x - x_1) \\
y - 9 &= -\frac{1}{6}(x - 3) \\
y - 9 &= -\frac{x}{6} + \frac{3}{6} \\
y &= -\frac{x}{6} + \frac{3}{6} + 9 \\
y &= -\frac{x}{6} + \frac{1}{2} + 9 \\
y &= -\frac{x}{6} + \frac{19}{2}
\end{aligned}
```

<div align='center'>
    <img src='../images/39.png' width='400'>
</div>