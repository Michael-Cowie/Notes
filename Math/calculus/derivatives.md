<div align='center'>
    <h1> Derivatives </h1>
</div>

One of the most fundamental problems in mathematics is the problem of change. How can change be measured precisely? At first this question appears simple. If a car travels 100 kilometres in 2 hours, then its average speed is illustrated below.

<div align='center'>
    <img src='./images/8.png' width='600'>
</div>

This measures average change over a finite interval. However, deeper conceptual difficulties emerge immediately when attempting to describe at a single instant. Suppose a car is moving along a road and the question is asked, "What is the car's velocity at exactly 2 seconds?".

This creates a serious mathematical problem. Ordinary velocity calculations require both,

1. Two positions
2. An interval between them

Without an interval, there appears to be no change to measure.  A similar difficulty appears geometrically, the slope of a line is defined using two distinct points.

```math
\frac{\Delta y}{\Delta x}
```

Yet **curves are not straight lines**. A curve changes direction continuously. At a single point on the curve there appears to be no second nearby points available to produce an ordinary slope. We can imagine that a car is never driving at a rate of $50\frac{km}{hr}$ continuously. The car will,

- Accelerate and decelerate
- Stop at red lights
- Speed up and slow down depending on traffic

<div align='center'>
    <img src='./images/9.png' width='600'>
</div>

This creates one of the deepest conceptual problems in mathematics. How can something possess an instantaneous rate of change at a single point if ordinary change requires an interval? The derivative was invented to resolve this problem.

<div align='center'>
    <h1> Derivatives as a Rate of Change </h1>
</div>

A derivative is a mathematical tool used to describe **rate of change**. When a quantity depends on another quantity, the derivative measures how quickly the output changes as the input changes. On a graph, this appears as the slope of the curve at a particular point. A positive derivative means the function is increasing, a negative derivative means it is decreasing and a derivative of zero indicatives a flat point where the function momentarily stops rising or falling. In practical terms, derivatives allow mathematics to move beyond simply describing values and instead describe behaviour. Rather than only stating where an object is, derivatives explain how fast it is moving, how quickly population grows, how temperature changes over time or how rapidly profit increases with production.

When performing a differentiation of two variables between the $y$ and $x$ axis, we're calculating the slope between them. That is, we will be performing a calculation involving $\frac{\Delta y}{\Delta x}$ at the given point. Therefore, the units need to be understood so that the relationship makes sense. A common example is a distance-time graph. Suppose a car travels a distance $s(t)$, where $t$ is measured in hours and distance is measured in kilometres. The derivance of distance with respect to time is velocity,

```math
v(t) = \frac{ds}{dt} = \frac{km}{h}
```

Suppose we graph $s(t) = t^2$. With,

- $y = s(t) = t^2$ with units km
- $x = t$ with units hour
- Slope between any two points $\frac{\Delta y}{\Delta x} = \frac{\text{km}}{\text{hour}}$
- The red line represents the function $s(t)$, graphing distance-time.
- The blue line is a function which graphs the derivative of $s(t)$. 

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

<div align='center'>
    <img src='./images/11.png' width='300'>
</div>

The second derivative extends this idea further by measuring how the rate of change itself changes. In motion, the first derivative of distance gives velocity, while the second derivative of velocity gives acceleration.

```math
a(t) = \frac{dv}{dt} = \frac{d^2s}{dt^2}
```

Acceleration describes how quickly velocity changes over time. If a car's speed increases from $50 \frac{\text{km}}{\text{hr}}$ to $70 \frac{\text{km}}{\text{hr}}$, the vehicle is accelerating, if the speed decreases, it is declerating. 

As with every differentiation we're performing a slope calculation. Because the Y axis is velocity and has units of $\frac{\text{km}}{\text{hr}}$ and the X axis has the units of $\text{hr}$.

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

- The second derivative gives $a(10) = 2$. Meaning the cars velocity is increasing at a constant rate of $2 \frac{\text{km}}{\text{hr}^2}$

This shows how each derivative adds another layer of interpretation. The original function describes position, the first derivative describes instantaneous velocity and finally the second derivative describes how rapidly the velocity itself changes over time.

<div align='center'>
    <img src='./images/13.png' width='300'>
</div>

