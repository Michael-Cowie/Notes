<div align='center'>
    <h1> Maximization and Minimization Problems </h1>
</div>

Calculus can be used to solve optimization problems. They involve finding the local minimum and maximum values for a function. We use the word "local" to describe the behaviour of the point, comparing to the nearest two points

- If it is higher that than the two closest points, it is a local maximum

- If it is lower than the two closest points, it is a local minimum

<div align='center'>
    <img src='../images/27.png' width='500'>
</div>

When we set the derivative to $0$ and solve for $x$, we would obtain 2 $x$ values. This would represent both the local maximum and minimum. For this reason, when calculating the derivative and solving for $f'(x) = 0$, it's important to distinguish between them both. To visualize the behaviour, we will colour code the function slope behaviour.

<div align='center'>
    <img src='../images/30.png' width='500'>
</div>

- For the local maximum behaviour the slope changes from positive to negative. Additionally, the slope of the derivative is negative at local maximum.
- For the local minimum behaviour the slope changes from negative to positive. Additionally, the slope of the derivative is positive at a local minimum.

Below is an illustration describing common scenarios where the second derivative can be visually understood. It's very useful because it describes the behaviour of functions.

<div align='center'>
    <img src='../images/31.png' width='600'>
</div>

It therefore follows, where $f'(x) = 0$

- It is a local maximum if $f''(x) < 0$
- It is a local minimum if $f''(x) > 0$

#### Maximum Profit Optimization

Suppose this graph represents the profit our company would make by manufacturing and selling $x$ number of a particular item.

- If we make and sell too few, our profit will be limited by the low number.
- If we make and sell too many, our supply might exceed the demand and extra cost for running more machines and hiring more people won't be offset by the higher volume.

<div align='center'>
    <img src='../images/25.png' width='400'>
</div>

We can use calculus to solve this problem. The optimal number $x$ is precisely when the slope is equal to $0$. Suppose

```math
\begin{aligned}
f(x) &= \text{profit}\;(\$1000\text{s}) \\
     &= -0.012x^2 + 9.8x - 1500 \\
f'(x) &= -0.024x + 9.8
\end{aligned}
```

Now, we set the derivative $f'(x) = 0$ and solve for $x$.

```math
\begin{aligned}
f'(x) &= -0.024x + 9.8 = 0 \\
0.024x &= 9.8 \\
x &= \frac{9.8}{0.024} \\
x &\approx 408.3
\end{aligned}
```

This means, we should make 408 units to maximize our profit. If the problem statement also asks for the profit amount, plug this **into the original profit function**.

```math
\begin{aligned}
f(408) &= -0.012(408)^2 + 9.8 \cdot 408 - 1500 \\
       &= 500.8
\end{aligned}
```

This means, the maximum profit amount will be $500,800 by producing 408 units.

#### Minimum Usage Optimization

Given a plain sheet of metal, we want to cut 4 squares around the edges with the goal of maximizing the volume of the box. The box will have no lid.

<div align='center'>
    <img src='../images/26.png' width='400'>
</div>

The 4 boxes will all have equal length $x$. The first thing to do is create a function $f(x)$ to represent the volume $V$.

- The width has a length $32 - 2x$
- The length has a length $24 -2x$
- The height has a length of $x$

We can create a function to represent the volume from the removal of squares as a function of $x$,

```math
\begin{aligned}
V = f(x) &= (32 - 2x)(24 - 2x)x \\
         &= (32 \cdot 24 - 64x - 48x + 4x^2)x \\
         &= (768 - 112x + 4x^2)x \\
         &= 768x - 112x^2 + 4x^3
\end{aligned}
```

This function is used to represent the volume as $x$ changes, therefore

```math
\frac{dV}{dx} = f'(x) = 768 -224x + 12x^2
```

Now, we want to make the derivative equal to $0$ to solve for the maximum. This will represent the maximum volume.

```math
f'(x) = 768 - 224x + 12x^3 = 0
```

We will use the quadratic formula here to solve for $x$, working will not be shown.

```math
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
```

This will solve for 2 $x$ values, $14.1$ and $4.53$. However, the first $14.1$ can be ignored. This is because $2 * 14.1 > 24$, therefore it has no practical application here we it is not possible to remove squares with the value $x = 14.1$. Therefore, this means the correct solution is $4.53$.

The question specifically asked for maximum dimension, this occurs when $x = 4.53$. Therefore, the total maximum dimension is

```math
V = f(x) = (32 - 2(4.53))(24 - 2(4.53)) * 4.53 = 1552\text{cm}^3
```