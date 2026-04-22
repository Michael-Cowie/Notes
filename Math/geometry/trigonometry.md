<div align='center'>
    <h1> Trigonometry </h1>
</div>

In nature, we observe numerous phenomena that propagate in the form of waves or can be described by the concept of a wave. To understand these phenomena, we model them mathematically. It is remarkable that the mathematical description of wave, even when solving complicated differential equations can be traced back to a simple geometric shape, **the triangle**. So, how can a wave arise from a triangle?

If we divide the circumfrance of a circle $C$ by the length of the diameter $D$, that is, if we calculate the ratio of the circumfrance to diameter,

```math
\frac{C}{d} = \pi
```

We get a number that **always remains the same**, no matter how large or small the circle is. Today, we know this number as pi. If we rearrange this equation and substitute the diameter as two times the radius, we get

```math
C = 2\pi r
```

With a radius of 1, the circumfrance is simply $2\pi$. It was precisely this circle that was used as a template for a new measurement of angular units. Which is why it became known as the unit circle. Now, instead of imagining that, for example $60^\circ$ consists of 60 parts, we place our circle template with its center at the tip of the angle and measure the length of the arc that this angle encloses.

<div align='center'>
    <img src='./images/106.png' width='700'>
</div>

In the case of this angle, the arc length corresponds with $\frac{1}{6}$ of the entire circumfrance. That is, $60^\circ \cong \frac{2\pi}{6} = \frac{\pi}{3}$. At a $90^\circ$ angle, the ark occupies a quarter of the circle. So this angle corresponds to $\frac{90}{360} \cdot 2\pi = \frac{1}{4} \cdot 2\pi = \frac{2\pi}{4} = \frac{\pi}{2}$

<div align='center'>
    <img src='./images/107.png' width='200'>
</div>

For a full circle, we eventually measure the complete circumfrance of $2\pi$.

#### What is a Degree?

A **degree ($^\circ$)** is defined by dividing a full circle into 360 equal parts. Therefore,

```math
360^\circ = \text{one full revolution}
```

Degrees are convenient because they align well with historical and practical uses (navigation, geometry, etc...) but they are arbitrary, there is nothing inherently "natural" about 360 beyond convention.

#### What is a Radian?

A **radian ($\mathrm{rad}$)** is defined using the geometry of a circle Let's say we have a circle with a radius $r$

<div align='center'>
    <img src='./images/133.png' width='300'>
</div>

If we bring the radius outside the circle and wrap it around the circumfrance to create an arc. From here, draw a line from the centre of the circle to where the arc ends, **this is the definition of one radian**. It is the angle created when we have an **arc length of $r$**.

<div align='center'>
    <img src='./images/134.png' width='300'>
</div>

For reference, this is about $\approx 57.3^\circ$. This conversion occurs because,

```math
\begin{align*}
2\pi \ \mathrm{rad} &= 360^\circ \\
1 \ \mathrm{rad} &= \frac{360^\circ}{2\pi} \\
1 \ \mathrm{rad} &\approx 57.3^\circ
\end{align*}
```

When we count the number of radians in a circle, this is how we come up with $2\pi \ \mathrm{rad}$ in a circle. This is not coincidental, it is precisely because the circumfrance of a circle is calculated from $2 \pi r$. Meaning, their are $2 \pi$ number of $r$ into the circumfrance.

That is, we know that $1 \ \mathrm{rad}$ occurs every $r$ length on the circumfrance.

```math
\begin{align*}
C &= 2 \pi r \\
\frac{C}{r} &= 2 \pi (\approx 6.28) \\
\end{align*}
```

Therefore, we know that $r$ goes into the circumfrance $C$, $2 \pi$ times. It follows that $1 \ \mathrm{rad}$ will go into the circumfrance (Also $360^\circ$) $2 \pi$ times.

<div align='center'>
    <img src='./images/135.png' width='300'>
</div>

Another important relationship is known from the radian to the geometry of a circle where,

```math
\theta = \frac{\text{arc length}}{\text{radius}}
```

We can begin to create this relationship by starting with something we already know.

```math
C = 2 \pi r
```

Now think in **fractions of a circle**. If an angle $\theta_{rad}$ in $\mathrm{rad}$ is some fraction of a full turn, then its arc length $s$ is the same fraction of the circumfrance. Because $\theta_{rad}$ is in $\mathrm{rad}$ and $2 \pi r$ is also in $\mathrm{rad}$, the units cancel out to get a pure number. This is how these equalities hold true.

```math
\begin{align*}
\frac{s}{2 \pi r} &= \frac{\theta_{rad}}{2\pi} \\
\frac{s}{r} &= \theta_{rad}
\end{align*}
```

