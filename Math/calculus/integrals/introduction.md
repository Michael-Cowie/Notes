<div align='center'>
    <h1> Integrals </h1>
</div>

Outside of calculus, the word **integration** refers broadly to the process of combining parts into a whole. In simple terms, it describes the act of assembling many small contributions into a single unified quantity. You could integrate information, integrate systems or integrate components in engineering. In each case, the meaning is conceptually the same, **a collection of small parts is combined to produce a single overall object**.

- **Integral** - The **result** of accumulation. For a definite integral, it is the numerical value, e.g. the accumulated area.

- **Integration** - The **process** of finding an integral, either by evaluating a definite integral or by finding an antiderivative.

This interpretation carries directly into mathematics when the goal is to measure quantities that emerge from continuous variation. In particular, the problem of **area under a curve** can be understood as a form of integration in this general sense, the **total area is constructured from infinitely many infinitesimal contributions**.

To formalise this idea, consider a function $f(x)$ defined on an interval $[a, b]$. The quantity we wish to define is the area under the curve $y = f(x)$. Since this region is not composed of simple geometric shapes, it is approximated using shapes whose areas are known exactly, rectangles. The interval is divided into subintervals of equal width

```math
\Delta x = \frac{b - a}{n}
```

On each subinterval, a sample point $x^\ast_i$ is chosen, producing a rectangle of height $f(x^\ast_i)$ and width $\Delta x$. The area of this rectangle is $f(x^\ast_i) \Delta x$, where $x_i^\ast$ is a sample point in the $i$-th subinterval, it's the $x$-coordinate associated with the $i$-th interval. This the asterisk means that the same point on each subinterval is the same because you could choose,

1. The left endpoint underestimates the area.
2. The right endpoint overestimate the area.
3. Midpoints are often closer.

However, the remarkable fact is that although these choices give different finite sums, they all converge to the same limit for continuous functions. Summing over all subintervals produces a finite approximation.

```math
S_n = \sum_{i=1}^n f(x_i^\ast) \Delta x
```

This process does not yet define the integral, it defines a sequence of approximations.

```math
S_1, S_2, S_3, ... 
```

<div align='center'>
    <img src='./images/integration_sum.gif' width='400'>
</div>

Each term refines the previous one by using more, thinner rectangles. The idea of integration is then expressed through a limiting process. If these approximations approach a stable value as $n$ increases without bound, **that value is defined to be the integral**. Thus, integration means **take increasingly finer finite approximations to the area, and define the integral to be the number those approximations approach.**

```math
\int_a^b f(x) dx = \lim_{n \to \infty} S_n
```

In this sense, integration is the process of replacing a complicated geometric quantity with a limit of increasingly refined finite sums. The integral is not one infinite sum, but rather the limiting value of an infinite sequence of finite approximations, much in the same way that constants such as $e$ are defined through limits like,

```math
e = \lim_{n \to \infty} \left( 1 + \frac{1}{n} \right)^n
```

<div align='center'>
    <h1> Geometric Construction to Analytical Structure </h1>
</div>

Once the integral is defined in terms of Riemann sums, it becomes a precise mathematical object independent of any computational technique. At this stage, the integral is fundamentally geometric, it represents accumulated area constructured from arbitrarily fine partitions of an interval. No reference has yet been made to derivatives.

Separately, differentiation is introduced as a measure of instantaneous change. The derivative is defined through the limit of a difference quotient,

```math
f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}
```

which captures the behaviour of a function at a point rather than the accumulation of values across an interval. These two processes

1. Accumulation 
2. Rate of change 

emerge from entirely different constructions and therefore have no immediate reason to expect any relationship between them. The connection between these ideas is established only after both have been defined independently. **The Fundamental Theorem of Calculus** states that if a function $f$ is continuous on $[a, b]$ and $F$ is any function satisfying $F'(x) = f(x)$, then

```math
\int^b_a f(x) \ dx = F(b) - F(a)
```

**This result is not a definition, it is a theorem linking two independently constructued objects**. The limit of Riemann sums on one side and the evaluation of antiderivatives on the other side. Its significance lies in the fact that it translates a limiting process involving many geometric pieces into a boundary evaluation of a derivative-based object.

The presence of Riemann sums in the definition is often contrasted with their absence in routine computation. This contrast is resolved by distinguishing between what is an integral *is* and how it is *computed*. The Riemann sum defines the integral by specifying it as a limiting accumulation of finite contributions. However evaluating this limit directly is rarely practical because it requires an explicit manipulation of sequences such as,

```math
S_n = \sum_{i=1}^n f(x_i^\ast) \Delta x
```

