<div align='center'>
    <h1> Power Rule — $\frac{d}{dx}(x^n)$ </h1>
</div>

One of the most fundamental rules in calculus is the power rule. It is written as,

```math
\frac{d}{dx} (x^n) = nx^{n-1}
```

This rule states that when differentiating a power of $x$, the exponent is brought down as a multiplier and the exponent is reduced by $1$.

```math
\begin{aligned}
\frac{d}{dx}(x^3) &= 3x^2 \\
\frac{d}{dx}(x^5) &= 5x^4
\end{aligned}
```

The power rule is significant because it reveals a consistent pattern in how polynomial functions change. Each increase in $x$ produces a predictable change in slope and differentiation systematically reduces the degree of the function while preserving its structure.

A common misunderstanding in early calculus comes from interpreting notation such as

```math
f(x) = x^4 + x^x
```

as meaning the entire function must match a derivative rule exactly before the rule can be used. Since the power rule is written as,

```math
\frac{d}{dx}(x^n) = nx^{n-1}
```

it may seem that the rule only applies when the whole function is a single power such as $x^5$ or $x^{10}$. However, this interpretation overlooks an important fact, derivative rules are not only rules about whole functions, but also rules about how derivatives interact with algebraic operations such as addition.

The expression

```math
x^4 + x^3
```

is not a single object of the form $x^n$. It is an addition operation joining two separate functions together.

```math
x^4 + x^3 = f(x) + g(x)
```

where

```math
f(x) = x^4 \qquad \text{and} \qquad g(x) = x^3
```

The derivative operator $\frac{d}{dx}$ has a special property called linearity. One consequence of linearity is the sum rule.

```math
\frac{d}{dx}(f(x) + g(x)) = \frac{d}{dx}f(x) + \frac{d}{dx}g(x)
```

This rule is logically separate from the power rule. The sum rule says that the differentiation passes through addition. In effect, the derivative operator distributes over sums in the same way multiplication distributes over addition in algebra. So when differentiating

```math
\frac{d}{dx} (x^4 + x^3)
```

the first step is not applying the power rule. The first step is applying the sum rule.

```math
\frac{d}{dx}(x^4 + x^3) = \frac{d}{dx}(x^4) + \frac{d}{dx}(x^3)
```

Only after the expression has been separated into individual pieces does the power rule become applicable, because each separate term now matches the structure $x^n$.

Then

```math
\frac{d}{dx}(x^4) = 4x^3
```

and

```math
\frac{d}{dx}(x^3) = 3x^2
```

giving

```math
\frac{d}{dx}(x^4 + x^3) = 4x^3 + 3x^2
```

The important conceptual distinction is that $f(x)$ names the entire function, but derivative rules act according to the internal algebraic structure of that function.

#### When to use the Power Rule

The power rule applies when a **variable is raised directly to a constant power**.

```math
\frac{d}{dx} (x^n) = nx^{n - 1}
```

Examples include

```math
\begin{align*}
x^5 \\
x^{12} \\
x^{\frac{1}{2}}
\end{align*}
```

For example,

```math
\frac{d}{dx}(x^3) = 5x^4
```

and

```math
\frac{d}{dx}(x^{\frac{1}{2}}) = \frac{1}{2}x^{-\frac{1}{2}}
```

The defining feature is that the base of the power is simply $x$. There is no additional function inside the exponentiation.

For instance,

```math
(x + 1)^2
```

looks similar to $x^2$, but the base is **no longer only** $x$. The quantity being squared is now $x + 1$. This introduces a layer of composition, and the chain rule becomes relevant. The reason the power rule is not directly applicable is that it implicitly a function inside another function. When observing $y = (x + 1)^2$, their are actually two operations happening.

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

#### Power Rule Visualized - 3D

Suppose we have a cube with side length $x$. The volume of the cube is given by

```math
y = V = x^3
```

where $V$ represents the volume.

<div align='center'>
    <img src='../images/21.png' width='500'>
</div>

If the side length is increased by an infinitesimal amount $dx$, then additional volume is created around the existing cube. The 3 largest contributions come from the 3 new rectangular prisms attached to the faces of the cube. Each has volume

```math
x^2 dx
```

giving a total contribution of

```math
x^2dx + x^2xdx + x^2x = 3x^2 dx
```

Additionally, there are three smaller edge prisms and one corner cube, highlighted in orange. Their combined volume is

```math
3(dx \cdot dx \ \cdot x) + dx^3 = 3 x dx^2 + dx^3
```

Since $dx^2$ and $dx^3$ are higher-order infinitesimals, they become negligible compared to $dx$ as $dx \to 0$. This gives

```math
d(x^3) = 3x^3dx
```

Therefore,

```math
\begin{aligned}
dy &= dV = d(x^3) = 3x^2\,dx \\
\frac{dy}{dx} &= \frac{dV}{dx} = \frac{d(x^3)}{dx} = 3x^2
\end{aligned}
```

This states that the derivative of $x^3$ is $3x^2$, and that the differential change in volume is obtained by multiplying the differential change in side length, $dx$, by the derivative.

In other words,

```math
dV = dy = 3x^2dx
```

states that a small change in side length $dx$ produces an approximately linear change in volume $dV$. The derivative $3x^2$ acts as the scaling factor that converts changes in side length inot changes in volume.

The derivative

```math
\frac{dV}{dx} = 3x^2
```

describes how rapidly the volume changes with respect to the side length at a particular value of $x$.

For example, when $x=2$ the derivative

```math
\frac{dV}{dx} = 3x^2 = 3(2)^2 = 12
```

Thus,

```math
dV = 12dx
```

This means that near a cube with side length $2$, an infinitesimal increase in side length produces approximately $12$ times that amount of change in volume.

Similarly, when $x = 4$ the derivative is

```math
\frac{dV}{dx} = 3(4)^2 = 48
```

Thus,

```math
dV = 48 dx
```

This means that near a cube with side length $4$, the same infinitesimal increase in side length produces approximately $48$ times that amount of change in volume.

A larger cube has much larger faces. Since the new volume is formed by extending those faces outward, the same increase in side length sweeps out a greater amount of volume when the cube is already large. For this reason, volume does not grow at a constant rate. As the cube becomes larger, each additional increase in side length creates increasingly more volume. The derivative

```math
\frac{dV}{dx} =3x^2
```

captures this behaviour precisely, showing that the rate of volume growth is proportional to the square of the side length.