<div align='center'>
    <img src='./images/136.png' width='800'>
</div>

While the above shows,

```math
\theta_{rad} = \frac{s}{r}
```

as a derived formula, it's significantly important to understand what this represents in terms of understanding radians as a unit. Instead, radians is defined as **"An angle is how many radius-lengths fit along the arc"**.

That is,

- If you have an arc length of $r$, then you have $1 \ \mathrm{rad}$
- If you have an arc length of $2r$, then you have $2 \ \mathrm{rad}$
- If you have an arc length of $\pi r$, then you have $\pi \ \mathrm{rad}$

If we break down the equation to properly understand what is happens, given the fraction

```math
\frac{s}{r}
```

We are trying to solve for many **how radius length $r$ fit into the arc length $s$**. The result will be a multiple of $r$ into $s$ and given that $1 \ \mathrm{rad} = r$ it therefore calculates the amount of radians into the arc length $s$.

Take the following example with $r=2$ and $s=5$.

<div align='center'>
    <img src='./images/137.png' width='300'>
</div>

```math
\theta_{rad} = \frac{s}{r} \\
\theta_{rad} = \frac{5}{2} \\ 
\theta_{rad} = 2.5 \\
```

Therefore we have,

<div align='center'>
    <img src='./images/138.png' width='300'>
</div>

This can also be represented in degrees because,

```math
2.5 \ \mathrm{rad} \times \frac{180^\circ}{\pi \ \textrm{rad}} = \frac{2.5 * 180}{\pi}^\circ = \ \approx 143.3^\circ
```

This means, given a circle with $r=2$ and $s=5$. The arc will form with an angle of $2.5 \ \mathrm{rad}$ or $\approx 143.3^\circ$.

#### Why Radians are Unitless

Units are one of the most reliable tools in mathematics and physics. They allow us to track quantities, verify equations and ensure that calculations make sense. For example, when multiplying and dividing measurements, units behave predictably, metres cancel metres, seconds remain seconds and so on. However, when working with angles, especially radians, this familiar system seems to break down. Expressions such as,

```math
s = r \theta_{rad}
```

raise a natural concern. If $r$ is a length and $\theta_{rad}$ is an angle, why does their product still produce a length? When multiplying two variables, the resulting product has the combined unit of both,

```math
m \times \mathrm{rad} = \mathrm{m \ rad}
```
This apparent inconsistency leads to an important realization. **Radians are not ordinary units**. Understanding how they differ from standard units resolves the confusion and explains why they're so powerful in mathematics.

In most contexts, units represent physical dimensions. For example,

1. Metres (m) measure length
2. Seconds (s) measure time
3. Kilograms (kg) measure mass

When performing calculations, these units combine and cancel according to agelbraic rules. For instance,

```math
\frac{10\text{m}}{2\text{m}} = 5
```

Here, the metres cancel, leaving a **dimensionless number**. This is familiar and intuitive.

A radian is defined **using a ratio**.

```math
\theta_{rad} = \frac{s}{r}
```

Where,

- $s$ is the arc length
- $r$ is the radius

From a unit perspective,

```math
\theta_{rad} = \frac{\text{length}}{\text{length}} = 1
```

This is the crucial point, **a radian is dimensionless**. It is not an independent unit like metres, or seconds, but rather **a ratio of two lengths**. The symbol $\mathrm{rad}$ is therefore best understood as a label that indicates "this number represents an angle", rather than a true physical unit.

The equation $s = r\theta_{rad}$ does not break the rules. If one thinks of $\theta_{rad}$ as carrying a unit $\mathrm{rad}$, then multiplying $r$ (metres) by $\theta$ might appear to produce "metre radians". However, this reasoning treats radians as if they were a fundamental unit, which they are not. 

Substituting the definition of $\theta_{rad}$ can validate this.

```math
\begin{align*}
s &= r \cdot \frac{s}{r} \\
s &= s
\end{align*}
```

In terms of units,

```math
m \cdot \frac{m}{m} = m
```

The units are entire consistent. The "radian" does not need to be cancelled at this stage because it has already disappeared in the ratio $\frac{s}{r}$. An angles radian value is "How many radii is the arc length of a circle subtended by this angle?". This is a pure number. In other words, **radians are adimensional**. This is why you are allowed to cancel radians everywhere it appears in a formula, as 1 radian is the same as 1.

Despite being dimensionless, radians are often written with the symbol $\mathrm{rad}$, especially in expressions like,