followed by algebraic simplification and passage to the limit $n \to \infty$. Even for simple functions, this process can involve substantial computation. There are the definitions (limit of difference quotient, limit of Riemann sum) and then there are practical methods that are much faster. Not every continuous function has an antiderivative describable in terms of elementary functions. The Riemann sum is the definition of an antiderivative in those cases, there are also other kinds of integration that aren't described in terms of the Riemann sum.

The Fundamental Theorem of Calculus replaces this limiting procedure with a structurally simpler operation, if an antiderivative $F$ of $f$ is known, the value of the integral is determined entirely by evaluating $F$ at the endpoints. In this way, theorem does not redefine the integral, but provides a method of computation that avoids direct engagement with the limiting construction that defines it.

**This separation explains why Riemann sums appear frequently in definitions and theoretical discussions, while antiderivatives dominate practical evaluation**. The Riemann sum establishes the meaning of integration as accumulation, while the Fundamental Theorem reveals that, under appropriate conditions, this accumulation can be expressed in terms of boundary values of a derivative-related function.

<div align='center'>
    <h1> Connecting Accumulation and Differentiation  </h1>
</div>

Suppose we have a particle. Physicists and engineers often use particles in thought experiments like this because a particle is an idealised object that has mass but is treated as having no physical size or dimensions. This simplifies the problem by allowing us to focus on its motion.

Suppose the particle is travelling at a constant velocity of $2\,\frac{m}{s}$ for $8$ seconds.

<div align='center'>
    <img src='./images/12.png' width=600>
</div>

What is the displacement after $8$ seconds? We can solve this problem simply by considering the units. Displacement is calculated by multiplying velocity by time,

```math
2\,\frac{m}{s}\times 8\,s
=2\,\frac{m}{\cancel{s}}\times 8\,\cancel{s}
=16\,m
```

As it turns out, **the signed area beneath a velocity-time graph represents displacement**. This relationship also appears in many other areas of mathematics and science, such as electrical charge accumulated from current, population growth accumulated from a growth rate, and energy transferred through power over time.

The key is to understand the units. Multiplying the units on the vertical axis by the units on the horizontal axis gives us the resulting unit.

<div align='center'>
    <img src='./images/13.png' width=600>
</div>

We can consider more complex examples, such as the following,

<div align='center'>
    <img src='./images/14.png' width=600>
</div>

Since the area beneath the velocity-time graph represents displacement, we can use simple geometry to calculate the total displacement. In this example, the graph is made up of a rectangle and a triangle, so we can calculate their combined area,

```math
\begin{aligned}
\text{Displacement}
&=16\,m+\frac{1}{2}\times 8\,s\times 2\,\frac{m}{s}\\
&=16\,m+8\,m\\
&=24\,m
\end{aligned}
```

The real complexity arises when we encounter a curved line.

<div align='center'>
    <img src='./images/15.png' width=600>
</div>

Suppose we want to calculate the area beneath this curve. One approach is to divide the region into eight smaller sections and estimate the total area by adding together the areas of individual rectangles.

<div align='center'>
    <img src='./images/16.png' width=600>
</div>

```math
\text{Estimated area}=\sum_{t=0}^{7}f(t)\Delta t
```

Although this provides a reasonable estimate, each rectangle fits the curve imperfectly, leaving a small margin of error. The narrower we make the rectangles, the more accurately their combined area approximates the area beneath the curve.

<div align='center'>
    <img src='./images/17.png' width=600>
</div>

The key idea is to make the width of each rectangle, $\Delta t$, progressively smaller, much like the process used when defining a derivative. As we increase the number of rectangles, each rectangle becomes narrower, allowing our approximation to follow the curve more closely. In the limit, as $\Delta t$ approaches zero, the sum of these rectangles approaches the exact area beneath the curve.

This limiting process introduces the idea of a differential. Rather than using a finite interval $\Delta t$, we use the differential $dt$ to represent an infinitesimally small change in our independent variable. In this example, our independent variable is $t$, rather than $x$, so we use $dt$ instead of $dx$.

Adding together an increasingly large number of rectangles would be impractical. Fortunately, calculus introduces a new symbol, resembling an elongated $S$, to represent continuous summation,

```math
\int
```

Similar to the summation symbol $\sum$, the integral symbol can have a specified starting and ending point. In our example, we want to calculate the area between $t=0$ and $t=8$, which is written as,

```math
\int_0^8
```

This represents the continuous accumulation of area across the interval from $0$ to $8$. Recall that our previous estimate used the expression,

```math
\text{Estimated area}=\sum_{t=0}^{7}f(t)\Delta t
```

