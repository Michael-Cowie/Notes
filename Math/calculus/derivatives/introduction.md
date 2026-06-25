<div align='center'>
    <h1> Derivatives </h1>
</div>

One of the most fundamental problems in mathematics is the problem of change. How can change be measured precisely? At first, this question appears simple. If a car travels 100 kilometres in 2 hours, then it drives at an **average** rate of $50 \frac{km}{hr}$ over the 2 hour drive to drive a total distance of 100 kilometres.

<div align='center'>
    <img src='../images/8.png' width='600'>
</div>

This measures average change over a finite interval. However, deeper conceptual difficulties emerge immediately when attempting to describe at a single instant. Suppose a car is moving along a road and the question is asked, "What is the car's velocity at exactly 2 seconds?". This creates a serious mathematical problem. Ordinary velocity calculations require both,

1. Two positions
2. An interval between them

Without an interval, there appears to be no change to measure.  A similar difficulty appears geometrically, the slope of a line is defined using two distinct points.

```math
\frac{\Delta y}{\Delta x}
```

However, **curves are not straight lines**. A curve changes direction continuously. At a single point on the curve there appears to be no second nearby points available to produce an ordinary slope. We can imagine that a car is never driving at a rate of $50\frac{km}{hr}$ continuously. The car will,

- Accelerate and decelerate
- Stop at red lights
- Speed up and slow down depending on traffic

<div align='center'>
    <img src='../images/9.png' width='600'>
</div>

This creates one of the deepest conceptual problems in mathematics. How can something possess an instantaneous rate of change at a single point if ordinary change requires an interval? The derivative was invented to resolve this problem.

<div align='center'>
    <h1> Derivatives as a Rate of Change </h1>
</div>

A derivative is a mathematical tool used to describe **rate of change**. When a quantity depends on another quantity, the derivative measures how quickly the output changes as the input changes. On a graph, this appears as the slope of the curve at a particular point. 

- A **positive derivative** means the function is **increasing**
- A **negative derivative** means the function is **decreasing**
- A **derivative of $0$** indicatives a **flat point** where the function momentarily stops rising or falling 

In practical terms, derivatives allow mathematics to move beyond simply describing values and instead describe behaviour. Rather than only stating where an object is, derivatives explain 

- How fast it is moving at a certain time
- How quickly population grows at a certain time
- How temperature changes at a certain time
- How rapidly profit increases with production
- How much of $y$ changes with respect to $x$, because of $\frac{\Delta y}{\Delta x}$
- ...

When performing a differentiation of two variables between the $y$ and $x$ axis, we're calculating the slope between them. That is, we will be performing a calculation involving $\frac{\Delta y}{\Delta x}$ at the given point. Therefore, the units need to be understood so that the relationship makes sense. A common example is a distance-time graph. Suppose a car travels a distance $s(t)$, where $t$ is measured in hours and distance is measured in kilometres. The derivative of the function for distance with respect to time is velocity,

```math
v(t) = \frac{ds}{dt} = \frac{km}{h}
```

Suppose we graph $s(t) = t^2$. With,

- $y = s(t) = t^2$ with units km
- $x = t$ with units hour
- Slope between any two points $\frac{\Delta y}{\Delta x} = \frac{\text{km}}{\text{hour}}$
- The red line represents the function $s(t)$, graphing distance-time.
- The blue line is a function which graphs the derivative of $s(t)$. 

<div align='center'>
    <img src='../images/11.png' width='300'>
</div>

This derivative measures how quickly distance changes as time changes. If the graph of distance versus time is steep, the car is travelling quickly. If it is shallow, the car is travelling slowly. Because distance is measured in kilometres (km) and time in hours (h), the derivative has units of kilometres per hour $\left( \frac{\text{km}}{\text{hr}}\right)$. Thus, the derivative function converts a "position" function into a "speed" function. 

Expanding on our distance function

```math
s(t) = t^2
```

This function itself describes the car's total distance from the starting point, while its derivative describes the cars instantaneous velocity. Differentiating gives