```math
2 \ \mathrm{rad} \times \frac{180^\circ}{\pi \ \mathrm{rad}}
```

In this context, $\mathrm{rad}$ behaves like a unit that can be cancelled. This is not because it is a true unit, but it serves as a **bookkeeping device**. It helps distinguish angles from ordinary numbers and ensures that conversions are applied correctly.

Thus, radians occupy a unique position.

1. Mathematically, they are dimensionless.
2. Practically, they are treated **as if they have units** for clarity.

#### Why we use Radians

A common question in mathematics is why radians are preferred over degrees, especially when both measure the same angle, angles. The key reason is not arbitrary convention, but **simplicity**. Radians are defined in a way that naturally fits the geometry of a circle, which causes many important formulas to become cleaner and more direct. This can be clearly seen through two fundamental examples,

1. The arc length
2. The sector area

Radians are defined by the relationship,

```math
\theta_{rad} = \frac{s}{r}
```

Where $s$ is the arc length and $r$ is the radius. Rearranging gives,

```math
s = r\theta_{rad}
```

This equation is not a derived formula, it is a direct consequence of how radians are defined. Because of this, radians encode the relationship between angle and length in a circle.

#### Arc Length

Using radians, the formula for arc length is,

```math
s = r\theta_{rad}
```

This is simple and proportional. Doubling the angle doubles the arc length. However, **if the angle $x$ is given in degrees**, it must first be converted.

```math
\theta_{rad} = x^\circ \cdot \frac{\pi \ \mathrm{rad}}{180^\circ}
```

Substituting into the formula,

```math
s = r \left( x^\circ \cdot \frac{\pi \ \textrm{rad}}{180^\circ} \right) = \frac{\pi x r}{180}
```

Now the formula contains an extra constant factor $\frac{\pi}{180}$. This factor does not come from geometry, it comes from the degree system itself.

#### Sector Area

The same pattern appears with sector area. The area of a circle is calculated as,

```math
A = \pi r^2
```

We can expand on this to calculate the area of a sector in a circle.

<div align='center'>
    <img src='./images/139.png' width='200'>
</div>

Given an angle $\theta_{rad}$ we can calculate the area of the sector as,

```math
\begin{align*}
A &= \frac{\theta_{rad}}{2\pi} \cdot \pi r^2 \\
A &= \frac{1}{2} r^2 \theta_{rad}
\end{align*}
```

This follows directly from taking a fraction of the full circle area. **Using the variable x in degrees**, we again convert.

```math
\theta_{rad} = x^\circ \cdot \frac{\pi \ \mathrm{rad}}{180^\circ}
```

Substituting,

```math
A = \frac{1}{2}r^2\left( x^\circ \cdot \frac{\pi \ \mathrm{rad} }{180^\circ} \right) = \frac{\pi x r^2}{360}
```

Once again, an extra factor appears, making the formula less clean.

These examples illustrate the core reason radians are preferred.

1. In radians, formulas reflect pure geometric relationships.
2. In degrees, formulas include conversion factors like $\frac{\pi}{180}$
3. Radians eliminate unnecessary constants because they are defined using the circle itself. This means relationships are direct and proportional, equations are simpler and easier to manipulate and patterns in mathematics become more visible.

<div align='center'>
    <h2> Unit Conversion </h2>
</div>

Since both measure the same full rotation,

```math
\begin{align*}
360^\circ &= 2\pi \ \mathrm{rad} \\
180^\circ &= \pi \ \mathrm{rad}
\end{align*}
```

Therefore,

```math
\frac{180^\circ}{\pi \ \mathrm{rad}} = 1
```

and,

```math
1 = \frac{\pi \ \mathrm{rad}}{180^\circ}
```

This is the **key conversion identity**. Think of conversion like cancelling units in fractions. 

### Radians to Degrees

To transform an angle $\theta_{rad}$ into degrees, we need to multiply the angle by 1, while cancelling out the $\mathrm{rad}$ unit and keep the $^\circ$ unit. This is done by multiplying by $\frac{180^\circ}{\pi \ \mathrm{rad}}$.

```math
\theta \ \mathrm{rad} \times \frac{180^\circ}{\pi \ \mathrm{rad}}
```

For example,

```math
\begin{align*}
\frac{\pi}{3} \ \textrm{rad} \times \frac{180^\circ}{\pi \ \textrm{rad}} \\
\\
\frac{\cancel{\pi}}{3} \ \cancel{\textrm{rad}} \times \frac{180^\circ}{\cancel{\pi} \ \cancel{\textrm{rad}}} \\
\\
\frac{180^\circ}{3} &= 60^\circ
\end{align*}
```

This works because,