Here, we are adding together rectangular areas, each calculated by multiplying its height by its width. The integral follows the same underlying idea, except that we consider the limiting process as the widths of the rectangles approach zero. We therefore write,

```math
\int_0^8 f(t)\,dt
```

### Connecting Accumulation and Differentiation

We are now going to introduce a function $A(t)$, which represents the area accumulated beneath our curve from the starting point $t=0$ up to any given time $t$. We do not yet know the exact expression for $A(t)$. However, we can consider how much the accumulated area changes over a small time interval $\Delta t$. This change can be approximated by the area of a rectangle,

```math
\Delta A\approx f(t)\cdot\Delta t
```

<div align='center'>
    <img src='./images/19.png' width=600>
</div>

We use the approximation symbol because the rectangular area does not perfectly match the area beneath the curve. However, this approximation becomes increasingly accurate as $\Delta t$ becomes smaller.

We can divide both sides by $\Delta t$ to obtain,

```math
\frac{\Delta A}{\Delta t}\approx f(t)
```

More precisely, the change in accumulated area is,

```math
\Delta A=A(t+\Delta t)-A(t)
```

Taking the limit as $\Delta t$ approaches zero means that our approximation becomes exact. The left-hand side approaches the derivative of our accumulated area function $A(t)$ with respect to $t$. We therefore obtain,

```math
\begin{aligned}
\lim_{\Delta t\to 0}
\frac{A(t+\Delta t)-A(t)}{\Delta t}
&=f(t)\\
\frac{dA}{dt}&=f(t)
\end{aligned}
```

This is a crucial result because it establishes that **the derivative of our accumulated area function is the original function $f(t)$**. In other words, differentiation tells us the rate at which our accumulated area is changing, while integration allows us to recover the accumulated quantity. We can express this relationship as,

```math
\begin{aligned}
A'(t)&=f(t)\\
A(t)&=F(t)+C
\end{aligned}
```

We have therefore established that $A(t)$ is an antiderivative of $f(t)$. However, knowing its derivative does not automatically tell us where our accumulation begins. To establish this, we need to consider our chosen starting point.

For our particle example, we have chosen to measure displacement from $t=0$. To calculate the area accumulated between $t=0$ and the current time $t$, we take the accumulated value at $t$ and subtract the accumulated value at our starting point, $t=0$. This gives us,

```math
A(t)-A(0)
```

Since no area has accumulated within our chosen interval when $t=0$, we know that $A(0)=0$. Therefore,

```math
\begin{aligned}
A(t)-A(0)&=A(t)-0\\
&=A(t)
\end{aligned}
```

Consequently, $A(t)$ represents the area accumulated between $t=0$ and the current time $t$. We can now use this initial condition to determine the unknown constant $C$. Since $A(t)$ is an antiderivative of $f(t)$, we can write,

```math
\begin{aligned}
A(t)&=F(t)+C\\
A(0)&=F(0)+C\\
0&=F(0)+C\\
C&=-F(0)
\end{aligned}
```

Substituting this value of $C$ back into our accumulation function gives,

```math
\boxed{A(t)=F(t)-F(0)}
```

We can therefore express our accumulation function using a definite integral,

```math
\boxed{A(t)=\int_0^t f(u)\,du}
```

Here, $u$ is simply a dummy variable of integration. We use it instead of $t$ to distinguish the variable being integrated from the upper limit of the integral.

### Generalising To Any Two Points

We now have an expression for the accumulated area between our starting point $t=0$ and any later point $t$. However, what if we are interested in the area between two arbitrary points, $t=a$ and $t=b$? This is represented by the following definite integral,

```math
\int_a^b f(t)\,dt
```

<div align='center'>
    <img src='./images/23.png' width=600>
</div>

We can understand this as the total area accumulated from $t=0$ to $t=b$, minus the area accumulated from $t=0$ to $t=a$. Since both accumulated areas share the same starting point, subtracting them leaves only the area between $a$ and $b$.

<div align='center'>
    <img src='./images/24.png' width=600>
</div>

We can express this relationship mathematically as,

```math
\begin{aligned}
\int_a^b f(t)\,dt
&=\int_0^b f(t)\,dt-\int_0^a f(t)\,dt\\
&=A(b)-A(a)\\
&=[F(b)-F(0)]-[F(a)-F(0)]\\
&=F(b)-F(a)
\end{aligned}
```

We have therefore established the relationship between definite integration and antiderivatives, known as the **Fundamental Theorem of Calculus**,

```math
\boxed{\int_a^b f(t)\,dt=F(b)-F(a)}
```

where $F(t)$ is any antiderivative of $f(t)$.