<div align='center'>
    <h1> Derivative Theorem </h1>
</div>

Suppose a function changes from $f(x)$ to $f(x + h)$. We can create a generalized function for calculating the slope between 2 different points, from $(x, f(x))$ and $(x + h, f(x + h))$.

<div align='center'>
    <img src='./images/14.png' width='300'>
</div>

This generalized first will be calculated as,

```math
\frac{\Delta y}{\Delta x} = \frac{f(x + h) - f(x)}{x + h - x} = \frac{f(x + h) - f(x)}{h}
```

Geometrically, this is a slope of a secant line joining two points on a curve. For fininite values of $h$, this produces an ordinary average slope over a finite interval.

<div align='center'>
    <img src='./images/derivative_visualized.gif' width='800'>
</div>

However, this still does not answer "What is occurring at exactly one point". To resolve this difficulty, calculus studies what happens as the interval shrinks indefinitely. This is precisely how limits are linked to derivatives. You cannot set the value of $h$ to $0$ as you will receive a division by $0$, calculus resolves this difficulty by examining the slopes between nearby points and then studying the limiting behaviour of those slopes as the interval between the points shrink indefinitely.

**The key idea is that the existence of a limit depends on nearby convergence behaviour, not on whether the limiting value is directly attained**. It only needs to describe a unique value all sufficiently close inputs force the expression toward. That number is then taken as the derivative because it is fully determined by the local behaviour of the function, even though the defining expression itself never needs to be evaluated at the limiting case. 

Calculus defines the derivative as the limit because the nearby secant slopes can converge toward one unique value as the interval width approaches $0$.

**The derivative is therefore defined by**,

```math
f'(x) = \lim_{h \rightarrow 0} \frac{f(x + h) - f(x)}{h}
```

It is therefore crucila to understand that **the derivative is a limit value**. The derivative is not obtained by directly substituting $h=0$. Doing so would produce division by zero. Instead, calculus examines the behaviour of nearby secant slopes as the interval width becomes arbitrarily small. This creates an extremely important conceptual distinction.

The derivative **is not**,

- One finite slope
- One secant line
- One ordinary ratio

Rather, the derivative at a point is the exact limiting value of nearby secant slopes as the interval width approaches zero. This means the derivative originates from convergence behaviour. **The derivative is therefore the exact number forced by the limiting behaviour**.