1. $\pi$ cancels
2. The unit $\mathrm{rad}$ cancels
3. This leaves the unit degrees ($^\circ$) left.

This works perfectly fine in scenarios where the radian is not a multiple of $\pi$, where it is frequently displayed as.

```math
2 \ \mathrm{rad} \times \frac{180^\circ}{\pi \ \mathrm{rad}} = \frac{360}{\pi}^\circ = \ \approx 114.5^\circ
```

#### Degrees to Radians

To transform an angle $\theta_{deg}$ into $\mathrm{rad}$, we need to multiply the angle by 1, while cancelling out the $^\circ$ unit and keep the $\mathrm{rad}$ unit. This is done by multiplying by $\frac{\pi \ \mathrm{rad}}{180^\circ}$.

```math
\theta_{deg} \times \frac{\pi \ \mathrm{rad}}{180^\circ}
```

For example,

```math
\begin{align*}
45^\circ \times \frac{\pi \ \mathrm{rad}}{180^\circ} \\
\\
45^\circ \times \frac{\pi \ \mathrm{rad}}{180^\circ} \\
\\
\frac{45 \times \pi}{180} \ \frac{\cancel{^\circ} \ \mathrm{rad}}{\cancel{^\circ}} \\
\\
\frac{45\pi}{180} \ \mathrm{rad} &= \frac{\pi}{4} \ \mathrm{rad}
\end{align*}
```

This works because,

1. The degrees unit cancel
2. Results keeps the $\mathrm{rad}$ unit


<div align='center'>
    <h1> The Right-Angled Triangle </h1>
</div>

The right-angled triangle is a very special triangle because it can do all things other triangles can do, in addition to the Pythagorean Theorem. Furthermore, we can construct any other triangle from two right angled ones. So, if we understand the right angle triangle, we understand all of the others.

<div align='center'>
    <img src='./images/108.png' width='200'>
</div>

For the study of triangles, known as Trigonometry, it is therefore sufficient to study the right-angled triangle.

<div align='center'>
    <img src='./images/109.png' width='300'>
</div>

Let us begin by first naming the individual sides.

- **Hypotenuse** - The side opposite the right angle. It is also the longest side.

<div align='center'>
    <img src='./images/110.png' width='300'>
</div>

- **Leg** - One of the other two remaining sides.

<div align='center'>
    <img src='./images/111.png' width='300'>
</div>

From the perspective of an angle, illustrated below as $\alpha$.

- **Opposite** - The leg opposite the angle.
- **Adjacent** - The leg adjacent to the angle.

<div align='center'>
    <img src='./images/112.png' width='400'>
</div>

From the perspective of the other angle $\beta$, you would swap them accordingly.

<div align='center'>
    <img src='./images/113.png' width='400'>
</div>

With these three sides, we can create a total of 6 ratios given the permutations of length 2 for the three sides $H$, $O$, $A$.

<div align='center'>
    <img src='./images/116.png' width='700'>
</div>

Now comes the remarkable part. These ratios correspond to a number that **does not change no matter how large or small we make the triangle**. For the number to change in ratio $\frac{O}{H}$, we would have to change only the numerator or only the denominator. But how can we change the numerator (Which is the length of the opposite), without changing the denominator (Which is the length of the hypotenuse). Well, **we would have to change the angle $\alpha$**. Meaning, if we set the hypotenuse to a fixed length and increase or decrease the angle $\alpha$, only then can the ratio change.

<div align='center'>
    <img src='./images/trigonometry_ratio.gif' width='700'>
</div>

Therefore, if these ratios only change when $\alpha$ changes, **then we can also understand them as functions**. Therefore, these are functions, that **when given an angle, will return the ratio of the two sides**.

<div align='center'>
    <img src='./images/117.png' width='700'>
</div>

Each of these functions has been given its own name. This is the meaning for each function

<div align='center'>
    <img src='./images/118.png' width='700'>
</div>

These ratios are **independent of the triangles size**. Any two triangles with the same angles are similar, so the ratios remain constant. This is due **triangle similarity**. This comes directly from the concept of similarity in geometry.

Two triangles are similar if,

1. Their corresponding angles are equal.
2. Their corresponding sides are in proportion.

So if two triangles share the same angle $\theta$ and both are right angled, then they automatically have the same three angles.

1. $90^\circ$
2. $\theta$
3. $90^\circ - \theta$


If Triangle $A$ and Triangle $B$ are similar, then all corresponding sides scale by a constant factor. If Triangle $A$ has sides $a, b, c$ then Triangle $B$ is a scaled version $ra, rb, rc$. Therefore,