With this relationship established, we can return to our previous examples and calculate the areas using antiderivatives and definite integrals, rather than relying on geometric area formulas.

#### Particle Example 1

Consider a particle travelling at a constant velocity of $2\,\frac{m}{s}$. As time progresses, its displacement increases, which we can represent using the displacement-time function $s(t)$. We can also calculate this displacement by integrating the velocity function to find the accumulated area beneath the velocity-time graph.

```math
\begin{aligned}
A'(t)&=f(t)=2\\
A(t)&=\int 2\,dt\\
&=2t + C
\end{aligned}
```

We want to calculate the displacement between $t=0$ and $t=8$. We therefore set $t=0$ as the lower bound and $t=8$ as the upper bound, and write the antiderivative using bracket notation,

```math
A=\int_0^8 2\,dt=\left[2t\right]_0^8
```

We now substitute the upper bound, then subtract the lower bound,

```math
\begin{aligned}
A&=2(8)-2(0)\\
&=16-0\\
&=16\,\text{m}
\end{aligned}
```

Therefore, after $8$ seconds, the particle has travelled $16$ metres.

<div align='center'> <img src='./images/distance_accumulation_corrected_preserve_s_graph.gif' width=600> </div>

This value is also the area of the rectangle beneath the velocity-time graph. Geometrically, the rectangle has a width of $8$ and a height of $2$, giving an area of $16$ square units on the graph. However, the axes are measured in $\text{m/s}$ and $\text{s}$, so each unit of area represents,

```math
(\text{m/s})\times\text{s}=\text{m}
```

Keep in mind that this example starts at $t=0$, but we still explicitly evaluate both bounds when calculating the definite integral. This becomes particularly important when our lower bound is not zero.

#### Particle Example 2

Consider a second example in which the particle travels with a linearly increasing velocity, described by the following function,

```math
\begin{aligned}
A'(t)&=f(t)=\frac{1}{4}t+2\\
A(t)&=\int\left(\frac{1}{4}t+2\right)\,dt\\
&=\frac{1}{8}t^2+2t + C
\end{aligned}
```

We want to calculate the displacement between $t=0$ and $t=8$. We therefore set $t=0$ as the lower bound and $t=8$ as the upper bound, and write the antiderivative using bracket notation,

```math
A=\int_0^8\left(\frac{1}{4}t+2\right)\,dt
=\left[\frac{1}{8}t^2+2t\right]_0^8
```

We now substitute the upper bound, then subtract the lower bound,

```math
\begin{aligned}
A&=\left(\frac{1}{8}(8)^2+2(8)\right)
-\left(\frac{1}{8}(0)^2+2(0)\right)\\
&=8+16-0\\
&=24\,\text{m}
\end{aligned}
```

Therefore, after $8$ seconds, the particle has travelled a total distance of $24\,\text{m}$.

<div align='center'> <img src='./images/distance_accumulation_linear_velocity.gif' width=600> </div>

#### Particle Example 3

Finally, we can observe the importance of integration when calculating the area beneath curves with more complicated shapes, such as,

```math
y=x^2
```

<div align='center'> <img src='./images/position_velocity_accumulation_x_squared_2_to_8.gif' width=600> </div>

Returning to our particle example, let its velocity be described by the function,

```math
\begin{aligned}
v(t)&=t^2\\
A'(t)&=v(t)=t^2
\end{aligned}
```

To find the accumulated area, we integrate our velocity function,

```math
A(t)=\int t^2\,dt
```

This time we want the area accumulated between $t=2$ and $t=8$. We therefore set $t=2$ as the lower bound and $t=8$ as the upper bound, and write the antiderivative using bracket notation,

```math
A=\int_2^8 t^2\,dt=\left[\frac{1}{3}t^3\right]_2^8
```

We now substitute the upper bound, then subtract the lower bound,

```math
\begin{aligned}
A&=\frac{1}{3}(8)^3-\frac{1}{3}(2)^3\\
&=\frac{512}{3}-\frac{8}{3}\\
&=\frac{504}{3}\\
&=168
\end{aligned}
```

Therefore, between $2$ and $8$ seconds, the particle travels a total distance of $168\,\text{m}$. This example demonstrates how integration allows us to calculate the exact accumulated area beneath a curve, even when its shape makes ordinary geometric area formulas impractical.

<div align='center'>
    <h1> Area Representation  </h1>
</div>

The concept of integration is not fundamentally about computing areas. Area is simply the first geometric application through which the subject is introduced. More generally, integration describes the accumulation of many infinitesimal contributions into a single total quantity. The quantity being accumulated depends entirely on the meaning of the function being integrated. This interpretation becomes particularly clear when considering physical units.