Finite secant slopes may differ slightly from one another. However, if all sufficiently small nearby slopes converge toward one unique value, calculus defines that value to be the derivative. 

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
s'(t) &= \lim_{h \to 0} (2t+h)
\end{aligned}
```

Now let $h \to 0$.

```math
s'(t) = 2t
```

In

```math
\lim_{h \to 0} (2t + h)
```

the $h$ term becomes $0$ because the limit is examining what happens as $h$ gets arbitrarily close to $0$. Earlier in the derivation, $h$ represented a small change in time used to compare two nearby points on the graph. After simplifying the difference quotient, the only remaining effect of that small change is the extra $h$ in $2t + h$. As the gap between the two points shrinks to nothing, that extra amount also shrinks to nothing, leaving only the instantaneous rate of change. This is possible because the derivative is the limit value where $h \to 0$, resulting it in being removed as it can be simplifying as it converges to a single value.


<div align='center'>
    <h1> Derivatives Notation </h1>
</div>

One of the most distinctive features of calculus is its symbolic language. Even within the topic of derivatives alone, several forms of notation are commonly used.

```math
\frac{dy}{dx}
\qquad
f'(x)
\qquad
\frac{d}{dx}f(x)
```

These are different notational systems describing the same mathematical object. The distinction between them lies not in meaning, but in emphasis. Each notation highlights a different perspective on differentiation and serves a different stylistic or conceptual purpose within mathematics.

The development of multiple derivative notations reflects the historical growth of calculus itself. Different mathematicians approached differentiation through different ways of thinking. Some emphasized changing quantities, other emphasized functions, while others viewed differentiation as an operation applied to an expression. Over time, these approaches evolved into the notation systems still used today.

Understanding derivative notation therefore involves more than simply learning how to read symbols. It involves understanding the mathematical perspective encoded within each notation. Some notations are especially useful in physics, others in pure mathematics and others in formal manipulation or computation. Together, they form a flexible symbolic language for expressing differentiation in a wide variety of contexts.

## Leibniz Notation — $\frac{dy}{dx}$

The notation,

```math
\frac{dy}{dx}
```

is known as Leibniz notation, named after Gottfried Wilhelm Leibniz, one of the founders of calculus. It is one of the most recognizable forms of derivative notation and remains especially common in physics, engineering and applied mathematics. This notation is read as "The derivative of $y$ with respect to $x$" or informally "d y by d x".

One of the defining characteristics of Leibniz notation is that it explicitly displays the relationship between variables. The numerator indicates the quantity being differentiated, while the denominator indicates the variable with respect to which the differentiation occurs. In this way, the notation naturally communicates dependency.

For example,

```math
\frac{dy}{dt}
```

immediately indicates differentiation with respect to time, while

```math
\frac{dP}{dr}
```

indicates differentiation with respect to radius. The notation therefore embeds interpretation directly into the symbols themselves.

Historically, Leibniz developed this notation from the idea of infinitesimal changes. Although modern calculus defines derivatives rigorously through limits, the notation preserves the intuitive appearance of a ratio between tiny changes. That is $dy$ represents the "infinitesimal" change in $y$ and $dx$ represents the "infinitesimal" change in $x$. Therefore, $\frac{dy}{dx}$ can be conceptually thought of as the ratio of these two infinitesimal variables which is represented in the notation.

Leibniz notation is also highly effective when expressing relationships between variables algebraically. In differential equations, for example, derivatives are often manipulated symbolically in ways that resemble ordinary fractions. Because the notation visually separates the dependent and independent variables, it naturally supports these forms of calculation.

Another important feature of Leibniz notation is its adaptability to higher derivatives. The second derivative may be written as,

```math
\frac{d^2y}{dx^2}
```

or generally

```math
\frac{d^ny}{dx^n}
```

This structure preserves the relationship between the variables while clearly indicating repeated differentiation.

## Prime Notation — $f'(x)$

Prime notation is written as

```math
f'(x)
```

and was introduced by Joseph-Louis Language. This notation is read as "f prime of x". Where Leibnzi notation emphasizes variables and relationships, prime notation emphasizes the function itself. The prime symbol marks the function as having been differentiated.

For example, if

```math
f(x) = x^3
```

then its derivative is written as

```math
f'(x) = 3x^2
```

The notation presents differentiation as a transformation from one function into another. The original function $f(x)$ and its derivative $f'(x)$ are viewed as related mathematical objects.

One reason prime notation became popular is its simplicity and compactness. It allows derivatives to be written quickly and cleanly without repeatedly specifying variables or operators. This makes it especially useful in contexts where the variable is already understood.

Prime notation is particularly effective when discussing repeated differentiation. Successive derivatives are written using additional primes. 

```math
f(x) \to f'(x) \to f''(x)
```

This creates a concise symbolic hierarchy that is visually easy to follow. In subjects such as differential equations and mathematical analysis, where higher derivatives appear frequently, prime notation becomes more frequently used.

Despite its simplicity, prime notation carries a strong conceptual message, differentiation transforms functions into new functions.

## Operator Notation — $\frac{d}{dx} f(x)$

Operator notation is written as

```math
\frac{d}{dx} f(x)
```

and emphasizes differentiation as an operation applied to a function or expression.

The symbol

```math
\frac{d}{dx}
```

acts as a mathematical instruction meaning "differentiate with respect to $x$". In this notation , differentiation is treated less as a static relationship and more as an active process.

For example,

```math
\frac{d}{dx} (x^2) = 2x
```

means "apply differentiation to the expression $x^2$. This means to apply the function $f(x) = x^2$ in the quotient difference. Although this is what occurs for every differentiation notation, this notation places a larger emphasis on functions.

```math
\frac{d}{dx}(x^2) = \lim_{h \rightarrow 0} \frac{(x + h)^2 - x^2}{h}
```

Operator notation becomes particularly valuable when differentiating large or complicated expressions. 

```math
\frac{d}{dx}[x^2 \sin(x)]
```

The notation makes it immediately clear that the derivative operator acts on the entire product inside the brackets. Another reason operator notation is important is that it encourages viewing differentiation as a mathematical transformation. The derivative operator behaves almost like a machine that accepts a function as input and produces another function as output.

<div align='center'>
    <h1> Differentiation Rules </h1>
</div>

While the definition of the derivative comes directly from the limit process,

```math
f'(x) = \lim_{h \rightarrow 0} \frac{f(x + h) - f(x)}{h}
```

in practice, most derivatives are not computed directly from this expression. Instead, calculus develops a set of differentiation rules that allow derivatives to be calculated efficiently without repeatedly expanding limits.

These rules are not new definitions of differentiations. Rather, they are logical consequences of the limit definition, derived once and then used as general tools. They allow complex functions to be differentiated through structured patterns rather than first principles each time.

## Power Rule — $\frac{d}{dx}(x^n)$

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

it may seem that the rule only applies when the whole function is a single power such as $x^5$ or $x^10$. However, this interpretation overlooks an important fact, derivative rules are not only rules about whole functions, but also rules about how derivatives interact with algebraic operations such as addition.

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

This rule is logically separate from the power rule. The sum rule says that the differentiation passes through addition. In effect, the derivative operator distributes over sums in the same way multiplication distributes over addition in algebra.

So when differentiating

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

## Linearity Rules — Addition and Constant Multiplication

Differentiation also respects basic algebraic structure. Two key properties are linearity rules.

```math
\frac{d}{dx}[f(x) + g(x)] = f'(x) + g'(x)
```

and

```math
\frac{d}{dx}[c \cdot f(x)] = c \cdot f'(x)
```

where $c$ is a constant.

These rules state that differentiation distributes across addition and factors through constants. In other words, each part of a function can be differentiated independently before being combined.

For example

```math
\frac{d}{dx} (x^2 + x^3) = 2x + 3x^2
```

and

```math
\frac{d}{dx}(5x^2) = 10x
```

These properties are essential because they allow complex espressions to be broken into simpler components. Without linearity, differentiation would require full limit expansion for every expression, making calculus far less practical.

We can try to visualize this by observing the behaviour in

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
    <img src='./images/15.png' width='600'>
</div>

Now, if we zoom in and take the point at $x = 0.5$ We create a new variable $df$ where

```math
df = d(\sin(x)) + d(x^2)
```

In this example $d$ means "differential" or "the tiny change". So $d(\sin(x))$ means "the tiny change in the quantity $\sin(x)$". Because $y = \sin(x)$, this is exactly the same as writing $dy$. Therefore,

```math
\begin{aligned}
dy &= d(\sin(x))
\\