```math
\frac{rb}{rc} = \frac{\cancel{r}b}{\cancel{r}c} = \frac{b}{c}
```

The scale factor $r$ cancels out.

<div align='center'>
    <img src='./images/119.png' width='700'>
</div>

Given that for $\theta_1$,

- $O = b$
- $H = c$

```math
\frac{O}{H} = \frac{b}{c} = \frac{rb}{rc}
```

It is this that allows for the relationship to exist. The size of the triangles do not change the ratio as long as they're similar triangles. This means the ratio $\frac{O}{H}$ is the same for similar triangles and the **only way to break this is to change the angle**. Therefore, the functions $\sin$, $\cos$ and $\cos$ are functions that given an angle $\theta$ can return the ratio for the two triangle sides for a given angle **for a right angled triangle**.

<div align='center'>
    <h1> The Unit Circle </h1>
</div>

The unit circle is a central unifying framework of trignometry, extending the subject beyond the limited context of right-angled triangles into a continuous theory of angles and functions. While early trigonometry defines sine, cosine and tangent as ratios of sides in a triangle, this approach is inherently restricted to acue angles. The unit circle resolves this limitation by redefining trigonometric functions in terms of **geometry on a circle of radius one**, thereby allowing these functions to be defined for all real angles.

<div align='center'>
    <img src='./images/120.png' width='400'>
</div>

This describes a circle of radius one centered at the origin. The choice of radius one is not arbitrary, it eliminates scaling factors and allows trigometric ratios to correspond directly to coordinates.

An angle $\theta$ is measured from the positive $x\text{-axis}$. Where this rotation meets the unit circle determines a point $P = (x,y)$. This point defines the trigonometric functions,

- The $x\text{-coordinate}$ is $\cos(\theta)$
- The $y\text{-coordinate}$ is $\sin(\theta)$

Thus, rather than being ratios derived from a triangle, sine and cosine become **functions mapping angles to coordinates**. This shift in interpretation is the fundamental reason the unit circle is used.

The unit circle preserves and generalizes the definitions from right angle triangles. If one inscribes a right angle within the circle, by dropping a perpendicular line from $P$ to the $x\text{-axis}$. The hypotenuse has length $1$, resulting in,

```math
\begin{aligned}
\sin(\theta) &= \frac{\text{opposite}}{\text{hypotenuse}} = \frac{\text{opposite}}{1} = \text{opposite}\\
\cos(\theta) &= \frac{\text{adjacent}}{\text{hypotenuse}} =\frac{\text{adjacent}}{1} = \text{adjacent}
\end{aligned}
```

Within the unit circle framework, trigonometric functions are understood as periodic mappings,

```math
\sin : \mathbb{R} \to [-1,1] \\
\cos : \mathbb{R} \to [-1,1]
```

Each angle corresponds to a unique point on the circle, as $\theta$ increases, this point moves continuously around the circumfrance. This motion directly generates the wave-like graphs of sine and cosine when projected onto the coordinate axes.

Additionally, other trigonometric functions arise naturally.

```math
\tan(\theta) = \frac{\sin(\theta)}{\cos(\theta)}
```

Interpreted as the slope of the line from the origin $P$. This provides a geometric meaning to tangent as a rate of change, linking trigonometry to calculus.

<div align='center'>
    <h1> Changing Angles </h1>
</div>

Given a right angled triangle, the "opposite" is always opposite the angle. However, this can mean that the "opposite" side can change on the same triangle when moving the angle $\theta$.

<div align='center'>
    <img src='./images/128.png' width='400'>
</div>

A more coherent way to understand why the "opposite" side is always opposite the angle is through the unit circle. Consider a unit circle centered at the origin. Any angle $\theta$, measured from the positive $x\text{-axis}$, determines a point on the circle with coordinates,

```math
(\cos(\theta), \sin(\theta))
```

Here, cosine represents the horizontal $x$ position and sine represents the vertical $y$ position.

The reason the "opposite" side is always opposite the angle is that it **represents the vertical change produced by the angle**. As $\theta$ increases, the point moves around the circle and its height changes. This vertical change is exactly what $\sin(\theta)$ measures, so the "opposite" side is simply the geometric expression of that vertical component.

When you switch to a different angle in the triangle, the roles of the sides appear to change because you have changed your reference. In the unit circle terms, this is **equivalent to rotating the coordinate system**. The triangle itself stays the same, but what counts as horizontal and vertical shifts relative to the new angle.

In this way, the labels "opposite" and "adjacent" are not arbitrary. They are directly tied to the coordinate definitions of sine and cosine.