Suppose a graph represents velocity as a function of time. The vertical axis has units of $\frac{m}{s}$, while the horizontal axis has units of $s$. Each rectangle in a Riemann sum has area,

```math
(\text{height})(\text{width}) = \frac{m}{s}s = m
```

The numerical value of a rectangle approximates how far an object travels during that short interval of time. Summing the areas of all rectangles therefore approximates total distance travelled over the interval. As the rectangle becomes thinner, this approximation converges to the exact accumulated distance. Thus, integration naturally combines countless infinitesimal changes in position into a single total displacement.

Suppose the velocity of an object is

```math
v(x) = 2x
```

Each infinitesimal contribution to displacement is

```math
v(x) dx
```

Accumulating these contributions from $a$ to $b$ gives

```math
\int^b_a 2x dx
```

According to the Fundamental Theorem of Calculus

```math
\int^b_a 2x \ dx = F(b) - F(a) = [x^2]^b_a = b^2 - a^2
```

Notice what has happened. The left-hand side expresses displacement as the accumulation of infinitely many infinitesimal pieces of distance. The right-hand side computes precisely the same quantity without ever constructing those pieces explicitly. The theorem therefore does not redefine the integral, it reveals that the accumulated quantity defined through Riemann sums is exactly equal to the change in an antiderivative evaluated at the endpoints.

The same principle applies regardless of the physical quantity involved. Integrating,

- Acceleration $\left( \frac{m}{s^2} \right)$ with respect to time $s$ produces velocity $\left( \frac{m}{s} \right)$

- Power $\left( \frac{J}{s} \right)$ with respect to time produces energy ($J$)

- Density $\left( \frac{kg}{m^3} \right)$ with respect to volume $\left( m^3 \right)$ produces mass $(kg)$.

In every case, integration accumulates a quantity measured "per unit" of the independent variable into the corresponding total quantity. Area under a curve is therefore not the defining intuition behind integration, but rather one particular instance of a much broader principle of accumulation.

<div align='center'>
    <h1> Limits of the Fundamental Theorem of Calculus </h1>
</div>

A distinction must me made between a **definition** and a **theorem**. 

A definition establishes the meaning of a mathematical object. It is not proved, rather, it specifies precisely what is meant by a concept. Essentially, a definition creates a new mathematical entity "out of nothing". The definite integral, is defined as the limit of a sequence of Riemann sums.

A theorem, by contrast, is not a definition but a mathematical statement that has been proved using definitions, axioms and previously established results. A theorem therefore describes a property of an already-defined object rather than giving the object its meaning. Unlike a definition, every theorem is accompained by a collection of hypotheses that specify the circumstances under which theorem is valid. The logic structure of every theorem is therefore, if the hypotheses are satisfied, then the stated conclusion follows. In essence, a theorem states some relation between previously defined mathematical entities.

The Fundamental Theorem of Calculus is precisely such a theorem. It does not define the definite integral, instead, it proves that the definite integral, already defined through the limit of Riemann sums, may be computed by evaluating an antiderivative at the endpoints of the interval, provided its hypotheses are satisfied.

One of the most important hypotheses is that the function being integrated must be continuous on the interval of integration. This requirement is not an arbitrary restriction but one of the assumptions under which theorem has been proved. Consequently, before applying the Fundamental Theorem, it is necessary to verify that its hypotheses hold. The importance of this distinction becomes apparent when considering functions with discontinuities. Consider the function,

```math
f(x) = \frac{1}{x^2}
```

Although an antiderivative exits,

```math
F(x) = - \frac{1}{x}
```

The function itself is undefined at $x = 0$. Therefore, it is not continuous on any interval containing $0$, such as $[-1, 1]$. Since one of the hypotheses of the Fundamental Theorem is violated, theorem cannot be applied to evaluate,

```math
\int^1_{-1} \frac{1}{x^2}dx
```

by computing

```math
\left[ - \frac{1}{x} \right]^1_{-1}
```

The issue is not that theorem produces an incorrect result, rather, theorem makes no claim in this situation because its assumptions have not been satisfied. Instead, the integral must be analysed using the definition appropriate for an improper integral, in which the interval is separated at the point of discontinuity and each portion is evaluated through its own limiting process.

This illustrates why the Riemann definition of the definite integral is logically primary. The integral itself is defined independently of antiderivatives and independently of the Fundamental Theorem of Calculus. **The theorem provides a remarkably efficient method for evaluating the integral when its hypotheses are satisfied, but it does not replace the definition**. Whenever those hypotheses fail, you return not to a different notion of integration, but to the original definition from which theorem was proved.