```math
v(t) = \frac{ds}{dt} = 2t
```

If $t = 10$, 

- The distance function gives $s(10) = 100$, meaning the car is 100 kilometres from its starting point. 
- The derivative $v(10) = 20$, meaning that at that exact instant the car is travelling at $20 \frac{km}{hr}$

This interpretation is fundamental in physics, engineering and economics because it allows changing systems to be analyzed instantaneously rather than only over large intervals.

The second derivative extends this idea further by measuring how the rate of change itself changes. In motion, the first derivative of distance gives velocity, while the second derivative of velocity gives acceleration.

```math
a(t) = \frac{dv}{dt} = \frac{d^2s}{dt^2}
```

Acceleration describes how quickly velocity changes over time. If a car's speed increases from $50 \frac{\text{km}}{\text{hr}}$ to $70 \frac{\text{km}}{\text{hr}}$, the vehicle is accelerating, if the speed decreases, it is declerating. As with every differentiation we're performing a slope calculation. Because the $y$ axis is velocity and has units of $\frac{\text{km}}{\text{hr}}$ and the $x$ axis has the units of $\text{hr}$.

```math
\frac{\Delta y}{\Delta x} = \frac{\frac{\text{km}}{\text{hr}}}{\text{hr}} = \frac{\text{km}}{\text{hr}} \div \text{hr} = \frac{\text{km}}{\text{hr}} \cdot \frac{1}{\text{hr}} = \frac{\text{km}}{\text{hr}^2}
```

The differentiation process is,

```math
a(t) = \frac{dv}{dt} = \frac{d^2s}{dt^2} = 2
```

If $t=10$,

- The distance function $s(10)$ gives $100$. Meaning the car is 100 kilometres from its starting point.

- The first derivative gives $v(10) = 20$. Meaning the car is currently travelling at $20 \frac{\text{km}}{\text{hr}}$.

- The second derivative gives $a(10) = 2$. Meaning the cars velocity is increasing at a constant rate of $2 \frac{\text{km}}{\text{hr}^2}$.

<div align='center'>
    <img src='../images/13.png' width='300'>
</div>

This shows how each derivative adds another layer of interpretation. 
- The original function describes position. The $y$ axis units is $km$. The $x$ axis units is $hr$.
- The first derivative describes instantaneous velocity. The $y$ axis units is $\frac{km}{hr}$. The $x$ axis units is $hr$.
- The second derivative describes how rapidly the velocity itself changes. The $y$ axis units is $\frac{km}{hr^2}$. The $x$ axis units is $hr$.

<div align='center'>
    <img src='../images/19.png' width='700'>
</div>


<div align='center'>
    <h1> Derivative Theorem </h1>
</div>

Suppose a function changes from $f(x)$ to $f(x + h)$. We can create a generalized function for calculating the slope between 2 different points, from $(x, f(x))$ and $(x + h, f(x + h))$.

<div align='center'>
    <img src='../images/14.png' width='300'>
</div>

This generalized function will be calculated as,

```math
\frac{\Delta y}{\Delta x} = \frac{f(x + h) - f(x)}{x + h - x} = \frac{f(x + h) - f(x)}{h}
```

Geometrically, this is a slope of a secant line joining two points on a curve.

<div align='center'>
    <img src='../images/derivative_visualized.gif' width='800'>
</div>

However, this still does not answer "What is occurring at exactly one point". To resolve this difficulty, calculus studies what happens as the interval shrinks indefinitely. This is precisely how limits are linked to derivatives. You cannot set the value of $h$ to $0$ as you will receive a division by $0$, calculus resolves this difficulty by examining the slopes between nearby points and then studying the limiting behaviour of those slopes as the interval between the points shrink indefinitely.

**The key idea is that the existence of a limit depends on nearby convergence behaviour, not on whether the limiting value is directly attained**. It only needs to describe a unique value all sufficiently close inputs force the expression toward. That number is then taken as the derivative because it is fully determined by the local behaviour of the function, even though the defining expression itself never needs to be evaluated at the limiting case. 