dy &= d(x^2)
\end{aligned}
```

<div align='center'>
    <img src='./images/16.png' width='600'>
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

## Product Rule — Differentiating Multiplication

When two functions are multiplied, differentiation becomes more structured. The product rule states,

```math
\frac{d}{dx}[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)
```

This rule shows that the derivative of a product is not simply the product of the derivatives.

Take $x^2 \cdot x^5$ for each function we can observe

Let,

```math
f(x) = x^2 \qquad g(x) = x^5
```

Then,

```math
f'(x) = 2x \qquad g'(x) = 5x^4
```

Now apply the product rule,

```math
\frac{d}{dx}[x^2 \cdot x^5] = (2x)(x^5) + (x^2)(5x^4)
```

Simplifying each term,

```math
\begin{aligned}
&= 2x^6 + 5x^6 \\
&= 7x^6
\end{aligned}
```

This matches the direct simplification approach,

```math
x^2 \cdot x^7 = x^7 \Rightarrow \frac{d}{dx}(x^7) = 7x^6
```

#### Product Rule - Visualized

Often, it is very difficult to visualize the behaviour of 2 functions multiplying, instead it is conceptually more intuitive to instead visualize it geometrically.

Let,

```math
f(x) = \sin(x) \cdot x^2
```

Now, consider $\sin(x)$ as the width and $x^2$ as the height. Therefore $\sin(x) \cdot x^2 = \text{Area}$. Below is a visualization of what is occurring geometrically when introducing $dx$, from here we attempt to calculate the newly added area $df$.

<div align='center'>
    <img src='./images/product_rule_visualized.gif' width='600'>
</div>

As illustrated above where $df$ represents the new area by the introduced $dx$,

<div align='center'>
    <img src='./images/17.png' width='300'>
</div>

```math
df = d(\sin(x)) x^2 + \sin(x) d(x^2) + d(x^2)
```

Because

```math
\lim_{x \to 0} dx^2 = 0
```

The expression is simplified to

```math
df = d(\sin(x)) x^2 + \sin(x) d(x^2)
```

Which represents the product rule.

#### Product Rule - Algebraic Proof

Here, we will prove the product rule.

```math
\frac{d}{dx}[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)
```

Let,

```math
F(x) = f(x) \cdot g(x)
```

According to the definition,

```math
f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}
```

Therefore,

```math
F'(x) = \lim_{h \to 0} \frac{F(x + h) - F(x)}{h}
```

Which follows,

```math
F'(x) = \lim_{h \to 0} \frac{f(x+h) \cdot g(x+h) - f(x) \cdot g(x)}{h}
```

Now, we're going to subtract and add $f(x + h) \cdot g(x)$ to the numerator. This is a completely valid operation as it is equivalent to adding $0$ on the numerator.

```math
\begin{aligned}
F'(x)
&= \lim_{h \to 0}
\frac{
f(x+h)g(x+h) - f(x)g(x)
\boxed{+\, f(x+h)g(x) - f(x+h)g(x)}
}{h}
\\