- Opposite = Vertical = $\sin(\theta)$
- Adjacent = Horizontal = $\cos(\theta)$

This is why the "opposite" side is always opposite the angle, it **reflects the vertical component** determined by that angle.

<div align='center'>
    <h1> Waves </h1>
</div>

The wave-like graphs of sine, cosine and tangent are direct consequences of their origins in the unit circle. As a point moves around the circle,

- **Sine** captures the vertical motion, producing a smooth oscillation.
- **Cosine** captures horizontal motion, creating the same wave shifted in phase.
- **Tangent** represents a ratio of these motions, leading to repeating but discontinuous curves.

Ultimately, trigonometric graphs are not just abstract shapes, they are visual representations of circular motion unfolding over time.

<div align='center'>
    <h3> The Sine Wave </h3>
</div>

To begin graphing the sine function, we will,

1. Plot the angle $\theta$ on the $x$ axis.
2. The length of the opposite side on the $y$ axis.

Here, the negative length means that the opposite side is in the lower semi-circle.

<div align='center'>
    <img src='./images/121.png' width='800'>
</div>

<div align='center'>
    <img src='./images/sin_wave_slowed.gif' width='800'>
</div>

We can extend the sine function to larger angle range. We can keep rotating around the circle, beyond $2\pi$. A negative angle will simply mean that we rotate clockwise.

The sine function is periodic, which means,

```math
\sin(x + 2\pi) = \sin(x)
```

This tells us that adding any multiple of $2\pi$ (one full rotation around the unit circle) does not change the value of sine. Effectively, you can think of sine as working in modulo $2\pi$. 

```math
4\pi ≡ 0 \ (\text{mod} \ 2\pi)
```

Therefore,

- $\sin(0) = 0$. This represents no movement.
- $sin(2\pi) = 0$. This represents one full rotation, and back to the same point as $\sin(0)$
- $sin(4\pi) = 0$. This represents two full rotations, and back to the same point as $\sin(0)$
- $sin(6\pi) = 0$. This represents three full rotations, and back to the same point as $\sin(0)$
- ...

<div align='center'>
    <img src='./images/sine_more_2_pi.gif' width='800'>
</div>

<div align='center'>
    <h3> The Cosine Wave </h3>
</div>

To begin graphing the cosine function, we will,

1. Plot the angle $\theta$ on the $x$ axis.
2. Plot the length of the $adjacent$ on the $y$ axis.

Here, the negative length means that the adjacent side is on the left half of the semi-circle. All properties of the cosine functions are equal.

Cosine literally means "complementary sine" because,

```math
\cos(\theta) = \sin(\frac{\pi}{2} -\theta)
```

<div align='center'>
    <img src='./images/123.png' width='200'>
</div>

<div align='center'>
    <img src='./images/cosine_wave_slowed.gif' width='800'>
</div>

<div align='center'>
    <img src='./images/122.png' width='800'>
</div>

<div align='center'>
    <h3> The Tangent Wave </h3>
</div>

Understanding the graph of $\tan(x)$ begins with clarifying what the function actually represents. Unlike $\sin$ and $\cos$, which describes positions on the unit circle, **tangent describes a relationship**. Specifically, a ratio that can be interpreted as a slope. This distinction

```math
y = \tan(x) = \frac{\sin(x)}{\cos(x)}
```

The tangent function is defined as a ratio of $\sin$ to $\cos$. On the unit circle, a point at angle $x$ has coordinates,

```math
(\cos(x), \sin(x))
```

Therefore, where $x$ represents the angle measured in radians.

- $\sin(x)$ represents the vertical position.
- $\cos(x)$ represents the horizontal position.

Taking the ratio $\frac{\sin(x)}{\cos(x)}$ gives,

```math
\frac{\text{vertical}}{\text{horizontal}} = \text{slope}
```

This finally means, $\tan(x)$ represents the slope of a line making an angle $x$ with the horizontal axis.

<div align='center'>
    <img src='./images/124.png' width='800'>
</div>

It's important to notice that we have a fraction. It is mathematically undefined to divide a number by 0. At the bottom of the fraction we have $\cos(x)$. Therefore, the tangent is undefined when

```math
\cos(x) = 0
```

This occurs at,

```math
x = \frac{\pi}{2} + n\pi
```

At these angles the slope becomes infinitely large. Therefore, the graph has vertical asymptotes at these values.

<div align='center'>
    <img src='./images/tan_wave_slowed.gif' width='800'>
</div>

While the function $\tan(x)$ represents the slope of the triangle, it can also be used to calculate an additional length illustrated below.

<div align='center'>
    <img src='./images/125.png' width='800'>