Calculus defines the derivative as the limit because the nearby secant slopes can converge toward one unique value as the interval width approaches $0$. **The derivative is therefore defined by**,

```math
f'(x) = \lim_{h \rightarrow 0} \frac{f(x + h) - f(x)}{h}
```

<div align='center'>
    <img src='../images/velocity_derivative_visualized.gif' width='800'>
</div>


It is therefore crucial to understand that **the derivative is a limit value**. The derivative is not obtained by directly substituting $h=0$. Doing so would produce division by 0. Instead, calculus examines the behaviour of nearby secant slopes as the interval width becomes arbitrarily small. This creates an extremely important conceptual distinction. The derivative **is not**,

- One finite slope
- One secant line
- One ordinary ratio

Rather, the derivative at a point **is the exact limiting value** of nearby secant slopes as the interval width approaches 0. This means the derivative originates from convergence behaviour. **The derivative is therefore the exact number forced by the limiting behaviour**. Finite secant slopes may differ slightly from one another. However, if all sufficiently small nearby slopes converge toward one unique value, calculus defines that value to be the derivative. 

### Manual Derivative Caculation

We can create the derivative for the previous distance function $s(t) = t^2$, which is used to graph the velocity. Starting with the distance function $s(t) = t^2$, the derivative is found using the fundamental difference quotient definition,

```math
f'(x) = \lim_{h \rightarrow 0} \frac{f(x + h) - f(x)}{h}
```

Substitution of $f(x)$ for $s(t)$ and finally $s(t) = t^2$, it till become

```math
\begin{aligned}
s'(t) &= \lim_{h \to 0} \frac{(t+h)^2-t^2}{h} \\
s'(t) &= \lim_{h \to 0} \frac{t^2+2th+h^2-t^2}{h} \\
s'(t) &= \lim_{h \to 0} \frac{2th+h^2}{h} \\
s'(t) &= \lim_{h \to 0} \frac{h(2t+h)}{h} \\
s'(t) &= \lim_{h \to 0} 2t+h
\end{aligned}
```

Now let $h \to 0$.

```math
s'(t) = 2t
```

During the final calculation,

```math
\lim_{h \to 0} 2t + h
```

the $h$ term vanishes because the limit is examining what happens as $h$ gets arbitrarily close to $0$. Earlier in the differentiation, $h$ represented a small change in time used to compare two nearby points on the graph. After simplifying the difference quotient, the only remaining effect of that small change is the extra $h$ in $2t + h$. As the gap between the two points shrinks to nothing, that extra amount also shrinks to nothing, leaving only the instantaneous rate of change. This is possible because the derivative is the limit value where $h \to 0$, resulting it in being removed as it can be simplifying as it converges to a single value.

### Theorem Recognition in Formulas

Throughout calculations within calculus, formulas and equations are often rearranged into a format that can be substituted directly into the quotient difference. Often, equations can be represented without a variable, such as the function $v$,

```math
v(x)
```

instead of the frequently used,

```math
y = f(x)
```

Often, a small movement of $v$ is represented by $\Delta v$. The calculation for this is,

```math
\Delta v = v(x + \Delta x) - v(x)
```

It's important to recognize this is the numerator in the quotient difference. Now, if we divide each side by $\Delta x$, this becomes

```math
\frac{\Delta v}{\Delta x} = \frac{v(x + \Delta x) - v(x)}{\Delta x}
```

Finally, it's crucial to remember that **the derivative is a limit value**, so we finally introduce a limit.

```math
\lim_{\Delta x \to 0} \frac{\Delta v}{\Delta x} = \lim_{\Delta x \to 0} \frac{v(x + \Delta x) - v(x)}{\Delta x}
```

This information tells us,

```math
\lim_{\Delta x \to 0} \frac{\Delta v}{\Delta x} = \frac{dv}{dx} = v'(x)
```