&= \lim_{h \to 0}
\frac{
f(x+h)g(x+h)
\boxed{-\, f(x+h)g(x)}
}{h}
+
\lim_{h \to 0}
\frac{
\boxed{f(x+h)g(x)}
- f(x)g(x)
}{h}
\\

&= \lim_{h \to 0}
f(x+h)
\frac{g(x+h)-g(x)}{h}
+
\lim_{h \to 0}
g(x)
\frac{f(x+h)-f(x)}{h}
\end{aligned}
```

Because,

```math
\lim_{h \to 0} f(x + h) = f(x)
```

and multiplying the limit by a constant $g(x)$ can be factored out. It follows,

```math
F'(x) = f(x) \cdot \lim_{h \to 0} \frac{g(x + h) -g(x) }{h} + g(x) \cdot \lim_{h \to 0} \frac{f(x+h) -f(x)}{h}
```

These two terms follow the definition of derivatives. It follows,

```math
F'(x) = f(x) \cdot g'(x) + g(x) \cdot f'(x)
```

## Chain Rule — Differentiating Composite Functions

Many functions are not formed from a single operation, but instead contain multiple layers of functions nested insde one another. These are known as **composite functions**. A composite function occurs when the output of one function becomes the input of another function.

A general composite function is written as

```math
f(g(x))
```

where,

- $g(x)$ is called the inner function
- $f(x)$ is called the outer function

The chain rule describes how derivatives behave when functions are composted together. It is written as

```math
\frac{d}{dx} f(g(x)) = f'(g(x)) \cdot g'(x))
```

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

It is important to understand that $u$ is not a new graph axis. The graph is still entirely determined by the relationship between $x$ and $y$. The variable $u$ is an intermediate quantity used to describe how changes propagate internally through the composite function.

Changing $x$ changes $u$, and changing $u$ then changes $y$. The chain rule therefore studies how change cascades through these intermediate changes.

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
\frac{du}{dx} 2(1) + 3 = 5
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

<div align='center'>
    <img src='./images/18.png' width='600'>
</div>

Therefore,

```math
\frac{dy}{dx} = 8(4)^7 \cdot 5
```

The first derivative,

```math
\frac{du}{dx}
```

describes how $x$ scale into changes in $u$. The second derivative,

```math
\frac{dy}{du}
```

describes how changes in $u$ scale into changes in $y$. 

Because the output change from the first derivative stage becomes the input for the second stage, the scaling factors multiply together. This produces the chain rule relationship.

```math
\frac{dy}{dx} = \frac{dy}{dy} \cdot \frac{du}{dx}
```

This relationship occurs because any small changes in $x$, increases $u$ which increases $y$.


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

#### Example 2 - Function Composite View with Leibniz notation

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

Therefore

```math
\begin{aligned}
y &= u^8
\\

\frac{dy}{du} &= 8u^7
\end{aligned}
```

finally,

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
\frac{dy}{dz} = 3z^2
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