</div>

We begin this proof by creating a single right angled triangle on the unit circle with 3 lengths, $a$, $b$ and $c$. From here, we create a second triangle with another straight line that is a tangent to the point touching the circumfrance. 

Because a line tangent touches the circumfrance to create a right angle and they both have the same angle $\theta$, they're therefore similar triangles as both triangles have all 3 equal angles.

<div align='center'>
    <img src='./images/126.png' width='800'>
</div>

Therefore because these are similar triangles,

```math
\begin{align*}
\frac{a}{b} &= \frac{ra}{rb} \\
\frac{\sin(\theta)}{\cos(\theta)} &= \frac{ra}{1} \\
\frac{\sin(\theta)}{\cos(\theta)} &= ra \\
\tan(\theta) &= ra
\end{align*}
```

<div align='center'>
    <h3> Wave Manipulation </h3>
</div>

Trigonometric functions such as sine and cosine are commonly used to model waves and periodic behaviour. To fully describe how a wave behaves, mathematics use a generalized equation that accounts for changes in height, position and timing. Understanding this allows us to interpret and manipulate real-world wave patterns more effectively.

##### The Complete Wave Function

The general form of a trigonometric wave function is,

```math
y = a\sin(b(x-c)) + d
```

(or using cosine instead of sine)

Each parameter plays a specific role,

- $a$ is the **amplitude**, determining the height of the wave.
- $b$ affects the **period**, or how long it takes for one full cycle.
- $c$ is the **phase shift**, controlling horizontal movement.
- $d$ is the **vertical shift**, moving the graph up or down.

Together, these values allow the function to represent a wide range of wave behaviours.

<div align='center'>
    <img src='./images/132.png' width='700'>
</div>

#### Amplitude - $a$

<div align='center'>
    <img src='./images/sine_wave_amplitude.gif' width='800'>
</div>

#### Period - $b$

The period of a function $f(x)$ is the smallest positive number $T$ such that $f(x + T) = f(x)$ for all $x$. For a basic sine function we know,

```math
\sin(\theta + 2\pi) = \sin(\theta)
```

so the period of $\sin(x)$ when the argument is $x$ is $2\pi$. 

Now consider $y = \sin(10x)$, the argument is no longer $x$, it is $10x$. When $x$ increases by some amount $T$, the argument inside the sine increases by $10T$.

```math
\sin(10(x + T)) = \sin(10x + 10T)
```

For the function to repeat, the argument must increase by a full cycle of sine, i.e. by a multiple of $2\pi$. The smallest such positive value is exactly one full cycle,

```math
\begin{align*}
10T &= 2\pi \\
T &= \frac{2\pi}{10} \\
T &= \frac{\pi}{5}
\end{align*}
```

<div align='center'>
    <img src='./images/sine_wave_period.gif' width='800'>
</div>

#### Phase Shift - $c$

<div align='center'>
    <img src='./images/sine_wave_phase_shift.gif' width='800'>
</div>

#### Vertical Shift - $d$

<div align='center'>
    <img src='./images/sine_wave_vertical_shift.gif' width='800'>
</div>

<div align='center'>
    <h1> Recriprocal Trigonometric Functions </h1>
</div>

In trigonometry, the primary functions $\sin$, $\cos$ and $\tan$ are used to describe relationships between angles and ratios in right triangles and the unit circle. However, alongside these are additional functions, cotangent, secant and cosecant. While they may initially appear unfamiliar or unnecessary, they are not new ideas but rather extensions of the original three. Each is defined **as the repriprocal**, or inverse, of sine, cosine or tangent. Understanding these functions involves recognising how they relate directly back to the fundamental definitions and how they provide alternate ways of expressing the same geometric relationships.

The three recriprocals can be used to calculation additional lengths shown below, which are demonstrated in more detail in their sections shown below.

<div align='center'>
    <img src='./images/131.png' width='700'>
</div>


<div align='center'>
    <h3> Cosecant - The Reciprocal of Sine </h3>
</div>

```math
\csc(\theta) = \frac{1}{\sin(\theta)}
```

Cosecant is the recriprocal of the sine function. Since sine represents the vertical coordinate on the unit circle, cosecant can be understood as a scaled version of this vertical measurement. In geometric terms, it corresponds to the length of a line extending from the origin to a horizontal line tangent to the unit circle. Like secant, cosecant transforms a bounded value (between -1 and 1) into an unbounded one, which grows large as the sine value approaches zero. Although it is not as commonly used in introductory problems, cosecant simplifies many trigonometric expressions and plays an important role in more advanced mathematical contexts.

Below, we will demonstrate that $\csc(\theta)$ represents the length of the hypotenuse shown below. The second triangle was calculated from,

1. Creating a second right angled triangle by creating a line tangent that is perpendicular to the hypotentuse of the right angled triangle on the unit circle.
2. This will create a second angle $90 - \theta$
3. This will result in the final angle equaling $\theta$. This happens due to the calculation,

```math
\begin{aligned}
90 - \theta + 90 + z &= 180 \\
180 - \theta + z &= 180 \\
- \theta + z &= 0 \\
-\theta &= -z \\
\theta &= z
\end{aligned}
```

We can calculate this,

```math
\begin{aligned}
\sin(\theta) &= \frac{O}{H} \\
\sin(\theta) &= \frac{1}{H} \\
\frac{1}{\sin(\theta)} &= H
\end{aligned}
```

Because $\csc(\theta) = \frac{1}{\sin(\theta)}$ it follows,

```math
\csc(\theta) = H
```

<div align='center'>
    <img src='./images/129.png' width='500'>
</div>


<div align='center'>
    <h3> Secant - The Reciprocal of Cosine </h3>
</div>

```math
\sec(\theta) = \frac{1}{\cos(\theta)}
```

Secant is defined as the reciprocal of cosine. On the unit circle, cosine represents the horizontal coordinate of a point at a given angle. Taking its reciprocal produces a value that can be interpreted as a scaled or extended version of this horizontal distance. In geometric constructions, secant often appears as the length of a line extending from the origin to the vertical line tangent to the unit circle. This gives secant a clear spatial meaning, it measures how far a line at a given angle must extend to reach a fixed vertical boundary. While this interpretation is less immediately intuitive than sine or cosine, secant becomes especially useful in higher-level mathematics, particularly in calculus and trigonometric identities.


Creating a second right angled triangle by creating a line tangent that is perpendicular to the hypotentuse of the right angled triangle on the unit circle.

We can calculate this from,

```math
\begin{aligned}
\cos(\theta) &= \frac{A}{H} \\
\frac{1}{\cos(\theta)} &= \frac{H}{A} \\
\frac{1}{\cos(\theta)} &= \frac{H}{1} \\
\frac{1}{\cos(\theta)} &= H
\end{aligned}
```

Because of the definition,

```math
\sec(\theta) = \frac{1}{\cos(\theta)}
```

It follows,

```math
\sec(\theta) = H
```

<div align='center'>
    <img src='./images/130.png' width='500'>
</div>


<div align='center'>
    <h3> Cotangent - The Reciprocal of Tangent </h3>
</div>

```math
\cot(\theta) = \frac{\cos(\theta)}{\sin(\theta)}
```

Cotangent is defined as the recriprocal of the tangent function. Since tangent itself represents the ratio of sine to cosine, cotangent reverses this relationship. Geometrically, if tangent describes the slope of a line as "rise over run", then cotangent describes the situation as "run over rise". This means that cotangent can be interpreted as an inverse measure of steepness. When a line is very steep and tangent is large, cotangent is small. Cotangent is small when a line is shallow, contangent becomes large. Although less commonly used than tangent, cotangent provides an alternative perspective on the same angular relationship and is particularly useful in certain algebraic manipulations and identities.

Cotangent is also used to calculate an additional side of an extended triangle.

Below, we will demonstrate that $\cot(\theta)$ represents the length of the adjacent leg shown below. The second triangle was calculated from,

1. Creating a second right angled triangle by creating a line tangent that is perpendicular to the hypotentuse of the right angled triangle on the unit circle.
2. This will create a second angle $90 - \theta$
3. This will result in the final angle equaling $\theta$. This happens due to the calculation,

```math
\begin{aligned}
90 - \theta + 90 + z &= 180 \\
180 - \theta + z &= 180 \\
- \theta + z &= 0 \\
-\theta &= -z \\
\theta &= z
\end{aligned}
```

We can calculate this,

```math
\begin{aligned}
\tan(\theta) &= \frac{O}{A} \\
\tan(\theta) &= \frac{1}{A} \\
\frac{\sin(\theta)}{\cos(\theta)} &= \frac{1}{A} \\
\frac{\cos(\theta)}{\sin(\theta)} &= \frac{A}{1} \\
\frac{\cos(\theta)}{\sin(\theta)} &= A
\end{aligned}
```

Because of the definition,

```math
\cot(\theta) = \frac{\cos(\theta)}{\sin(\theta)}
```

It follows,

```math
\cot(\theta) = A
```

<div align='center'>
    <img src='./images/129.png' width='500'>
</div>
